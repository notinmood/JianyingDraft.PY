import os.path

from BasicLibrary.projectHelper import ProjectHelper

from JianYingDraft.core.mediaFactory import MediaFactory
from JianYingDraft.core.mediaVideo import MediaVideo
from JianYingDraft.core.mediaAudio import MediaAudio
from JianYingDraft.core.mediaImage import MediaImage


def test_create():
    root_path = ProjectHelper.get_root_physical_path()
    my_resource = os.path.join(root_path, ".test/_res/my-video.mov")
    actual = MediaFactory.create(my_resource)
    assert isinstance(actual, MediaVideo)

    my_resource = os.path.join(root_path, ".test/_res/my-audio.mp3")
    actual = MediaFactory.create(my_resource)
    assert isinstance(actual, MediaAudio)

    my_resource = os.path.join(root_path, ".test/_res/my-picture.png")
    actual = MediaFactory.create(my_resource)
    assert isinstance(actual, MediaImage)


pass
