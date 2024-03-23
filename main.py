from JianYingDraft.core.draft import Draft

if __name__ == '__main__':
    # # 新建项目
    # draft = Draft("草稿")
    # text = Material('Hello World')
    # text.change_color('#ABCABC')
    # draft.add_media_to_track(text, duration=3_000_000)
    # draft.save()

    draft = Draft()

    video_full_name = r"Z:\mm\my-video.mov"
    draft.add_material(video_full_name, duration=3_000_000)

    video_full_name = r"Z:\mm\人民日报金句摘抄｜20240215｜关于.mov"
    draft.add_material(video_full_name, start=3_000_000, duration=3_000_000)

    draft.save()

    # draft = Draft("图片草稿")
    # video_full_name = r"Z:\mm\image1.jpg"
    # material = Material(video_full_name)
    # draft.add_media_to_track(material, duration=5_000_000)
    # draft.save()
