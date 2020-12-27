import os


class PathFinder:
    @staticmethod
    def assets():
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return dir_path + "/../../assets"

    @staticmethod
    def audio(name):
        return PathFinder.assets() + f'/audio/{name}'

    @staticmethod
    def sprite(name):
        return PathFinder.assets() + f'/sprites/{name}'
