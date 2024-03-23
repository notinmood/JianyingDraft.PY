from JianyingDraft.core import template


class Tracks:
    """
    轨道信息
    """

    def __init__(self):
        """
        初始化轨道类型
        """
        self.video_track = []
        self.audio_track = []
        self.text_track = []

    def add_video_track(self, track_index=0) -> dict:
        """
        添加一条视频轨道
        当track_index超过现有轨道数时，则新建轨道，否则为选取轨道
        Args:
            track_index (int, optional): 第几条轨道. Defaults to 0.

        Returns:
            dict: 返回轨道字典
        """
        track = self.gen_track(self.video_track, 'video', track_index)

        if track:
            self.video_track.append(track)
        pass

        return self.video_track[track_index]

    def add_audio_track(self, track_index=0) -> dict:
        track = self.gen_track(self.audio_track, 'audio', track_index)
        if track:
            # 当视频轨道为空时
            if len(self.video_track) == 0:
                self.add_video_track()
            pass

            self.audio_track.append(track)
        pass

        return self.audio_track[track_index]

    def add_text_track(self, track_index=0):
        track = self.gen_track(self.text_track, 'text', track_index)
        if track:
            # 当视频轨道为空时
            if len(self.video_track) == 0:
                self.add_video_track()
            pass

            self.text_track.append(track)
        pass

        return self.text_track[track_index]

    def add_segment(self, material_type, segment, track_index):
        target_track = None
        if material_type == "video":
            target_track = self.video_track[track_index]
        elif material_type == "music":
            target_track = self.audio_track[track_index]
        elif material_type == "text":
            target_track = self.text_track[track_index]
        pass

        target_track['segments'].append(segment)

    def composite(self):
        """
        将所有轨道合成为一个列表
        """
        tracks = []
        tracks.extend(self.video_track)
        tracks.extend(self.text_track)
        tracks.extend(self.audio_track)

        return tracks

    def gen_track(self, tracks, track_type, track_index) -> dict:
        _self = self

        track_len = len(tracks)
        if track_index == track_len:
            track = template.get_track()
            track['type'] = track_type
            if track_len:
                track['flag'] = 2
            pass

            return track
        else:
            return False
        pass
