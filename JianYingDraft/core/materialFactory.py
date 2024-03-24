"""
 * @file   : materialFactory.py
 * @time   : 16:10
 * @date   : 2024/3/24
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from BasicLibrary.data.stringHelper import StringHelper
from BasicLibrary.environment.dynamicImporter import DynamicImporter


class MaterialFactory:
    """
    素材工厂
    """

    @staticmethod
    def create(material_type):
        """
        根据素材来信创建素材实体
        :param material_type:
        :return:
        """
        material_type = StringHelper.upper_first_char(material_type)
        package_name = f"JianYingDraft.core.material{material_type}"
        class_name = f"Material{material_type}"

        material = DynamicImporter.load_class(package_name, class_name)
        return material
