from JianYingDraft.core import template
import os
from pymediainfo import MediaInfo


class MaterialMate:
    media_type_mapping = {
        "video": "video",
        "audio": "music",
        "image": "photo",
    }

    def __init__(self, file_full_name_or_text):
        self.data_for_meta_info = template.get_material_for_meta_info()
        self.data_for_content = {}
        self.material_type = ''
        self.track_type = ''
        self.width = 0
        self.height = 0
        self.duration = 0
        self.extra_info = ''
        self.file_Path = ''
        self.id = self.data_for_meta_info['id']

        if isinstance(file_full_name_or_text, str):
            if os.path.exists(file_full_name_or_text):
                self.load_property_from_file(file_full_name_or_text)
                if self.track_type == 'video':
                    self.data_for_content = self.gen_video()
                elif self.track_type == 'audio':
                    self.data_for_content = self.gen_audio()
            else:
                self.material_type = 'text'
                self.track_type = 'text'
                self.data_for_content = self.gen_text()
                self.data_for_content['content'] = self.data_for_content['content'].replace('默认文本',
                                                                                            file_full_name_or_text)
        elif isinstance(file_full_name_or_text, dict):
            # 估计用不到
            self.load_material(file_full_name_or_text)
        else:
            pass  # 素材类型错误

        self._set_data_for_meta_info()

    # def get_data_for_content(self):
    #     return self.data_in_content

    def _set_data_for_meta_info(self):
        self.data_for_meta_info['metetype'] = self.material_type
        self.data_for_meta_info['width'] = self.width
        self.data_for_meta_info['height'] = self.height
        self.data_for_meta_info['duration'] = self.duration
        self.data_for_meta_info['extra_info'] = self.extra_info
        self.data_for_meta_info['file_Path'] = self.file_Path
        # return self.data_in_meta_info

    # @data_for_meta_info.setter
    # def data_for_meta_info(self, value):
    #     self._data_in_meta_info = value

    def load_property_from_file(self, file_path, **kwargs):
        """
        通过文件的方式去加载为素材
        """
        media_info = MediaInfo.parse(file_path).to_data()["tracks"][1]

        self.track_type = media_info['track_type'].lower()
        self.material_type = self.media_type_mapping[self.track_type]

        if "width" in media_info:
            self.width = media_info['width']
            self.height = media_info['height']
        pass

        if "duration" in media_info:
            self.duration = media_info['duration'] * 1000
        else:
            self.duration = kwargs.get("duration", 5000)
        pass

        self.extra_info = file_path.split("/")[-1]
        self.file_Path = file_path

    def load_material(self, material):
        """
        将剪映的素材加载为素材类
        """
        self.material_type = material['metetype']
        self.width = material['width']
        self.height = material['height']
        self.duration = material['duration']
        self.extra_info = material['extra_info']
        self.file_Path = material['file_Path']
        self.id = material['id']

    def gen_video(self):
        v = template.get_video()
        v["duration"] = self.duration
        v["height"] = self.height
        v["local_material_id"] = self.id
        v["material_name"] = self.extra_info
        v["path"] = self.file_Path
        v["type"] = self.material_type
        v["width"] = self.width
        return v

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
        self.data_for_content['text_color'] = color
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        color1 = "<color=(1.000000, 1.000000, 1.000000, 1.000000)>"
        color2 = F'<color=({round(r / 255, 6):.6f}, {round(g / 255, 6):.6f}, {round(b / 255, 6):.6f}, 1.000000)>'
        self.data_for_content['content'] = self.data_for_content['content'].replace(color1, color2)

    @staticmethod
    def gen_basic_and_refs_info(material: "MaterialMate"):
        """
        生成material的基础信息和附加引用信息
        """

        basic_info = {}
        extra_material_refs = []
        if material.material_type == 'video':
            basic_info['speeds'] = template.get_speed()
            basic_info['sound_channel_mappings'] = template.get_sound_channel_mapping()
            basic_info['canvases'] = template.get_canvas()
        elif material.material_type == 'photo':
            # TODO:xiedali@2024/03/23 需要通过在剪映内添加一个图片测试一下
            pass
        elif material.material_type == 'audio':
            basic_info['speeds'] = template.get_speed()
            basic_info['sound_channel_mappings'] = template.get_sound_channel_mapping()
            basic_info['beats'] = template.get_sound_channel_mapping()
        elif material.material_type == 'text':
            basic_info['material_animations'] = template.get_material_animation()

        basic_info[f'{material.track_type}s'] = material.data_for_content

        for key in basic_info:
            extra_material_refs.append(basic_info[key]['id'])
        pass

        return basic_info, extra_material_refs, material.data_for_content['id']

    pass
