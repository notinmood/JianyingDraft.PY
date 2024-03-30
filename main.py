import os.path

from BasicLibrary.projectHelper import ProjectHelper

from JianYingDraft.core.draft import Draft


def make_videos():
    draft = Draft()

    video_full_name = r"Z:\mm\my-video.mov"
    draft.add_media(video_full_name, duration=3_000_000)

    video_full_name = r"Z:\mm\人民日报金句摘抄｜20240215｜关于.mov"
    draft.add_media(video_full_name, start=3_000_000, duration=3_000_000)

    draft.save()


pass


def make_text():
    # # 新建项目
    # draft = Draft("草稿")
    # text = Material('Hello World')
    # text.change_color('#ABCABC')
    # draft.add_media_to_track(text, duration=3_000_000)
    # draft.save()
    ...


def make_images():
    draft = Draft("古诗词欣赏")
    root_path = ProjectHelper.get_root_physical_path()
    middle_path = ".res"

    # 1. 添加两幅图片，分别设置不同的播放时间
    image1_full_name = os.path.join(root_path, middle_path, "古诗1.jpg")
    image2_full_name = os.path.join(root_path, middle_path, "古诗2.jpg")
    draft.add_media(image1_full_name, duration=5_000_000)
    draft.add_media(image2_full_name, duration=3_000_000)

    # 2. 添加背景音乐，音乐长度会根据视频的长度自动剪截
    music_full_name = os.path.join(root_path, middle_path, "似是故人来.mp3")
    draft.add_media(music_full_name)

    draft.save()


pass

if __name__ == '__main__':
    make_images()
