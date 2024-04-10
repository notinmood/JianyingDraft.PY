"""
 * @file   : draftContext.py
 * @time   : 上午10:38
 * @date   : 2024/4/9
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import os

from BasicLibrary.projectHelper import ProjectHelper

from JianYingDraft.core.draft import Draft


class DraftContext:
    """
    将创建和使用draft的公共功能都集中在此处
    """

    def __init__(self, draft_name=""):
        root_path = ProjectHelper.get_root_physical_path()
        middle_path = ".res"
        self.res_path = os.path.join(root_path, middle_path)
        self.draft = Draft(draft_name)
        ...

    def __enter__(self):
        return self
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 2. 添加背景音乐，音频长度会根据视频的长度自动剪截
        music_full_name = os.path.join(self.res_path, "似是故人来.mp3")
        ## 2.1. 最简方式:直接添加音频文件的地址即可。
        # draft.add_media(music_full_name)
        ## 2.2. 也可以给音频指定淡入淡出时长
        self.draft.add_media(music_full_name, fade_in_duration=1_000_000, fade_out_duration=1_500_000)

        self.draft.save()
        ...


...
