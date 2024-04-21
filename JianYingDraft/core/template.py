"""
 * @file   : materialVideo.py
 * @time   : 15:23
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import time
from JianYingDraft.utils import tools


def get_canvas(guid: str = None):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "album_image": "",
        "blur": 0.0,
        "color": "",
        "id": guid,
        "image": "",
        "image_id": "",
        "image_name": "",
        "source_platform": 0,
        "team_id": "",
        "type": "canvas_color"
    }


def get_sound_channel_mapping(guid: str = None):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "audio_channel_mapping": 0,
        "id": guid,
        "is_config_open": False,
        "type": "none"
    }


def get_speed(guid: str = None):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "curve_speed": None,
        "id": guid,
        "mode": 0,
        "speed": 1.0,
        "type": "speed"
    }


def get_material_for_meta_info(guid: str = None):
    """
    获取素材信息
    :param guid: 素材id
    :return:
    """
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "create_time": int(time.time()),
        "duration": 0,
        "extra_info": "",
        "file_Path": "",
        "height": 0,
        "id": guid,
        "import_time": int(time.time()),
        "import_time_ms": int(time.time()) * 10 ^ 6,
        "md5": "",
        "metetype": "",  # meta or mate?? 估计剪映开发人员最初拼写错误，以后大家就以讹传讹将错就错了。
        "roughcut_time_range": {"duration": 0, "start": 0},
        "sub_time_range": {"duration": -1, "start": -1},
        "type": 0,
        "width": 0
    }


def get_track(guid: str = None, track_type: str = ""):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "attribute": 0,  # 0表示正常；1表示关闭本轨道
        "flag": 0,
        "id": guid,
        "segments": [],
        "type": track_type
    }


def get_segment(guid: str = None):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "cartoon": False,
        "clip": {
            "alpha": 1.0,
            "flip": {"horizontal": False, "vertical": False},
            "rotation": 0.0,
            "scale": {"x": 1.0, "y": 1.0},
            "transform": {"x": 0.0, "y": 0.0}
        },
        "common_keyframes": [],
        "enable_adjust": True,
        "enable_color_curves": True,
        "enable_color_wheels": True,
        "enable_lut": True,
        "enable_smart_color_adjust": False,
        "extra_material_refs": [
        ],
        "group_id": "",
        "hdr_settings": {"intensity": 1.0, "mode": 1, "nits": 1000},
        "id": guid,
        "intensifies_audio": False,
        "is_placeholder": False,
        "is_tone_modify": False,
        "keyframe_refs": [],
        "last_nonzero_volume": 1.0,
        "material_id": "",
        "render_index": 0,
        "reverse": False,
        "source_timerange": {"duration": 0, "start": 0},
        "speed": 1.0,
        "target_timerange": {"duration": 0, "start": 0},
        "template_id": "",
        "template_scene": "default",
        "track_attribute": 0,
        "track_render_index": 0,
        "visible": True,
        "volume": 1.0
    }


def get_beat(guid: str = None):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "ai_beats": {
            "beats_path": "",
            "beats_url": "",
            "melody_path": "",
            "melody_percents": [0.0],
            "melody_url": ""
        },
        "enable_ai_beats": False,
        "gear": 404,
        "id": guid,
        "mode": 404,
        "type": "beats",
        "user_beats": [],
        "user_delete_ai_beats": None
    }


def get_video(guid: str = None):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "audio_fade": None,
        "cartoon_path": "",
        "category_id": "",
        "category_name": "local",
        "check_flag": 63487,
        "crop": {
            "lower_left_x": 0.0,
            "lower_left_y": 1.0,
            "lower_right_x": 1.0,
            "lower_right_y": 1.0,
            "upper_left_x": 0.0,
            "upper_left_y": 0.0,
            "upper_right_x": 1.0,
            "upper_right_y": 0.0
        },
        "crop_ratio": "free",
        "crop_scale": 1.0,
        "duration": 0,
        "extra_type_option": 0,  # 是否播放视频素材的本身的背景音。0：播放；1：不播放
        "formula_id": "",
        "freeze": None,
        "gameplay": None,
        "has_audio": True,
        "height": 0,
        "id": guid,
        "intensifies_audio_path": "",
        "intensifies_path": "",
        "is_unified_beauty_mode": False,
        "local_id": "",
        "local_material_id": "",
        "material_id": "",
        "material_name": "",
        "material_url": "",
        "matting": {
            "flag": 0,
            "has_use_quick_brush": False,
            "has_use_quick_eraser": False,
            "interactiveTime": [],
            "path": "",
            "strokes": []
        },
        "media_path": "",
        "object_locked": None,
        "path": "",
        "picture_from": "none",
        "picture_set_category_id": "",
        "picture_set_category_name": "",
        "request_id": "",
        "reverse_intensifies_path": "",
        "reverse_path": "",
        "source_platform": 0,
        "stable": None,
        "team_id": "",
        "type": "",
        "video_algorithm": {
            "algorithms": [],
            "deflicker": None,
            "motion_blur_config": None,
            "noise_reduction": None,
            "path": "",
            "time_range": None
        },
        "width": 0
    }


def get_audio(guid: str = None):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "app_id": 0,
        "category_id": "",
        "category_name": "local",
        "check_flag": 1,
        "duration": 0,
        "effect_id": "",
        "formula_id": "",
        "id": guid,
        "intensifies_path": "",
        "local_material_id": "",
        "music_id": tools.generate_id(),
        "name": "Krubb Wenkroist - Bleach.mp3",
        "path": "D:/Music/Krubb Wenkroist - Bleach.mp3",
        "request_id": "",
        "resource_id": "",
        "source_platform": 0,
        "team_id": "",
        "text_id": "",
        "tone_category_id": "",
        "tone_category_name": "",
        "tone_effect_id": "",
        "tone_effect_name": "",
        "tone_speaker": "",
        "tone_type": "",
        "type": "extract_music",
        "video_id": "",
        "wave_points": []
    }


def get_text(guid: str = None):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "add_type": 0,
        "alignment": 1,
        "background_alpha": 1.0,
        "background_color": "",
        "background_height": 1.0,
        "background_horizontal_offset": 0.0,
        "background_round_radius": 0.0,
        "background_style": 0,
        "background_vertical_offset": 0.0,
        "background_width": 1.0,
        "bold_width": 0.0,
        "border_color": "",
        "border_width": 0.08,
        "check_flag": 7,
        "content": "<font id=\"\" path=\"E:/JianyingPro/4.2.0.10100/Resources/Font/SystemFont/zh-hans.ttf\"><color=(1.000000, 1.000000, 1.000000, 1.000000)><size=15.000000>[默认文本]</size></color></font>",
        "font_category_id": "",
        "font_category_name": "",
        "font_id": "",
        "font_name": "",
        "font_path": "E:/JianyingPro/4.2.0.10100/Resources/Font/SystemFont/zh-hans.ttf",
        "font_resource_id": "",
        "font_size": 15.0,
        "font_source_platform": 0,
        "font_team_id": "",
        "font_title": "none",
        "font_url": "",
        "fonts": [],
        "force_apply_line_max_width": False,
        "global_alpha": 1.0,
        "group_id": "",
        "has_shadow": False,
        "id": guid,
        "initial_scale": 1.0,
        "is_rich_text": False,
        "italic_degree": 0,
        "ktv_color": "",
        "language": "",
        "layer_weight": 1,
        "letter_spacing": 0.0,
        "line_spacing": 0.02,
        "name": "",
        "preset_category": "",
        "preset_category_id": "",
        "preset_has_set_alignment": False,
        "preset_id": "",
        "preset_index": 0,
        "preset_name": "",
        "recognize_type": 0,
        "relevance_segment": [],
        "shadow_alpha": 0.8,
        "shadow_angle": -45.0,
        "shadow_color": "",
        "shadow_distance": 8.0,
        "shadow_point": {"x": 1.0182337649086284, "y": -1.0182337649086284},
        "shadow_smoothing": 1.0,
        "shape_clip_x": False,
        "shape_clip_y": False,
        "style_name": "",
        "sub_type": 0,
        "text_alpha": 1.0,
        "text_color": "#FFFFFF",
        "text_preset_resource_id": "",
        "text_size": 30,
        "text_to_audio_ids": [],
        "tts_auto_update": False,
        "type": "text",
        "typesetting": 0,
        "underline": False,
        "underline_offset": 0.22,
        "underline_width": 0.05,
        "use_effect_default_color": True,
        "words": []
    }


def get_material_animation(guid: str = None):
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "animations": [],
        "id": guid,
        "type": "sticker_animation"
    }


def get_detail_animation(resource_id: str = "", name="", animation_type: str = "in", start: int = 0,
                         duration: int = 0, ):
    return {
        "resource_id": resource_id,
        "type": animation_type,
        "category_id": animation_type,
        "category_name": animation_type,
        "start": start,
        "duration": duration,
        "id": tools.generate_id(),  # 不会被其他地方引用，所以赋值一个随机id
        "material_type": "video",
        "name": name,
        "panel": "video",
        "path": "",
        "platform": "all",
        "request_id": "",
        "anim_adjust_params": ""
    }


def get_audio_fade(guid: str = None, fade_in_duration: int = 0, fade_out_duration: int = 0):
    """
    添加音频的淡入淡出效果
    @param guid:
    @param fade_in_duration: 淡入时间（单位微秒）
    @param fade_out_duration: 淡出时间（单位微秒）
    @return:
    """
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "fade_in_duration": fade_in_duration,
        "fade_out_duration": fade_out_duration,
        "fade_type": 0,
        "id": guid,
        "type": "audio_fade"
    }


def get_video_effect(guid: str = None, resource_id: str = "", name=""):
    """
    添加视频特效

    @param guid: 特效的资源id
    @param name: 特效的名称
    @param resource_id: 特效资源在剪映的资源库中的id（非常重要，剪映通过这个id来自动获取特效的各种资源）
    @return:
    """
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "adjust_params": [
            {
                "default_value": 0.33,
                "name": "effects_adjust_speed",
                "value": 0.33
            },
            {
                "default_value": 1.0,
                "name": "effects_adjust_background_animation",
                "value": 1.0
            }
        ],
        "algorithm_artifact_path": "",
        "apply_target_type": 2,
        "apply_time_range": {"duration": 0, "start": 0},
        "category_id": "1039448",
        "category_name": "热门",
        "common_keyframes": [],
        "disable_effect_faces": [],
        "effect_id": "1039448",
        "formula_id": "",
        "id": guid,
        "name": name,
        "path": "",
        "platform": "all",
        "render_index": 0,
        "request_id": "",
        "resource_id": resource_id,  # 特效的资源id（剪映通过这个id来自动获取特效的各种资源）
        "source_platform": 0,
        "time_range": {"duration": 0, "start": 0},
        "track_render_index": 0,
        "type": "video_effect",
        "value": 1.0,
        "version": ""
    }


def get_transition(guid: str = None, resource_id: str = "", name="", duration: int = 500_000):
    """
    添加视频特效

    @param duration: 转场的持续时间（单位微秒）
    @param guid: 转场的资源id
    @param name: 转场的名称
    @param resource_id: 转场资源在剪映的资源库中的id（非常重要，剪映通过这个id来自动获取转场的各种资源）
    @return:
    """
    if guid is None:
        guid = tools.generate_id()
    pass

    return {
        "category_id": "39862",
        "category_name": "叠化",
        "duration": duration,
        "effect_id": "321493",
        "id": guid,
        "is_overlap": False,
        "name": name,
        "path": "",
        "platform": "all",
        "request_id": "202404100726237F33ED27AE329CF48C4E",
        "resource_id": resource_id,
        "type": "transition"
    }
