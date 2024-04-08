"""
 * @file   : materialVideo.py
 * @time   : 15:23
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from JianYingDraft.core import template
from JianYingDraft.core.media import Media
from JianYingDraft.utils import tools


class MediaAudio(Media):

    def _set_material_data_for_content(self):
        speed_id = tools.generate_id()
        scm_id = tools.generate_id()
        beat_id = tools.generate_id()

        self.material_data_for_content['speeds'] = template.get_speed(speed_id)
        self.material_data_for_content['sound_channel_mappings'] = template.get_sound_channel_mapping(scm_id)
        self.material_data_for_content['beats'] = template.get_beat(beat_id)

        self.material_data_for_content["audios"] = self.__gen_audio()
        # 将素材的各种业务信息，暂时保存起来，后续供track下的segment使用
        self.material_data_for_content["X.extra_material_refs"] = [speed_id, scm_id, beat_id]

        # 以下为音频淡入淡出的效果
        fade_in_duration = self.kwargs.get("fade_in_duration", 0)
        fade_out_duration = self.kwargs.get("fade_out_duration", 0)
        if fade_in_duration > 0 or fade_out_duration > 0:
            audio_fade_id = tools.generate_id()
            self.material_data_for_content['audio_fades'] = template.get_audio_fade(
                audio_fade_id,
                fade_in_duration,
                fade_out_duration
            )

            self.material_data_for_content["X.extra_material_refs"].append(audio_fade_id)
        pass

    def __gen_audio(self):
        entity = template.get_audio(self.id)
        entity["duration"] = self.duration
        entity["local_material_id"] = self.id
        entity["name"] = self.material_name
        entity["path"] = self.file_Path
        entity["type"] = "extract_" + self.material_type  # "extract_"??什么时候不加这个前缀
        return entity


pass
