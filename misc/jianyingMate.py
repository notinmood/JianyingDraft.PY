# """
#  * @file   : jianyingMate.py
#  * @time   : 10:31
#  * @date   : 2024/3/7
#  * @mail   : 9727005@qq.com
#  * @creator: ShanDong Xiedali
#  * @company: HiLand & RainyTop
# """
# import os.path
#
# from utils.tool import *
# from utils.util import *
#
#
# class JianyingMate:
#     def __init__(self, draft_name: str):
#         """
#         初始化剪映草稿生成器
#         :param draft_name:要创建草稿的文件名
#         """
#         # 模板文件的路径
#         self.template_content_path = None
#         self.template_meta_info_path = None
#
#         # 剪映草稿文件的路径
#         self.draft_content_path = None
#         self.draft_meta_info_path = None
#
#         # 剪映草稿文件内容
#         self.draft_meta_info_data = None
#         self.draft_content_data = None
#
#         # 具体某个草稿的名字
#         self.draft_name = draft_name
#         # 剪映的草稿根路径
#         self.draft_root_path = r"Z:\jianying\Data\JianyingPro Drafts"
#         # 具体某个草稿的目录
#         self.draft_fold_path = os.path.join(self.draft_root_path, self.draft_name)
#
#     def init_data(self):
#         """
#         初始化数据
#         """
#         self.template_meta_info_path, self.template_content_path = template_path()  # 返回两个模版的完整路劲
#         self.draft_content_data = read_json(self.template_content_path)  # 模版1
#         self.draft_meta_info_data = read_json(self.template_meta_info_path)  # 模版2
#
#         self.draft_content_data['id'] = generate_id()  # 给模版ID设置唯一id
#         tracks_video_data = tracks()  # 创建tracks用于存放图片信息
#         tracks_video_data['type'] = 'video'  # 类型
#         self.draft_content_data['tracks'].append(tracks_video_data)  # 添加到模板里
#
#         tracks_audio_data = tracks()  # 创建tracks用于存放音频信息
#         tracks_audio_data['type'] = 'audio'  # 类型
#         self.draft_content_data['tracks'].append(tracks_audio_data)  # 添加到模板里
#
#         self.draft_meta_info_data['draft_id'] = generate_id()  # 给模版ID设置唯一id
#         # 剪映的草稿路径 如：D:\\\\software\\\\剪映\\\\JianyingPro Drafts
#         self.draft_meta_info_data['draft_root_path'] = self.draft_root_path
#         self.draft_meta_info_data['tm_draft_create'] = int(time.time() * 1000)  # draft_meta_info.json创建时间，时间戳
#         self.draft_meta_info_data['tm_draft_modified'] = generate_16_digit_timestamp()  # 13或16位毫秒级时间戳
#         # 磁盘的驱动器 如"D:"
#         self.draft_meta_info_data['draft_removable_storage_device'] = get_drive_from_path(self.draft_root_path)
#         # 草稿目录 如： D:/software/剪映/JianyingPro Drafts/六合八荒唯我独尊
#         self.draft_meta_info_data['draft_fold_path'] = self.draft_fold_path.replace('\\', '/')
#         # 草稿名字 如："六合八荒唯我独尊"
#         self.draft_meta_info_data['draft_name'] = self.draft_name
#
#     def write_data(self):
#         """
#         创建文件,并写入数据
#         """
#         # 创建文件夹
#         os.makedirs(self.draft_fold_path, exist_ok=True)
#         # 创建 draft_meta_info.json
#         with open(self.draft_meta_info_path, 'w', encoding='utf-8') as meta_info_file:
#             json.dump(self.draft_meta_info_data, meta_info_file, indent=4, ensure_ascii=False)
#
#         with open(self.draft_content_path, 'w', encoding='utf-8') as content_file:
#             json.dump(self.draft_content_data, content_file, indent=4, ensure_ascii=False)
