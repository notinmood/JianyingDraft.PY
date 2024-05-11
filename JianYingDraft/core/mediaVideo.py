"""
 * @file   : materialVideo.py
 * @time   : 15:23
 * @date   : 2024/3/23
 * @mail   : 9727005@qq.com
 * @creator: ShanDong Xiedali
 * @company: HiLand & RainyTop
"""
from JianYingDraft.core.media import Media
from JianYingDraft.core import template
from JianYingDraft.utils import tools
from JianYingDraft.utils.dataStruct import TransitionData, AnimationData


class MediaVideo(Media):

    def _set_material_data_for_content(self):
        """
        设置草稿文件的content部分
        """
        speed_id = tools.generate_id()
        scm_id = tools.generate_id()
        canvas_id = tools.generate_id()

        self.material_data_for_content["sound_channel_mappings"] = template.get_sound_channel_mapping(scm_id)
        self.material_data_for_content["canvases"] = template.get_canvas(canvas_id)

        speed_data = template.get_speed(speed_id)
        speed = self.kwargs.get("speed", 1.0)
        speed_data["speed"] = speed
        self.material_data_for_content["speeds"] = speed_data
        video_data = self.__generate_main_data()

        # 判定是否要对视频素材本身的背景音进行静音处理
        bgm_mute = self.kwargs.get("bgm_mute", False)
        if bgm_mute:
            video_data["extra_type_option"] = 1
        else:
            video_data["extra_type_option"] = 0
        pass

        self.material_data_for_content["videos"] = video_data

        # 将素材的各种业务信息，暂时保存起来，后续供track下的segment使用
        self.material_data_for_content["X.extra_material_refs"] = [speed_id, scm_id, canvas_id]

        # 处理转场效果
        transition_data: TransitionData | None = self.kwargs.get("transition_data", None)
        if transition_data:
            transition_guid = tools.generate_id()
            transition_data.guid = transition_guid
            self.material_data_for_content["transitions"] = template.get_transition(
                transition_data.guid,
                transition_data.resource_id,
                transition_data.name,
                transition_data.duration
            )
            self.material_data_for_content["X.extra_material_refs"].append(transition_guid)
        pass

        # 处理视频动画
        animation_datas: list[AnimationData] | None = self.kwargs.get("animation_datas", None)
        if animation_datas:
            animation_guid = tools.generate_id()
            material_animations = template.get_material_animation(animation_guid)

            for animation_data in animation_datas:

                animation_start = animation_data.start
                # 如果是入场动画，则动画的起始时间为0
                if animation_data.animation_type == "in":
                    animation_start = 0
                pass

                # 如果是出场动画，则动画的起始时间为素材的持续时间向前推动画时长duration
                if animation_data.animation_type == "out":
                    animation_start = self.duration - animation_data.duration
                pass

                animation_entity = template.get_detail_animation(
                    animation_data.resource_id,
                    animation_data.name,
                    animation_data.animation_type,
                    animation_start,
                    animation_data.duration,
                )

                material_animations["animations"].append(animation_entity)
            pass

            self.material_data_for_content["material_animations"] = material_animations
            self.material_data_for_content["X.extra_material_refs"].append(animation_guid)

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
