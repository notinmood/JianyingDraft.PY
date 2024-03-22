"""
 * @file   : tool.py
 * @time   : 10:29
 * @date   : 2024/3/7
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
import time

from util import *


def tracks():
    return {
        "attribute": 0,
        "flag": 0,
        "id": generate_id(),
        "is_default_name": True,
        "name": "",
        "segments": [],
        "type": ""
    }


def segment_video():
    return {
        "cartoon": False,
        "clip": {
            "alpha": 1.0,
            "flip": {
                "horizontal": False,
                "vertical": False
            },
            "rotation": 0.0,
            "scale": {
                "x": 1.0,
                "y": 1.0
            },
            "transform": {
                "x": 0.0,
                "y": 0.0
            }
        },
        "common_keyframes": [],
        "enable_adjust": True,
        "enable_color_curves": True,
        "enable_color_match_adjust": False,
        "enable_color_wheels": True,
        "enable_lut": True,
        "enable_smart_color_adjust": False,
        "extra_material_refs": [],
        "group_id": "",
        "hdr_settings": {
            "intensity": 1.0,
            "mode": 1,
            "nits": 1000
        },
        "id": generate_id(),
        "intensifies_audio": False,
        "is_placeholder": False,
        "is_tone_modify": False,
        "keyframe_refs": [],
        "last_nonzero_volume": 1.0,
        "material_id": "",
        "render_index": 0,
        "responsive_layout": {
            "enable": False,
            "horizontal_pos_layout": 0,
            "size_layout": 0,
            "target_follow": "",
            "vertical_pos_layout": 0
        },
        "reverse": False,
        "source_timerange": {
            "duration": 5000000,
            "start": 0
        },
        "speed": 1.0,
        "target_timerange": {
            "duration": 5000000,
            "start": 0
        },
        "template_id": "",
        "template_scene": "default",
        "track_attribute": 0,
        "track_render_index": 0,
        "uniform_scale": {
            "on": True,
            "value": 1.0
        },
        "visible": True,
        "volume": 1.0
    }


def segment_audio():
    return {
        "cartoon": False,
        "clip": None,
        "common_keyframes": [],
        "enable_adjust": False,
        "enable_color_curves": True,
        "enable_color_match_adjust": False,
        "enable_color_wheels": True,
        "enable_lut": False,
        "enable_smart_color_adjust": False,
        "extra_material_refs": [],
        "group_id": "",
        "hdr_settings": None,
        "id": generate_id(),
        "intensifies_audio": False,
        "is_placeholder": False,
        "is_tone_modify": False,
        "keyframe_refs": [],
        "last_nonzero_volume": 1.0,
        "material_id": "",
        "render_index": 0,
        "responsive_layout": {
            "enable": False,
            "horizontal_pos_layout": 0,
            "size_layout": 0,
            "target_follow": "",
            "vertical_pos_layout": 0
        },
        "reverse": False,
        "source_timerange": {
            "duration": 0,
            "start": 0
        },
        "speed": 1.0,
        "target_timerange": {
            "duration": 0,
            "start": 0
        },
        "template_id": "",
        "template_scene": "default",
        "track_attribute": 0,
        "track_render_index": 0,
        "uniform_scale": None,
        "visible": True,
        "volume": 1.0
    }


def vocal():
    return {
        "choice": 0,
        "id": "",
        "production_path": "",
        "time_range": None,
        "type": "vocal_separation"
    }


def videos_items():
    return {
        "aigc_type": "none",
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
        "duration": 10800000000,
        "extra_type_option": 0,
        "formula_id": "",
        "freeze": None,
        "gameplay": None,
        "has_audio": False,
        "height": 0,
        "id": "",
        "intensifies_audio_path": "",
        "intensifies_path": "",
        "is_ai_generate_content": False,
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
        "origin_material_id": "",
        "path": "",
        "picture_from": "none",
        "picture_set_category_id": "",
        "picture_set_category_name": "",
        "request_id": "",
        "reverse_intensifies_path": "",
        "reverse_path": "",
        "smart_motion": None,
        "source": 0,
        "source_platform": 0,
        "stable": {
            "matrix_path": "",
            "stable_level": 0,
            "time_range": {
                "duration": 0,
                "start": 0
            }
        },
        "team_id": "",
        "type": "photo",
        "video_algorithm": {
            "algorithms": [],
            "deflicker": None,
            "motion_blur_config": None,
            "noise_reduction": None,
            "path": "",
            "quality_enhance": None,
            "time_range": None
        },
        "width": 0
    }


def speeds_items():
    return {
        "curve_speed": None,
        "id": "",
        "mode": 0,
        "speed": 1.0,
        "type": "speed"
    }


def sound_items():
    return {
        "audio_channel_mapping": 0,
        "id": "",
        "is_config_open": False,
        "type": ""
    }


def canvases_items():
    return {
        "album_image": "",
        "blur": 0.0,
        "color": "",
        "id": "",
        "image": "",
        "image_id": "",
        "image_name": "",
        "source_platform": 0,
        "team_id": "",
        "type": "canvas_color"
    }


def beats_items():
    return {
        "ai_beats": {
            "beat_speed_infos": [],
            "beats_path": "",
            "beats_url": "",
            "melody_path": "",
            "melody_percents": [
                0.0
            ],
            "melody_url": ""
        },
        "enable_ai_beats": False,
        "gear": 404,
        "gear_count": 0,
        "id": "",
        "mode": 404,
        "type": "beats",
        "user_beats": [],
        "user_delete_ai_beats": None
    }


def audios():
    return {
        "app_id": 0,
        "category_id": "",
        "category_name": "local",
        "check_flag": 1,
        "duration": 0,
        "effect_id": "",
        "formula_id": "",
        "id": "",
        "intensifies_path": "",
        "local_material_id": generate_id(),
        "music_id": generate_id(),
        "name": "",
        "path": "",
        "query": "",
        "request_id": "",
        "resource_id": "",
        "search_id": "",
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


def draft_materials_items():
    return {
        "create_time": int(time.time()),
        "duration": 0,
        "extra_info": "",
        "file_Path": "",
        "height": 0,
        "id": generate_id(),
        "import_time": int(time.time()),
        "import_time_ms": int(time.time()) * 10 ** 3,
        "item_source": 1,
        "md5": "",
        "metetype": "0",
        "roughcut_time_range": {
            "duration": -1,
            "start": -1
        },
        "sub_time_range": {
            "duration": -1,
            "start": -1
        },
        "type": 0,
        "width": 0
    }


def material_animations_items():
    return {
        "animations": [],
        "id": "",
        "type": "sticker_animation"
    }
