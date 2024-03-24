from JianYingDraft.core.materialFactory import MaterialFactory
from JianYingDraft.core.materialVideo import MaterialVideo
from JianYingDraft.core.materialAudio import MaterialAudio
from JianYingDraft.core.materialPhoto import MaterialPhoto


def test_create():
    actual = MaterialFactory.create("video")
    assert isinstance(actual, MaterialVideo)

    actual = MaterialFactory.create("audio")
    assert isinstance(actual, MaterialAudio)

    actual = MaterialFactory.create("photo")
    assert isinstance(actual, MaterialPhoto)


pass
