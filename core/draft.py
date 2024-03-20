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
from core import util
from core import template
from core.material import Material
from core.track import Tracks


class Draft:
    drafts_folder = "Z:/jianying/Data/JianyingPro Drafts"
    template_folder = "./template/"
    content_file = "draft_content.json"
    meta_info_file = "draft_meta_info.json"

    def __init__(self, name: str = "Test"):
        # 路径变量
        self.name = name
        self.folder = os.path.join(self.drafts_folder, name)
        self.content_path = os.path.join(self.folder, self.content_file)
        self.meta_info_path = os.path.join(self.folder, self.meta_info_file)
        # 新建项目文件夹
        util.new_folder(self.folder)
        # 读取草稿模板
        self.content = util.read_json(os.path.join(self.template_folder, self.content_file))
        self.meta_info = util.read_json(os.path.join(self.template_folder, self.meta_info_file))
        # 初始化草稿内容信息
        self.content['id'] = util.generate_id()
        # 初始化素材信息
        self.meta_info['id'] = util.generate_id()
        self.meta_info['draft_fold_path'] = self.folder.replace("\\", '/')
        self.meta_info['draft_timeline_metetyperials_size_'] = 0
        self.meta_info['tm_draft_create'] = time.time()
        self.meta_info['tm_draft_modified'] = time.time()
        self.meta_info['draft_root_path'] = self.drafts_folder.replace("/", "\\")
        self.meta_info['draft_removable_storage_device'] = self.drafts_folder.split(':/')[0]
        # 创建变量
        self.draft_materials: list = self.meta_info['draft_materials'][0]['value']  # 草稿素材库
        self.content_materials: list = self.content['materials']  # 内容素材库
        self.tracks = Tracks()  # 轨道
        self.materials = {}

    def add_media_to_materials(self, file):
        """
            添加媒体到素材库

            如果是DraftMaterial类直接添加到素材库

            如果是文件路径先转化为DraftMaterial
        """
        if type(file) == Material:
            self.materials[file.file_Path] = file
            self.draft_materials.append(file.data)
            return file
        if file not in self.materials:
            mate = Material(file)
            self.materials[file] = mate
            self.draft_materials.append(mate.data)
            return mate
        else:
            return self.materials[file]

    def _content_material(self, material: Material):
        materials = {}
        extra_material_refs = []
        if material.mate_type == 'video':
            materials['speeds'] = template.speed()
            materials['sound_channel_mappings'] = template.sound_channel_mapping()
            materials['canvases'] = template.canvas()
        elif material.mate_type == 'photo':
            pass
        elif material.mate_type == 'audio':
            materials['speeds'] = template.speed()
            materials['sound_channel_mappings'] = template.sound_channel_mapping()
            materials['beats'] = template.sound_channel_mapping()
        elif material.mate_type == 'text':
            materials['material_animations'] = template.material_animation()

        materials[f'{material.track_type}s'] = material.content_material

        for key in materials:
            extra_material_refs.append(materials[key]['id'])
        return materials, extra_material_refs, material.content_material['id']

    def add_media_to_track(self, media, start=0, duration=0, index=0):
        if duration == 0:
            duration = media.duration

        segment = template.segment()
        track = []

        if type(media) == str:
            media = Material(media)

        if media.mate_type == 'video':
            track = self.tracks.add_video_track(index)
        elif media.mate_type == 'photo':
            track = self.tracks.add_video_track(index)
        elif media.mate_type == 'audio':
            track = self.tracks.add_audio_track(index)
        elif media.mate_type == 'text':
            track = self.tracks.add_text_track(index)

        # 轨道总时长
        track_duration = 0
        if len(track['segments']) != 0:
            track_duration = track['segments'][-1]['target_timerange']['duration'] + \
                             track['segments'][-1]['target_timerange']['start']

        materials, extra_material_refs, material_id = self._content_material(media)
        for key in materials:
            self.content_materials[key].append(materials[key])

        segment['extra_material_refs'] = extra_material_refs
        segment['material_id'] = material_id
        segment['source_timerange'] = {"duration": duration, "start": start}
        segment['target_timerange'] = {"duration": duration, "start": track_duration}

        self.tracks.to_track(media.mate_type, segment, index)

    def save(self):
        """保存草稿"""
        self.content['tracks'] = self.tracks._composite()  # 覆盖轨道
        util.write_json(self.content_path, self.content)
        util.write_json(self.meta_info_path, self.meta_info)
