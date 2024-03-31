"""
 * @file   : material.py
 * @time   : 15:17
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from abc import abstractmethod

from BasicLibrary.io.fileHelper import FileHelper

from JianYingDraft.core import template
from JianYingDraft.utils import tools
from pymediainfo import MediaInfo


class Media:
    """
    素材的基类
    """

    # +--------------------------------------------------------------------------
    # |::::TIPS::::| 本代码的实现逻辑与说明
    # ---------------------------------------------------------------------------
    # 1. 本类型的实例对应某一个加入到草稿中的媒体文件
    # 2. 本类型的属性，分为两类：素材的基础属性和业务属性
    #   2.1. 素材的基础属性，包括素材的长、宽、名称等固有信息
    #   2.2. 素材的业务属性，包括基于此素材进行的各种业务操作，比如播放速度（speed）等
    #
    # 3. 与文件draft_content内节点的对映关系
    #   3.1. 节点materials的videos（或者audio）数组中会保存media的基础属性
    #   3.2. 节点materials的speeds、sound_channel_mappings等几个数组中会保存media的业务属性
    #   3.3. 节点Tracks数组内的每个轨道，都有segments数组节点，数组的元素segment内保存media的基础属性，及其业务属性的id列表
    # 4. 与文件draft_meta_info内节点的对映关系
    #   数组draft_materials的第0和第8个元素，value数组的每个元素记录media的基础属性
    # +--------------------------------------------------------------------------

    media_material_type_mapping = {
        "audio": "music",
        "image": "photo",
    }

    media_category_type_mapping = {
        "image": "video"
    }

    def __init__(self, **kwargs):
        """
        初始化数据
        初始化数据分为两个阶段：
        1. 初始化基础属性（media本身的属性，比如width等）
        2. 初始化业务属性（media为组成草稿准备的属性，比如轨道的segment等）
        针对这2个阶段，设置4个钩子，派生类可以根据情况调用：
        1. _init_basic_info_before
        2. _init_basic_info_after
        3. _init_biz_info_before
        4. _init_biz_info_after
        :param kwargs:
        """
        # 00. 保存传递进来的kwargs，供后续灵活使用
        self.kwargs = kwargs

        # A.1. 定义基础属性
        self.id = tools.generate_id()  # 在mete_info和content中都使用同一个guid

        self.media_type = ''  # 这是媒体文件真实的类型
        self.material_type = ''  # 这是媒体添加到草稿里面，对应的素材类型（比如图片媒体文件image，对应的素材类型就是photo）
        self.category_type = ''  # 这是媒体添加到草稿里面，素材所属类目（比如图片对应的类目就是Video）

        self.width = 0
        self.height = 0
        self.duration = 0

        self.material_name = ''
        self.file_Path = ''
        self.extra_info = ''

        # A.2 初始化基础属性
        ## A.2.00. 为初始化基础属性前加载逻辑
        self._init_basic_info_before()

        ## A.2.10. 加载各种资源的文件名称等基础信息
        media_file_full_name = kwargs.get("mediaFileFullName", "")
        media_base_name_no_extension = FileHelper.get_base_name_no_extension(media_file_full_name)
        self.extra_info = media_base_name_no_extension  # media_file_full_name.split("/")[-1]
        self.material_name = media_base_name_no_extension
        self.file_Path = media_file_full_name

        ## A.2.20. 加载各种媒体公共的信息
        media_info = kwargs.get("mediaInfo")
        self._load_property_from_media(media_info)

        ## A.2.30. 加载媒体的自定义设置
        duration = kwargs.get("duration", 0)
        if duration:
            self.duration = duration
        pass

        ## A.2.99. 为初始化基础属性后加载逻辑
        self._init_basic_info_after()

        # B.1. 定义业务属性（最后暴露给草稿文件使用）

        ## B.1.10. 定义暴露给draft_meta_info文件的属性
        self.data_for_meta_info = template.get_material_for_meta_info(self.id)

        ## B.1.20. 定义暴露给draft_content文件的属性
        ## 内部有各种属性分为两组，并分别为两个组设置别名：material_for_content,track_for_content
        # 第1组. material组（speed、sound_channel_mapping等，当然最重要的是video（或者audio））
        # 这些属性最后都会最成为materials各种数组属性的元素（比如此处的speed会保存为materials.speeds数组的一个元素：
        # materials.speeds = [speed1, speed2, speed3, ...]。此处的其他各属性亦然。）
        # 第2组. track组（segments等）
        # 具体内容在派生类中实现
        self.data_for_content = {
            "material": {},
            "segment": {},
        }
        self.material_data_for_content = self.data_for_content["material"]
        self.segment_data_for_content = self.data_for_content["segment"]

        # B.2.00. 为初始化业务属性前加载逻辑
        self._init_biz_info_before()

        ## B.2.10. 设置草稿文件的meta_info部分
        self.__set_data_for_meta_info()

        ## B.2.20. 设置草稿文件的content部分
        # 此部分功能在派生类中实现
        self.__set_data_for_content()

        ## B.2.99. 为初始化业务属性后加载逻辑
        self._init_biz_info_after()

    def _init_basic_info_before(self):
        """
        在初始化基础属性前加载逻辑（供派生类使用）
        """
        _self = self

    def _init_basic_info_after(self):
        """
        在初始化基础属性后加载逻辑（供派生类使用）
        """
        _self = self

    def _init_biz_info_before(self):
        """
        在初始化业务属性前加载逻辑（供派生类使用）
        """
        _self = self

    def _init_biz_info_after(self):
        """
        在初始化业务属性后加载逻辑（供派生类使用）
        """
        _self = self

    def __set_data_for_content(self):
        """
        为草稿文件draft_content准备信息
        """
        self._set_material_data_for_content()
        self._set_segment_data_for_content()

    @abstractmethod
    def _set_material_data_for_content(self):
        """
        设置草稿文件的material部分
        """

    pass

    def _set_segment_data_for_content(self):
        """
        设置草稿文件track中的segment部分
        """
        segment = template.get_segment()
        self.segment_data_for_content = segment

        # # 将本片段应该表示的素材类型，临时记录在“X.xx”内
        # segment['X.material_type'] = self.material_type

        segment['material_id'] = self.id
        segment['extra_material_refs'] = self.material_data_for_content["X.extra_material_refs"]

        segment['source_timerange'] = {"duration": self.duration, "start": 0}  # 使用原素材的开始位置和使用时长信息（素材自己的时间）
        segment['target_timerange'] = {"duration": self.duration, "start": 0}  # 放入轨道上的开始位置和使用时长信息（轨道上的时间）

    pass

    def __set_data_for_meta_info(self):
        """
        为稿文件draft_meta_info准备信息
        """
        self.data_for_meta_info['metetype'] = self.material_type
        self.data_for_meta_info['width'] = self.width
        self.data_for_meta_info['height'] = self.height
        self.data_for_meta_info['duration'] = self.duration
        self.data_for_meta_info['extra_info'] = self.extra_info
        self.data_for_meta_info['file_Path'] = self.file_Path

    def _load_property_from_media(self, media_info: MediaInfo):
        """
        从媒体信息中加载素材信息
        """
        self.media_type = media_info['track_type'].lower()

        if self.media_type in self.media_material_type_mapping:
            self.material_type = self.media_material_type_mapping[self.media_type]
        else:
            self.material_type = self.media_type
        pass

        if self.media_type in self.media_category_type_mapping:
            self.category_type = self.media_category_type_mapping[self.media_type]
        else:
            self.category_type = self.media_type
        pass

        if "width" in media_info:
            self.width = media_info['width']
            self.height = media_info['height']
        pass

        if "duration" in media_info:
            self.duration = media_info['duration'] * 1000
        pass
