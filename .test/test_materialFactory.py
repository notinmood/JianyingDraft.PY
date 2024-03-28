from JianYingDraft.core.mediaFactory import MediaFactory
from JianYingDraft.core.mediaVideo import MediaVideo
from JianYingDraft.core.mediaAudio import MediaAudio
from JianYingDraft.core.mediaImage import MediaPhoto


def test_create():
    actual = MediaFactory.create("video")
    assert isinstance(actual, MediaVideo)

    actual = MediaFactory.create("audio")
    assert isinstance(actual, MediaAudio)

    actual = MediaFactory.create("photo")
    assert isinstance(actual, MediaPhoto)


pass
