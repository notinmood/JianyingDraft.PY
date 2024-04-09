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
    @staticmethod
    def get_effect_dict():
        """
        获取特效列表
        """

        effect_dict = {
            "仙女棒": "7314565034586149403",
            "烟雾": "6733145063997575694",
            "星光绽放": "6760243564598268420",
            "萤火": "7006265184050221576",
            "镜头变焦": "6868546663607177736",
            "星雨": "6766488666261950989",
            "萤光飞舞": "6877098783209951751",

            "星星灯": "6903072502369489422",
            "烟花": "6782461740274684424",
            "星夜": "7008149210159649294",
            "星火": "6715209198109463054",
            "萤光": "6715209844216828420",
            "星河": "6734498838410695175",
            "光斑飘落": "6899747276718084622",

            "庆祝彩带": "6984685757508096520",
            "泡泡": "6806254230614053383",
            "星月童话": "6967255330958873124",
            "彩带": "7012933493663470088",
            "小花花": "6926823177670627848",
            "蝴蝶": "6706773499836404228",
            "落叶": "6740863535674298888",
        }

        return effect_dict

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
        effect_name_or_resource_id = self.kwargs.get("effect_name_or_resource_id")

        resource_id = "7012933493663470088"  # 缺省的特效资源ID表示小花花特效
        effect_name = "小花花"
        if isinstance(effect_name_or_resource_id, str):
            effect_name = effect_name_or_resource_id
            if effect_name in self.get_effect_dict():
                resource_id = self.get_effect_dict()[effect_name]
            pass
        elif isinstance(effect_name_or_resource_id, int):
            resource_id = str(effect_name_or_resource_id)
            effect_name = resource_id
        pass

        effect_data = template.get_video_effect(self.id, resource_id, effect_name)

        self.material_data_for_content["video_effects"] = effect_data

        # 将特效的各种业务信息为空，后续供track下的segment使用
        self.material_data_for_content["X.extra_material_refs"] = []

    pass
