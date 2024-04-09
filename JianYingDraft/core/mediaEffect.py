"""
 * @file   : materialVideo.py
 * @time   : 15:23
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from pathlib import Path

from BasicLibrary.io.dirHelper import DirHelper

from JianYingDraft.core import template
from JianYingDraft.core.media import Media


class MediaEffect(Media):

    def __init__(self, **kwargs):
        kwargs.setdefault("media_type", "effect")
        super().__init__(**kwargs)

    @staticmethod
    def get_inner_effect_path(effect_name):
        """
        获取内置特效路径
        """
        here = Path(__file__).resolve().parent
        effect_path = here.parent / '.res' / 'effects'
        sub_dirs = DirHelper.get_sub_dirs(effect_path)
        effect_path = ""
        for sub_dir in sub_dirs:
            sub_dir_base_name = Path(sub_dir).resolve().name
            if sub_dir_base_name == effect_name:
                effect_path = sub_dir
                break
            pass
        pass

        return effect_path

    pass

    def _set_material_data_for_content(self):
        """
        设置草稿文件的content部分
        """
        effect_path = self.kwargs.get("effect_path")
        effect_name = self.kwargs.get("effect_name")

        # 仅指定特效名称，不指定特效路径时，为内置特效
        if not effect_path and effect_name:
            effect_path = self.get_inner_effect_path(effect_name)
        pass

        effect_data = template.get_video_effect(self.id, effect_name, effect_path)

        self.material_data_for_content["video_effects"] = effect_data

        # 将特效的各种业务信息为空，后续供track下的segment使用
        self.material_data_for_content["X.extra_material_refs"] = []

    pass
