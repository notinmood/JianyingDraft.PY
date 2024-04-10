"""
 * @file   : dataStruct.py
 * @time   : 上午8:19
 * @date   : 2024/4/10
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from dataclasses import dataclass


@dataclass
class ResourceData:
    guid: str
    name: str
    resource_id: str


@dataclass
class EffectData(ResourceData):
    pass


@dataclass
class TransitionData(ResourceData):
    duration: int
