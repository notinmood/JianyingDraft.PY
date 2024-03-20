from core import template
import os
from pymediainfo import MediaInfo


class Material:
    media_type_mapping = {
        "video": "video",
        "audio": "music",
        "image": "photo",
    }

    def __init__(self, file_full_name_or_text):
        self._data = template.get_material()
        self.material_type = ''
        self.track_type = ''
        self.width = 0
        self.height = 0
        self.duration = 0
        self.extra_info = ''
        self.file_Path = ''
        self.id = self._data['id']
        self.content_material = {}

        if isinstance(file_full_name_or_text, str):
            if os.path.exists(file_full_name_or_text):
                self.load_property_from_file(file_full_name_or_text)
                if self.track_type == 'video':
                    self.content_material = self.gen_video()
                elif self.track_type == 'audio':
                    self.content_material = self.gen_audio()
            else:
                self.material_type = 'text'
                self.track_type = 'text'
                self.content_material = self.gen_text()
                self.content_material['content'] = self.content_material['content'].replace('默认文本',
                                                                                            file_full_name_or_text)
        elif isinstance(file_full_name_or_text, dict):
            # 估计用不到
            self.load_material(file_full_name_or_text)
        else:
            pass  # 素材类型错误

    @property
    def data(self):
        self._data['metetype'] = self.material_type
        self._data['width'] = self.width
        self._data['height'] = self.height
        self._data['duration'] = self.duration
        self._data['extra_info'] = self.extra_info
        self._data['file_Path'] = self.file_Path
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def load_property_from_file(self, file_path, *kwargs):
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
        t = template.get_text()
        return t

    def change_color(self, color):
        """
        改变文字颜色
        :param color: 以“#”开头后跟6位的颜色值
        """
        self.content_material['text_color'] = color
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        color1 = "<color=(1.000000, 1.000000, 1.000000, 1.000000)>"
        color2 = F'<color=({round(r / 255, 6):.6f}, {round(g / 255, 6):.6f}, {round(b / 255, 6):.6f}, 1.000000)>'
        self.content_material['content'] = self.content_material['content'].replace(color1, color2)
