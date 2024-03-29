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
    draft = Draft()
    image1_full_name = r"Z:\mm1\2023_10_01_12_34_06_想知道学霸们疯狂摘抄的诗句有哪些_3.jpg"
    image2_full_name = r"Z:\mm1\2023_10_01_12_34_06_想知道学霸们疯狂摘抄的诗句有哪些_2.jpg"

    draft.add_media(image1_full_name, duration=5_000_000)
    draft.add_media(image2_full_name, duration=3_000_000)

    music_full_name = r"Z:\mm1\似是故人来.mp3"
    draft.add_media(music_full_name)

    draft.save()


pass

if __name__ == '__main__':
    make_images()
