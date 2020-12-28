from os import path


class PathFinder:
    @staticmethod
    def assets():
        return path.dirname(path.realpath(__file__)) + "/../../assets"

    @staticmethod
    def audio(name):
        return PathFinder.assets() + f'/audio/{name}'

    @staticmethod
    def sprite(name):
        return PathFinder.assets() + f'/sprites/{name}'
