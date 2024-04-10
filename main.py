import os.path

from BasicLibrary.projectHelper import ProjectHelper

from draftContext import DraftContext
from JianYingDraft.core.draft import Draft
from JianYingDraft.utils.dataStruct import TransitionData
from JianYingDraft.utils import tools


def basic_using():
    """
    最简使用方式
    @return:
    """
    # 0. 可以给草稿指定名字，比如Draft("古诗词欣赏")；如果不指定名字的话，默认是根据时间戳自动生成草稿名字
    draft = Draft()
    root_path = ProjectHelper.get_root_physical_path()
    middle_path = ".res"

    # 1. 添加两幅图片，分别设置不同的播放时间
    image1_full_name = os.path.join(root_path, middle_path, "古诗1.jpg")
    image2_full_name = os.path.join(root_path, middle_path, "古诗2.jpg")

    draft.add_media(image1_full_name)  # 图片如果不指定duration，默认播放5秒
    draft.add_media(image2_full_name, duration=4_000_000)  # 指定图片播放时长为4秒

    # 2. 添加背景音乐，音频长度会根据视频的长度自动剪截
    music_full_name = os.path.join(root_path, middle_path, "似是故人来.mp3")
    ## 2.1. 最简方式:直接添加音频文件的地址即可。
    # draft.add_media(music_full_name)
    ## 2.2. 也可以给音频指定淡入淡出时长
    draft.add_media(music_full_name, fade_in_duration=1_000_000, fade_out_duration=1_500_000)

    draft.save()


def make_videos():
    with DraftContext() as context:
        video1_full_name = os.path.join(context.res_path, "日报摘抄1.mov")
        video2_full_name = os.path.join(context.res_path, "日报摘抄2.mov")

        context.draft.add_media(video1_full_name)  # 视频如果不指定duration，默认全时长播放
        context.draft.add_media(video2_full_name, duration=4_000_000, bgm_mute=True)  # 指定视频播放时长为4秒，静音播放
    pass


def make_images_with_effect():
    with DraftContext() as context:
        # 1. 添加两幅图片
        image1_full_name = os.path.join(context.res_path, "古诗1.jpg")
        image2_full_name = os.path.join(context.res_path, "古诗2.jpg")

        context.draft.add_media(image1_full_name)
        context.draft.add_media(image2_full_name)

        # 2. 添加特效
        effect_name = "烟花"  # 可以使用内置特效的名称（各种内置特效请参考文档innerBizTypes.py内）；也可以使用剪映本身的特效资源id（请使用int类型为id提供值）
        context.draft.add_effect(effect_name, start=2_000_000, duration=5_000_000)

    pass


def make_images_with_transition():
    with (DraftContext() as context):
        # 1. 添加两幅图片
        image1_full_name = os.path.join(context.res_path, "古诗1.jpg")
        image2_full_name = os.path.join(context.res_path, "古诗2.jpg")

        # 2. 添加转场
        transition_data: TransitionData = tools.generate_transition_data(
            name_or_resource_id="翻页",  # 转场名称（可以是内置的转场名称，也可以是剪映本身的转场资源id）
            duration=700_000,  # 转场持续时间
        )

        context.draft.add_media(image1_full_name, transition_data=transition_data)
        # 如果是最后一张图片（或者视频），即便设置了转场，在剪映软件中也不会显示出任何效果
        context.draft.add_media(image2_full_name, transition_data=transition_data)

    pass


if __name__ == '__main__':
    ## 1. 最简方式（将图片做成视频）
    # basic_using()

    ## 2. 将既有视频进一步处理为新视频
    # make_videos()

    ## 3. 新建带有特效的图片素材
    # make_images_with_effect()

    ## 4. 新建带有转场的图片素材
    make_images_with_transition()
