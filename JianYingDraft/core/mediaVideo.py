"""
 * @file   : materialVideo.py
 * @time   : 15:23
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from JianYingDraft.core.media import Media
from core import template
from utils import tools


class MediaVideo(Media):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.track_type = "video"
        self.material_type = "video"
        # self.data_for_content = self.gen_video()

    pass

    def _set_material_data_for_content(self):
        """
        设置草稿文件的content部分
        """
        speed_id = tools.generate_id()
        scm_id = tools.generate_id()
        canvas_id = tools.generate_id()

        self.material_data_for_content["speeds"] = template.get_speed(speed_id)
        self.material_data_for_content["sound_channel_mappings"] = template.get_sound_channel_mapping(scm_id)
        self.material_data_for_content["canvases"] = template.get_canvas(canvas_id)

        self.material_data_for_content["video"] = self.gen_video()
        # 将素材的各种业务信息，暂时保存起来，后续供track下的segment使用
        self.material_data_for_content["X.extra_material_refs"] = [speed_id, scm_id, canvas_id]

    def gen_video(self):
        v = template.get_video(self.id)
        v["duration"] = self.duration
        v["height"] = self.height
        v["local_material_id"] = self.id  # 暂时跟素材的id设置为相同
        v["material_name"] = self.extra_info
        v["path"] = self.file_Path
        v["type"] = self.material_type
        v["width"] = self.width
        return v

    # def apply_to_content(self, materials_of_content: {}):
    #     """
    #     将媒体信息应用到drft_content的materials节点内
    #     :param materials_of_content: 文件drft_content的materials节点
    #     """
    #     ...
    #
    # pass


pass
