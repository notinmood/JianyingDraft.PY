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
    guid: str
    name: str
    resource_id: str


@dataclass
class EffectData(ResourceData):
    """
    特效数据
    """
    pass


@dataclass
class TransitionData(ResourceData):
    """
    转场数据
    """
    duration: int


@dataclass
class AnimationData(ResourceData):
    """
    动画数据
    """
    animation_type: AnimationTypes
    start: int
    duration: int
