"""
 * @file   : __.py
 * @time   : 11:12
 * @date   : 2024/3/20
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""

import os
import time

from BasicLibrary.configHelper import ConfigHelper
from BasicLibrary.projectHelper import ProjectHelper

from JianyingDraft.utils import tools
from JianyingDraft.core import template
from JianyingDraft.core.materialMisc import MaterialMisc
from JianyingDraft.core.tracks import Tracks


class Draft:
    draft_content_file = "draft_content.json"
    draft_meta_info_file = "draft_meta_info.json"

    def __init__(self, name: str = ""):
        # 路径变量
        if not name:
            name = time.strftime("%Y%m%d.%H%M%S", time.localtime())
        pass

        self.drafts_root = ConfigHelper.get_item("basic", "drafts_root")
        self.draft_folder = os.path.join(self.drafts_root, name)
        self.draft_content_path = os.path.join(self.draft_folder, self.draft_content_file)
        self.draft_meta_info_path = os.path.join(self.draft_folder, self.draft_meta_info_file)

        # 新建项目文件夹
        tools.create_folder(self.draft_folder)

        # 读取草稿模板
        here = os.path.abspath(os.path.dirname(__file__))
        template_folder = os.path.join(os.path.dirname(here), "template")
        self.draft_content_data = tools.read_json(os.path.join(template_folder, self.draft_content_file))
        self.draft_meta_info_data = tools.read_json(os.path.join(template_folder, self.draft_meta_info_file))

        # 初始化草稿内容信息
        self.draft_content_data['id'] = tools.generate_id()

        # 初始化素材信息
        self.draft_meta_info_data['id'] = tools.generate_id()
        self.draft_meta_info_data['draft_fold_path'] = self.draft_folder.replace("\\", '/')
        self.draft_meta_info_data['draft_timeline_metetyperials_size_'] = 0
        self.draft_meta_info_data['tm_draft_create'] = time.time()
        self.draft_meta_info_data['tm_draft_modified'] = time.time()
        self.draft_meta_info_data['draft_root_path'] = self.drafts_root.replace("/", "\\")
        self.draft_meta_info_data['draft_removable_storage_device'] = self.drafts_root.split(':/')[0]

        # 创建变量
        self.materials_in_draft_meta_info: list = self.draft_meta_info_data['draft_materials'][0]['value']  # 草稿素材库
        self.materials_in_draft_content: list = self.draft_content_data['materials']  # 内容素材库
        self.tracks = Tracks()  # 轨道
        self.materials = {}

    # def add_media_to_materials(self, media):
    #     """
    #     添加媒体信息到素材库：
    #     1. 如果是文件路径先转化为DraftMaterial
    #     2. 如果是DraftMaterial类直接添加到素材库
    #     """
    #     if isinstance(media, Material):
    #         self.materials[media.file_Path] = media
    #         self.materials_in_draft_meta_info.append(media.data)
    #         return media
    #     pass
    #
    #     if media not in self.materials:
    #         m = Material(media)
    #         self.materials[media] = m
    #         self.materials_in_draft_meta_info.append(m.data)
    #         return m
    #     else:
    #         return self.materials[media]
    #     pass

    def add_material(self, material: str | MaterialMisc, start=0, duration=0, index=0):
        if duration == 0:
            duration = material.duration
        pass

        segment = template.get_segment()
        track = []

        if isinstance(material, str):
            material = MaterialMisc(material)
        pass

        if material.material_type == 'video':
            track = self.tracks.add_video_track(index)
        elif material.material_type == 'photo':
            track = self.tracks.add_video_track(index)
        elif material.material_type == 'audio':
            track = self.tracks.add_audio_track(index)
        elif material.material_type == 'text':
            track = self.tracks.add_text_track(index)

        # 轨道总时长
        track_duration = 0
        if len(track['segments']) != 0:
            last_segment = track['segments'][-1]
            last_segment_timerange = last_segment['target_timerange']
            track_duration = last_segment_timerange['start'] + last_segment_timerange['duration']
        pass

        basic_info, extra_material_refs, material_id = MaterialMisc.gen_basic_and_refs_info(material)

        for key in basic_info:
            self.materials_in_draft_content[key].append(basic_info[key])
        pass

        segment['extra_material_refs'] = extra_material_refs
        segment['material_id'] = material_id
        segment['source_timerange'] = {"duration": duration, "start": start}
        segment['target_timerange'] = {"duration": duration, "start": track_duration}

        self.tracks.add_segment(material.material_type, segment, index)

    def save(self):
        """保存草稿"""
        self.draft_content_data['tracks'] = self.tracks.composite()  # 覆盖轨道
        tools.write_json(self.draft_content_path, self.draft_content_data)
        tools.write_json(self.draft_meta_info_path, self.draft_meta_info_data)
