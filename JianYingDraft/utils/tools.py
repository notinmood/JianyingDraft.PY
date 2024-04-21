import os
import shutil
import uuid
import json

from BasicLibrary.io.dirHelper import DirHelper

from JianYingDraft.utils.innerBizTypes import *
from JianYingDraft.utils.dataStruct import TransitionData, EffectData, AnimationData, AnimationTypes


def generate_id() -> str:
    """
    生成uuid
    """
    return str(uuid.uuid4()).upper()


def read_json(path):
    """
    读取json文件
    :param path: 文件路径
    """
    with open(path, 'r') as file:
        return json.load(file)
    pass


def write_json(path, data):
    """
    写入json文件
    :param path: 文件路径
    :param data: 数据
    """
    with open(path, 'w') as file:
        # 给json.dump添加参数 ensure_ascii=false可以保证汉字不被编码
        json.dump(data, file)
    pass


def create_folder(folder_path):
    """
    创建文件夹
    :param folder_path: 文件夹路径
    """
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    pass

    DirHelper.ensure_exist(folder_path)


def generate_effect_data(name_or_resource_id: str | int) -> EffectData:
    """
    生成转场数据
    :param name_or_resource_id: 动画名称或资源id
    """
    resource_id = "7012933493663470088"  # 缺省的特效资源ID表示小花花特效
    name = "小花花"

    if isinstance(name_or_resource_id, str):
        name = name_or_resource_id

        if name in effectDict:
            resource_id = effectDict[name]
        pass
    elif isinstance(name_or_resource_id, int):
        resource_id = str(name_or_resource_id)
        name = resource_id
    pass

    return EffectData(
        guid=generate_id(),
        resource_id=resource_id,
        name=name
    )


def generate_transition_data(name_or_resource_id: str | int, duration=0) -> TransitionData:
    """
    生成转场数据
    :param name_or_resource_id: 动画名称或资源id
    :param duration: 持续时间
    """
    resource_id = "6724239388189921806"  # 缺省的转场资源ID表示闪黑
    name = "闪黑"
    if isinstance(name_or_resource_id, str):
        name = name_or_resource_id

        if name in transitionDict:
            resource_id = transitionDict[name]
        pass
    elif isinstance(name_or_resource_id, int):
        resource_id = str(name_or_resource_id)
        name = resource_id
    pass

    return TransitionData(
        guid=generate_id(),
        resource_id=resource_id,
        duration=duration,
        name=name
    )


def generate_animation_data(name_or_resource_id: str | int, animation_type: AnimationTypes = "in", start=0,
                            duration=0) -> AnimationData:
    """
    生成动画数据
    :param animation_type: 动画类型 in/out/group
    :param name_or_resource_id: 动画名称或资源id
    :param start:
    :param duration: 持续时间
    """
    resource_id = ""  # 缺省的动画资源ID
    name = ""
    if isinstance(name_or_resource_id, str):
        name = name_or_resource_id

        if animation_type == "in" and name in animationInDict:
            resource_id = animationInDict[name]
        pass

        if animation_type == "out" and name in animationOutDict:
            resource_id = animationOutDict[name]
        pass

        if animation_type == "group" and name in animationGroupDict:
            resource_id = animationGroupDict[name]
        pass
    elif isinstance(name_or_resource_id, int):
        resource_id = str(name_or_resource_id)
        name = resource_id
    pass

    return AnimationData(
        guid=generate_id(),
        resource_id=resource_id,
        duration=duration,
        animation_type=animation_type,
        start=start,
        name=name
    )
