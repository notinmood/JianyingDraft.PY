# import random
# import os
# # import selenium
# from core import draft
# from core import Material
#
# # 新建项目
# draft = Draft("测试草稿")
# # 选择背景音乐并添加鼓点
# audio = "D:/Music/Krubb Wenkroist - Bleach.mp3"
# draft.add_media_to_track(audio)
# # 读取鼓点
# beats = draft.content_materials['beats'][0]['user_beats']
# # 加载视频
# files= []
# for pt in os.listdir('D:/myCode/Python/spider/douyin_spider/media/video/小仙儿'):
#     file_path = os.path.join('D:/myCode/Python/spider/douyin_spider/media/video/小仙儿',pt)
#     files.append(file_path)
# # 随机裁切视频为合适时长
# end = 0
# for beat in beats:
#     duration = beat - end
#     mate = Material(files[random.randint(0,len(files)-1)])
#     start = int(random.uniform(0,(mate.duration-duration)/1000))*1000
#     Draft.add_media_to_track(mate,start,duration)
#     end = beat
# # 保存草稿
# draft.save()
