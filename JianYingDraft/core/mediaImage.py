"""
 * @file   : materialVideo.py
 * @time   : 15:23
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from core import template
from core.media import Media
from utils import tools


# TODO:xiedali@2024/03/27 功能需要实现

class MediaImage(Media):

    def _set_material_data_for_content(self):
        speed_id = tools.generate_id()
        scm_id = tools.generate_id()
        canvas_id = tools.generate_id()

        self.material_data_for_content["speeds"] = template.get_speed(speed_id)
        self.material_data_for_content["sound_channel_mappings"] = template.get_sound_channel_mapping(scm_id)
        self.material_data_for_content["canvases"] = template.get_canvas(canvas_id)

        self.material_data_for_content["videos"] = self.__gen_photo()
        # 将素材的各种业务信息，暂时保存起来，后续供track下的segment使用
        self.material_data_for_content["X.extra_material_refs"] = [speed_id, scm_id, canvas_id]

    def __gen_photo(self):
        entity = template.get_video(self.id)
        entity["duration"] = self.duration
        entity["height"] = self.height
        entity["local_material_id"] = self.id  # 暂时跟素材设置为相同的id
        entity["material_name"] = self.material_name
        entity["path"] = self.file_Path
        entity["type"] = self.material_type
        entity["width"] = self.width
        return entity
pass
