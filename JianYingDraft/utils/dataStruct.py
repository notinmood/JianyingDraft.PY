"""
 * @file   : dataStruct.py
 * @time   : 上午8:19
 * @date   : 2024/4/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from dataclasses import dataclass, field
from typing import Literal, Tuple, List

AnimationTypes = Literal["in", "out", "group"]


@dataclass
class ResourceData:
    """
    资源数据
    """
    guid: str = ""
    name: str = ""
    resource_id: str = ""


@dataclass
class DurationResourceData(ResourceData):
    """
    延时资源数据
    """
    start: int = 0
    duration: int = 0


@dataclass
class EffectData(DurationResourceData):
    """
    特效数据
    """
    pass


@dataclass
class TransitionData(DurationResourceData):
    """
    转场数据
    """
    pass


@dataclass
class AnimationData(DurationResourceData):
    """
    动画数据
    """
    animation_type: AnimationTypes = "in"


@dataclass
class ColorData:
    """
    颜色RGB
    """
    R: float = 0.0
    G: float = 0.0
    B: float = 0.0

    def __int__(self, R: float, G: float, B: float):
        """
        初始化
        @param R: red
        @param G: green
        @param B: blue
        @return:
        """
        self.R, self.G, self.B = R, G, B


@dataclass
class SubtitleStrokesData:
    """
    字幕描边数据
    """

    # 颜色
    color: ColorData = field(default_factory=lambda: ColorData(0.0, 0.0, 0.0))

    # 粗细
    width: float = 0.8


@dataclass
class SubtitleFontData:
    """
    字幕字体数据
    """

    # 颜色
    color: ColorData = field(default_factory=lambda: ColorData(1.0, 1.0, 1.0))

    # 字体大小
    size: float = 8

    # 描边数据
    strokes: SubtitleStrokesData = None

    def set_enabled_strokes(self):
        """
        启用描边
        @return:self
        """
        if self.strokes is None:
            self.strokes = SubtitleStrokesData()
        return self
