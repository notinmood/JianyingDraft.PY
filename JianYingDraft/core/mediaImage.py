"""
 * @file   : materialVideo.py
 * @time   : 15:23
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.configHelper import ConfigHelper

from JianYingDraft.core import template
from JianYingDraft.core.mediaVideo import MediaVideo
from JianYingDraft.utils import tools


# TODO:xiedali@2024/03/27 功能需要实现

class MediaImage(MediaVideo):

    def _init_basic_info_after(self):
        """
        在初始化基础属性后加载逻辑（供派生类使用）
        """
        # duration = self.kwargs.get("duration", 0)
        if self.duration == 0:
            duration = ConfigHelper.get_item("JianYingDraft.image", "default_duration", 5000000)
            self.duration = duration
        pass

    def __generate_main_data(self):
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
