from core import template


class Tracks:
    """
    轨道信息
    """

    def __init__(self) -> None:
        """
        初始化轨道类型
        """

        self.video_track = []
        self.audio_track = []
        self.text_track = []

    def add_video_track(self, track_index=0):
        """
        添加一条视频轨道
        当track_index超过现有轨道数时，则新建轨道，否则为选取轨道
        Args:
            track_index (int, optional): 第几条轨道. Defaults to 0.

        Returns:
            dict: 返回轨道字典
        """
        track = self._add_track(self.video_track, 'video', track_index)
        if track:
            self.video_track.append(track)
        return self.video_track[track_index]

    def add_audio_track(self, track_index=0):
        track = self._add_track(self.audio_track, 'audio', track_index)
        if track:
            # 当视频轨道为空时
            if len(self.video_track) == 0:
                self.add_video_track()
            self.audio_track.append(track)
        return self.audio_track[track_index]

    def add_text_track(self, track_index=0):
        track = self._add_track(self.text_track, 'text', track_index)
        if track:
            # 当视频轨道为空时
            if len(self.video_track) == 0:
                self.add_video_track()
            self.text_track.append(track)
        return self.text_track[track_index]

    def _add_track(self, tracks, track_type, track_index):
        track_len = len(tracks)
        if track_index == track_len:
            track = template.track()
            track['type'] = track_type
            if track_len:
                track['flag'] = 2
            return track
        else:
            return False

    def to_track(self, metetype, segment, track_index):
        if metetype == "video":
            self.video_track[track_index]['segments'].append(segment)
        elif metetype == "music":
            self.audio_track[track_index]['segments'].append(segment)
        elif metetype == "text":
            self.text_track[track_index]['segments'].append(segment)

    def _composite(self):
        """
        将所有轨道合成为一个列表
        """
        track = []
        track.extend(self.video_track)
        track.extend(self.text_track)
        track.extend(self.audio_track)
        return track
