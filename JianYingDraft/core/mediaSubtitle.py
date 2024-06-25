"""
 * @file   : materialVideo.py
 * @time   : 15:23
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import json

from JianYingDraft.core import template
from JianYingDraft.core.media import Media
from JianYingDraft.utils import tools
import pysrt

from utils.dataStruct import SubtitleStrokesData, SubtitleFontData


def RGB_to_Hex(tmp: list):
    rgb = tmp
    strs = '#'
    for i in rgb:
        num = int(i)  # 将str转int
        # 将R、G、B分别转化为16进制拼接转换并大写
        strs += str(hex(num))[-2:].replace('x', '0').upper()

    return strs


class MediaSubtitle(Media):
    def __init__(self, **kwargs):
        kwargs.setdefault("media_type", "subtitle")
        super().__init__(**kwargs)

    pass

    def _set_material_data_for_content(self):
        ma_id = tools.generate_id()

        self.material_data_for_content['material_animations'] = template.get_speed(ma_id)
        text_data = self.__generate_main_data()
        self.material_data_for_content["texts"] = text_data
        # 将素材的各种业务信息，暂时保存起来，后续供track下的segment使用
        self.material_data_for_content["X.extra_material_refs"] = [ma_id, ]

    def __generate_main_data(self):
        entity = template.get_subtitle(self.id)

        font_info: SubtitleFontData = self.kwargs.get("font_info")

        content = template.get_subtitle_content(self.kwargs.get("info").text, font_info=font_info)

        entity["content"] = json.dumps(content)
        return entity


pass
