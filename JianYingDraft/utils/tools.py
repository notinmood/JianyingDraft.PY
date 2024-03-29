import os
import shutil
import uuid
import json

from BasicLibrary.io.dirHelper import DirHelper


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
