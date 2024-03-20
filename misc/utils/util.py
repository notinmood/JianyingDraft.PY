"""
 * @file   : util.py
 * @time   : 10:33
 * @date   : 2024/3/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import json
import os.path
import uuid
from datetime import datetime

from PIL import Image
from moviepy.editor import *


def generate_16_digit_timestamp():
    # 获取当前时间的微秒级时间戳
    timestamp_micro = datetime.now().timestamp() * 1_000_000
    # 将时间戳转换为整数
    timestamp_micro_int = int(timestamp_micro)
    # 确保时间戳是16位的，这可能需要根据你的具体需求调整
    return str(timestamp_micro_int)[:16]


pass


def get_drive_from_path(path: str):
    """
    获取路径的盘符
    :param path:
    :return:
    """
    return os.path.splitdrive(path)[0]


pass


def generate_id():
    """
    生成uuid(大写)
    """
    return str(uuid.uuid4()).upper()


def read_json(path):
    """
    加载模板JSON
    """
    try:
        with open(path, 'r', encoding="utf-8") as template_meta_info_file:
            info_data = json.load(template_meta_info_file)
            return info_data
    except Exception as e:
        print(f"Error: {e}")
        return None


def process_image(file_path):
    """
    获取图片信息
    """
    try:
        # 提取文件名
        file_name = os.path.basename(file_path)

        # 打开图片文件
        with Image.open(file_path) as img:
            # 获取图片的宽度和高度
            width, height = img.size
            # 宽度、高度、完整路径和文件名
            image_info = {
                'file_path': file_path,
                'file_name': file_name,
                'width': width,
                'height': height
            }
            return image_info
    except Exception as e:
        # 处理可能的异常，比如无法打开文件或不是有效的图片文件
        print(f"Error processing file {file_path}: {e}")
        return None


def process_images_in_folder(folder_path):
    """
    返回图片信息以及完整路劲
    """
    image_info_array = []

    # 遍历文件夹中的文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件扩展名，确保它是图片文件
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tif')):
                # 获取图片文件的完整路径
                image_path = os.path.join(root, file).replace('\\', '/')

                # 处理图片文件
                image_info = process_image(image_path)

                # 将image_info添加到数组中
                if image_info:
                    image_info_array.append(image_info)

    return image_info_array


def template_path():
    """
    :return: 模板草稿的完整路劲
    """
    # 获取当前文件所在目录的路径
    current_folder_path = os.path.dirname(os.path.abspath(__file__))

    # 获取当前文件所在目录的父目录的路径
    parent_folder_path = os.path.dirname(current_folder_path)

    # 构建 template 文件夹的路径
    template_folder_path = os.path.join(parent_folder_path, 'template')

    # 构建 draft_meta_info.json 文件的完整路径
    template_meta_info_path = os.path.join(template_folder_path, 'draft_meta_info.json')
    template_content_path = os.path.join(template_folder_path, 'draft_content.json')

    return template_meta_info_path, template_content_path


def process_audio(file_path):
    """
    获取音频信息
    """
    try:
        # 提取文件名
        file_name = os.path.basename(file_path)

        # 读取音频文件
        clip = AudioFileClip(file_path)

        # 获取音频时长
        audio_duration = int(clip.duration * 1_000_000) + 3333  # 这里是转成剪映的

        audio_info = {
            'file_path': file_path,
            'file_name': file_name,
            'duration': audio_duration,
            'filetype': 'audio'
        }

        return audio_info
    except Exception as e:
        # 处理可能的异常，比如无法打开文件或不是有效的音频文件
        print(f"处理文件 {file_path} 时出错：{e}")
        return None


def process_audios_in_folder(folder_path):
    """
    返回音频信息以及完整路劲
    """
    audio_info_array = []

    # 遍历文件夹中的文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件扩展名，确保它是音频文件
            if file.lower().endswith(('.wav', '.mp3', '.ogg', '.aac', '.m4a')):
                # 获取音频文件的完整路径
                audio_path = os.path.join(root, file).replace('\\', '/')

                # 处理音频文件
                audio_info = process_audio(audio_path)

                # 将audio_info添加到数组中
                if audio_info:
                    audio_info_array.append(audio_info)

    return audio_info_array
