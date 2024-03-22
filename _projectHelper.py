import os

"""
1、项目使用的时候，请将本文件复制到项目根目录下，由'__projectHelper.py' 改名为'_projectHelper.py'
2、本文件('__projectHelper.py'和'_projectHelper.py')不直接向外暴露。
3、相应的功能，请使用ProjectHelper.py内包装后的逻辑。
"""


class ProjectHelper:
    """

    """

    @staticmethod
    def get_root_physical_path():
        """
        获取项目的物理根目录
        :return:
        """
        _rootPath = os.path.dirname(os.path.abspath(__file__))
        return _rootPath
