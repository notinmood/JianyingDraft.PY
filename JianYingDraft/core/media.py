"""
 * @file   : material.py
 * @time   : 15:17
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from abc import abstractmethod
from core import template
from utils import tools
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

    media_type_mapping = {
        "video": "video",
        "audio": "music",
        "image": "photo",
    }

    def __init__(self, **kwargs):
        """
        初始化
        :param kwargs:
        """

        # 10. 定义基础属性
        self.id = tools.generate_id()  # 在mete_info和content中都使用同一个guid
        self.material_type = ''  #
        self.track_type = ''  # TODO:xiedali@2024/03/25 material_type和track_type的区别是什么
        self.width = 0
        self.height = 0
        self.duration = 0
        self.extra_info = ''
        self.file_Path = ''

        # 20. 定义最后暴露给草稿文件的属性
        ## 20.1. 定义暴露给draft_meta_info文件的属性
        self.data_for_meta_info = template.get_material_for_meta_info(self.id)
        ## 20.2. 定义暴露给draft_content文件的属性
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

        # 30. 加载各种资源的文件名称等信息
        media_full_name = kwargs.get("media_full_name")
        self.extra_info = media_full_name.split("/")[-1]
        self.file_Path = media_full_name

        # 40. 加载各种媒体公共的信息
        media_info = kwargs.get("media_info")
        self._load_property_from_media(media_info)

        # 50. 加载素材的自定义设置
        duration = kwargs.get("duration", 0)
        if not duration:
            self.duration = duration
        pass

        # 60.1. 设置草稿文件的meta_info部分
        self.__set_data_for_meta_info()

        # 60.2. 设置草稿文件的content部分
        # 此部分功能在派生类中实现
        self.__set_data_for_content()

    pass

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
        # track = template.get_track()
        # track['type'] = self.track_type
        # self.track_data_for_content = track

        segment = template.get_segment()
        self.segment_data_for_content = segment

        # 将本片段应该表示的素材类型，临时记录在“X.xx”内
        segment['X.material_type'] = self.material_type

        segment['material_id'] = self.id
        segment['extra_material_refs'] = self.material_data_for_content["X.extra_material_refs"]

        segment['source_timerange'] = {"duration": self.duration, "start": 0}
        segment['target_timerange'] = {"duration": self.duration, "start": 0}  # TODO:xiedali@2024/03/27 什么意思

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

        self.track_type = media_info['track_type'].lower()
        self.material_type = self.media_type_mapping[self.track_type]

        if "width" in media_info:
            self.width = media_info['width']
            self.height = media_info['height']
        pass

        if "duration" in media_info:
            self.duration = media_info['duration'] * 1000
        pass

    # def gen_track(self, track_type) -> dict:
    #     _self = self
    #
    #     track = template.get_track()
    #     track['type'] = track_type
    #
    #     return track

    def gen_audio(self):
        a = template.get_audio()
        a["duration"] = self.duration
        a["local_material_id"] = self.id
        a["name"] = self.extra_info
        a["path"] = self.file_Path
        a["type"] = "extract_" + self.material_type
        return a

    def gen_text(self):
        _self = self
        t = template.get_text()
        return t

    def change_color(self, color):
        """
        改变文字颜色
        :param color: 以“#”开头后跟6位的颜色值
        """
        self.material_data_for_content['text_color'] = color
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        color1 = "<color=(1.000000, 1.000000, 1.000000, 1.000000)>"
        color2 = F'<color=({round(r / 255, 6):.6f}, {round(g / 255, 6):.6f}, {round(b / 255, 6):.6f}, 1.000000)>'
        self.material_data_for_content['content'] = self.material_data_for_content['content'].replace(color1, color2)

    # @staticmethod
    # def gen_basic_and_refs_info(material: "Media"):
    #     """
    #     生成material的基础信息和附加引用信息
    #     """
    #
    #     basic_info = {}
    #     extra_material_refs = []
    #     if material.material_type == 'video':
    #         basic_info['speeds'] = template.get_speed()
    #         basic_info['sound_channel_mappings'] = template.get_sound_channel_mapping()
    #         basic_info['canvases'] = template.get_canvas()
    #     elif material.material_type == 'photo':
    #         # TODO:xiedali@2024/03/23 需要通过在剪映内添加一个图片测试一下
    #         pass
    #     elif material.material_type == 'audio':
    #         basic_info['speeds'] = template.get_speed()
    #         basic_info['sound_channel_mappings'] = template.get_sound_channel_mapping()
    #         basic_info['beats'] = template.get_sound_channel_mapping()
    #     elif material.material_type == 'text':
    #         basic_info['material_animations'] = template.get_material_animation()
    #
    #     basic_info[f'{material.track_type}s'] = material.data_for_content
    #
    #     for key in basic_info:
    #         extra_material_refs.append(basic_info[key]['id'])
    #     pass
    #
    #     return basic_info, extra_material_refs, material.data_for_content['id']
    #
    # pass
