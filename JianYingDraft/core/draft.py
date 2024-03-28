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

from utils import tools
from core.media import Media
from core.mediaFactory import MediaFactory
from core import template


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
        self.materials_in_draft_content: {} = self.draft_content_data['materials']  # 草稿内容库的素材

        self.materials_in_draft_meta_info: {} = self.draft_meta_info_data['draft_materials']  # 草稿元数据库的素材
        self.videos_material_in_draft_meta_info = self.materials_in_draft_meta_info[0]['value']
        self.audios_material_in_draft_meta_info = self.materials_in_draft_meta_info[6]['value']  # type为8的那条

        self.tracks_in_draft_content: [] = self.draft_content_data['tracks']  # 草稿内容库的轨道

    def add_media(self, media: str | Media, start=0, duration=0, index=0):
        """
        添加媒体到草稿
        """

        # TODO:xiedali@2024/03/28 需要重新确认以下index的作用，其应该是表示轨道信息的时候使用，不需要向media传送

        if isinstance(media, str):
            media = MediaFactory.create(media, start=start, duration=duration, index=index)
        pass

        # 将媒体信息添加到draft的素材库
        self.__add_media_to_content_materials(media)

        # 将媒体信息添加到draft的轨道库
        self.__add_media_to_content_tracks(media)

        # 将媒体信息添加到draft的元数据库
        self.__add_media_to_meta_info(media)

    pass

    def __add_media_to_content_materials(self, media: Media):
        """
        添加媒体信息到素材内容库的素材部分：
        """
        if not isinstance(media, Media):
            return
        pass

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

    def __add_media_to_content_tracks(self, media: Media):
        """
        添加媒体信息到素材内容库的轨道部分：
        """
        if not isinstance(media, Media):
            return
        pass

        # if media not in self.materials:
        #     self.materials_in_draft_meta_info.append(media.data_for_meta_info)
        # pass
        # TODO:xiedali@2024/03/27 是否需要检查媒体已经存在？

        all_tracks = self.tracks_in_draft_content
        target_track = None
        for _track in all_tracks:
            if _track["type"] == media.category_type:
                target_track = _track
                break
            pass
        pass

        if target_track is None:
            target_track = template.get_track()
            target_track["type"] = media.category_type
            all_tracks.append(target_track)
        pass

        # 轨道总时长
        track_duration = 0
        if len(target_track['segments']) != 0:
            last_segment = target_track['segments'][-1]
            last_segment_timerange = last_segment['target_timerange']
            track_duration = last_segment_timerange['start'] + last_segment_timerange['duration']
        pass

        ## TODO:xiedali@2024/03/28 设置新segment的duration等信息

        target_track["segments"].append(media.segment_data_for_content)

    def __add_media_to_meta_info(self, media: Media):
        """
        添加媒体信息到元数据库：
        """
        if not isinstance(media, Media):
            return
        pass

        # if media not in self.materials:
        #     self.materials_in_draft_meta_info.append(media.data_for_meta_info)
        # pass
        # TODO:xiedali@2024/03/27 是否需要检查媒体已经存在？

        if media.category_type == "video":
            self.videos_material_in_draft_meta_info.append(media.data_for_meta_info)
        else:
            self.audios_material_in_draft_meta_info.append(media.data_for_meta_info)
        pass

    def save(self):
        """
        保存草稿
        """
        # self.draft_content_data['tracks'] = self.tracks.composite()  # 整合轨道
        # TODO:xiedali@2024/03/23 加入一个总时长的计算，并设置各处总时长字段duration

        # 新建项目文件夹
        tools.create_folder(self.draft_folder)

        draft_content_file_full_name = os.path.join(self.draft_folder, self.draft_content_file_base_name)
        draft_meta_info_file_full_name = os.path.join(self.draft_folder, self.draft_meta_info_file_base_name)

        tools.write_json(draft_content_file_full_name, self.draft_content_data)
        tools.write_json(draft_meta_info_file_full_name, self.draft_meta_info_data)
