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
from BasicLibrary.data.dateTimeHelper import DateTimeHelper

from JianYingDraft.utils import tools
from JianYingDraft.core.tracks import Tracks
from JianYingDraft.core.media import Media
from JianYingDraft.core.mediaFactory import MediaFactory


class Draft:
    draft_content_file_base_name = "draft_content.json"
    draft_meta_info_file_base_name = "draft_meta_info.json"

    def __init__(self, name: str = ""):
        if not name:
            name = time.strftime("%Y%m%d.%H%M%S", time.localtime())
        pass

        # 草稿保存位置
        self.drafts_root = ConfigHelper.get_item("JianYingDraft.basic", "drafts_root", "C:\\Jianying.Drafts")
        self.draft_folder = os.path.join(self.drafts_root, name)

        # 从模板获取草稿的基础数据
        here = os.path.abspath(os.path.dirname(__file__))
        template_folder = os.path.join(os.path.dirname(here), "template")
        self.draft_content_data = tools.read_json(os.path.join(template_folder, self.draft_content_file_base_name))
        self.draft_meta_info_data = tools.read_json(os.path.join(template_folder, self.draft_meta_info_file_base_name))

        # 初始化草稿内容信息
        self.draft_content_data['id'] = tools.generate_id()

        # 初始化草稿元数据信息
        self.draft_meta_info_data['id'] = tools.generate_id()
        self.draft_meta_info_data['draft_fold_path'] = self.draft_folder.replace("\\", '/')
        self.draft_meta_info_data['draft_timeline_metetyperials_size_'] = 0
        self.draft_meta_info_data['tm_draft_create'] = DateTimeHelper.get_timestamp(formatter=16)
        self.draft_meta_info_data['tm_draft_modified'] = DateTimeHelper.get_timestamp(formatter=16)
        self.draft_meta_info_data['draft_root_path'] = self.drafts_root.replace("/", "\\")
        self.draft_meta_info_data['draft_removable_storage_device'] = self.drafts_root.split(':/')[0]

        # 为方便调用目标文件中的material部分，定义快捷变量
        self.materials_in_draft_content: {} = self.draft_content_data['materials']  # 草稿素材内容库

        self.materials_in_draft_meta_info: {} = self.draft_meta_info_data['draft_materials']  # 草稿素材元数据库
        self.videos_material_in_draft_meta_info = self.materials_in_draft_meta_info[0]['value']
        self.audios_material_in_draft_meta_info = self.materials_in_draft_meta_info[8]['value']

        # 定义最重要的容器变量
        self.tracks = Tracks()  # 本草稿使用的所有的轨道
        self.medias = []  # 本草稿使用的所有的媒体

    def add_media(self, media: str | Media, start=0, duration=0, index=0):
        """
        添加媒体到草稿
        """

        if isinstance(media, str):
            media = MediaFactory.create(media, start=start, duration=duration, index=index)
        pass

        # 将媒体信息添加到draft的素材库
        self.add_media_to_content_materials(media)

        # 将媒体信息添加到draft的轨道库
        # TODO:xiedali@2024/03/27
        ...

        # 将媒体信息添加到draft的元数据库
        self.add_media_to_meta_info(media)

        # if isinstance(material, str):
        #     material = MaterialMate(material)
        # pass

        # if duration == 0:
        #     duration = material.duration
        # pass
        #
        # segment = template.get_segment()
        # track = []
        #
        # if material.material_type == 'video':
        #     track = self.tracks.add_video_track(index)
        # elif material.material_type == 'photo':
        #     track = self.tracks.add_video_track(index)
        # elif material.material_type == 'audio':
        #     track = self.tracks.add_audio_track(index)
        # elif material.material_type == 'text':
        #     track = self.tracks.add_text_track(index)
        #
        # # 轨道总时长
        # track_duration = 0
        # if len(track['segments']) != 0:
        #     last_segment = track['segments'][-1]
        #     last_segment_timerange = last_segment['target_timerange']
        #     track_duration = last_segment_timerange['start'] + last_segment_timerange['duration']
        # pass
        #
        # basic_info, extra_material_refs, material_id = MaterialMate.gen_basic_and_refs_info(material)
        #
        # for key in basic_info:
        #     self.materials_in_draft_content[key].append(basic_info[key])
        # pass
        #
        # segment['extra_material_refs'] = extra_material_refs
        # segment['material_id'] = material_id
        # segment['source_timerange'] = {"duration": duration, "start": start}
        # segment['target_timerange'] = {"duration": duration, "start": track_duration}
        #
        # self.tracks.add_segment(material.material_type, segment, index)
        #
        # self.add_material_to_meta_info(material)

    pass

    def add_media_to_content_materials(self, media: str | Media):
        """
        添加媒体信息到元数据库：
        1. 如果是文件路径先转化为Media
        2. 如果是Media类直接添加到元数据库
        """
        if isinstance(media, str):
            media = MediaFactory.create(media)
        pass

        if isinstance(media, Media):
            # if media not in self.materials:
            #     self.materials_in_draft_meta_info.append(media.data_for_meta_info)
            # pass
            # TODO:xiedali@2024/03/27 是否需要检查媒体已经存在？

            for _key, _value in media.material_data_for_content.items():
                _key = str(_key)

                # 排出中转使用的临时信息
                if _key.startswith("X."):
                    continue
                pass

                self.materials_in_draft_content[_key].append(_value)
            pass
        pass

    def add_media_to_meta_info(self, media: str | Media):
        """
        添加媒体信息到元数据库：
        1. 如果是文件路径先转化为Media
        2. 如果是Media类直接添加到元数据库
        """
        if isinstance(media, str):
            media = MediaFactory.create(media)
        pass

        if isinstance(media, Media):
            # if media not in self.materials:
            #     self.materials_in_draft_meta_info.append(media.data_for_meta_info)
            # pass
            # TODO:xiedali@2024/03/27 是否需要检查媒体已经存在？

            if media.material_type == "video":
                self.videos_material_in_draft_meta_info.append(media.data_for_meta_info)
            else:
                self.audios_material_in_draft_meta_info.append(media.data_for_meta_info)
            pass
        pass

    def save(self):
        """
        保存草稿
        """
        self.draft_content_data['tracks'] = self.tracks.composite()  # 整合轨道
        # TODO:xiedali@2024/03/23 加入一个总时长的计算，并设置各处总时长字段duration

        # 新建项目文件夹
        tools.create_folder(self.draft_folder)

        draft_content_file_full_name = os.path.join(self.draft_folder, self.draft_content_file_base_name)
        draft_meta_info_file_full_name = os.path.join(self.draft_folder, self.draft_meta_info_file_base_name)

        tools.write_json(draft_content_file_full_name, self.draft_content_data)
        tools.write_json(draft_meta_info_file_full_name, self.draft_meta_info_data)
