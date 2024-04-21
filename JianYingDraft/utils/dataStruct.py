"""
 * @file   : dataStruct.py
 * @time   : 上午8:19
 * @date   : 2024/4/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from dataclasses import dataclass
from typing import Literal

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

