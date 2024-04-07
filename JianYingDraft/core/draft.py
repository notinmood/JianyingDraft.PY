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
from JianYingDraft.core.media import Media
from JianYingDraft.core.mediaFactory import MediaFactory
from JianYingDraft.core import template


class Draft:
    _draft_content_file_base_name = "draft_content.json"
    _draft_meta_info_file_base_name = "draft_meta_info.json"

    def __init__(self, name: str = ""):
        if not name:
            name = time.strftime("%Y%m%d.%H%M%S", time.localtime())
        pass

        # 草稿保存位置
        self._drafts_root = ConfigHelper.get_item("JianYingDraft.basic", "drafts_root", "C:\\Jianying.Drafts")
        self._draft_folder = os.path.join(self._drafts_root, name)

        # 从模板获取草稿的基础数据
        here = os.path.abspath(os.path.dirname(__file__))
        template_folder = os.path.join(os.path.dirname(here), "template")
        self._draft_content_data = tools.read_json(os.path.join(template_folder, self._draft_content_file_base_name))
        self._draft_meta_info_data = tools.read_json(
            os.path.join(template_folder, self._draft_meta_info_file_base_name))

        # 初始化草稿内容信息
        self._draft_content_data['id'] = tools.generate_id()

        # 初始化草稿元数据信息
        self._draft_meta_info_data['id'] = tools.generate_id()
        self._draft_meta_info_data['draft_fold_path'] = self._draft_folder.replace("\\", '/')
        self._draft_meta_info_data['draft_timeline_metetyperials_size_'] = 0
        self._draft_meta_info_data['tm_draft_create'] = DateTimeHelper.get_timestamp(formatter=16)
        self._draft_meta_info_data['tm_draft_modified'] = DateTimeHelper.get_timestamp(formatter=16)
        self._draft_meta_info_data['draft_root_path'] = self._drafts_root.replace("/", "\\")
        self._draft_meta_info_data['draft_removable_storage_device'] = self._drafts_root.split(':/')[0]

        # 为方便调用目标文件中的material部分，定义快捷变量
        self._materials_in_draft_content: {} = self._draft_content_data['materials']  # 草稿内容库的素材

        self._materials_in_draft_meta_info: {} = self._draft_meta_info_data['draft_materials']  # 草稿元数据库的素材
        self._videos_material_in_draft_meta_info = self._materials_in_draft_meta_info[0]['value']
        self._audios_material_in_draft_meta_info = self._materials_in_draft_meta_info[6]['value']  # type为8的那条

        self._tracks_in_draft_content: [] = self._draft_content_data['tracks']  # 草稿内容库的轨道

    def add_media(self, media_file_full_name: str, start=0, duration=0, index=0, **kwargs):
        """
        添加媒体到草稿
        """
        _index = index

        media = MediaFactory.create(media_file_full_name, start=start, duration=duration, **kwargs)

        if media is None:
            return
        pass

        # 将媒体信息添加到draft的素材库
        self.__add_media_to_content_materials(media)

        # 将媒体信息添加到draft的轨道库
        self.__add_media_to_content_tracks(media)

        # 将媒体信息添加到draft的元数据库
        self.__add_media_to_meta_info(media)

    def add_effect(self, effect_path: str, effect_name: str, start=0, duration=0, index=0):
        """
        添加特效到草稿
        @param index:
        @param duration:
        @param start:
        @param effect_path: 特效所在的路径（内置特效时请设置本参数为空；外置的特效时使用。）
        @param effect_name: 特效的名称（内置特效总共有限的几个名称中的一个；外置特效的名称随意设定。）
        """
        pass

    def calc_draft_duration(self):
        """
        获取（通过计算）草稿的时长
        """
        return self.__get_track_duration("video")

    def save(self):
        """
        保存草稿
        """
        # 校准时长信息
        self.__calc_duration()

        # 新建项目文件夹
        tools.create_folder(self._draft_folder)

        # 持久化草稿
        draft_content_file_full_name = os.path.join(self._draft_folder, self._draft_content_file_base_name)
        draft_meta_info_file_full_name = os.path.join(self._draft_folder, self._draft_meta_info_file_base_name)
        tools.write_json(draft_content_file_full_name, self._draft_content_data)
        tools.write_json(draft_meta_info_file_full_name, self._draft_meta_info_data)

    def __add_media_to_content_materials(self, media: Media):
        """
        添加媒体信息到素材内容库的素材部分：
        """

        for _key, _value in media.material_data_for_content.items():
            _key = str(_key)

            # 排除中转使用的临时信息
            if _key.startswith("X."):
                continue
            pass

            self._materials_in_draft_content[_key].append(_value)
        pass

    def __add_media_to_content_tracks(self, media: Media):
        """
        添加媒体信息到素材内容库的轨道部分：
        """

        all_tracks = self._tracks_in_draft_content
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
            self._tracks_in_draft_content.append(target_track)
        pass

        # 添加新片段之前轨道总时长
        track_duration = self.__get_track_duration(media.category_type)

        # 设置新segment的在轨道上的开始时间
        segment_source_timerange = media.segment_data_for_content["target_timerange"]
        segment_source_timerange["start"] = track_duration
        target_track["segments"].append(media.segment_data_for_content)

    def __add_media_to_meta_info(self, media: Media):
        """
        添加媒体信息到元数据库：
        """

        if media.category_type == "video":
            self._videos_material_in_draft_meta_info.append(media.data_for_meta_info)
        else:
            self._audios_material_in_draft_meta_info.append(media.data_for_meta_info)
        pass

    def __calc_duration(self):
        """
        计算并设置草稿的总时长
        计算策略为（以视频时长为基准，让其他地方的duration相对此时长对齐）：
        1. 以视频轨道中最后一个segment的结束时间作为总时长
        2. 将音频轨道的总时长设置为第一步计算的结果
        3. 设置草稿的总时长字段duration（文件content和meta_info都要设置）
        """
        # 1. 获取视频轨道的总时长
        video_durations = self.__get_track_duration("video")
        # 2. 设置音频轨道的总时长
        # TODO:xiedali@2024/03/23 暂时只设置audio
        self.__set_track_duration("audio", video_durations)

        # 3. 设置草稿的总时长
        self._draft_content_data['duration'] = video_durations
        self._draft_meta_info_data['tm_duration'] = video_durations

    def __get_track_duration(self, track_type: str):
        all_tracks = self._tracks_in_draft_content
        target_track = None
        for _track in all_tracks:
            if _track["type"] == track_type:
                target_track = _track
                break
            pass
        pass

        if not target_track:
            return 0
        pass

        if len(target_track['segments']) == 0:
            return 0
        pass

        # 轨道总时长
        last_segment = target_track['segments'][-1]
        last_segment_timerange = last_segment['target_timerange']
        track_duration = last_segment_timerange['start'] + last_segment_timerange['duration']
        return track_duration

    def __set_track_duration(self, track_type: str, duration: int):
        all_tracks = self._tracks_in_draft_content
        target_track = None
        for _track in all_tracks:
            if _track["type"] == track_type:
                target_track = _track
                break
            pass
        pass

        if not target_track:
            return
        pass

        segments = target_track['segments']

        done = False
        for segment in segments:
            ss_timerange = segment['source_timerange']
            st_timerange = segment['target_timerange']

            if done:
                st_timerange['start'] = 0
                st_timerange['duration'] = 0

                ss_timerange['start'] = 0
                ss_timerange['duration'] = 0
            else:
                segment_start = st_timerange['start']
                segment_duration = st_timerange['duration']
                segment_end = segment_start + segment_duration

                if segment_end > duration:
                    ss_timerange['duration'] = duration - segment_start
                    st_timerange['duration'] = duration - segment_start
                    done = True
                pass
            pass
        pass
