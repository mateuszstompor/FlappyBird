from os import path


class PathFinder:
    """
    Eases retrieving paths for the assets bundled with the game
    """
    @staticmethod
    def assets() -> str:
        return path.dirname(path.realpath(__file__)) + "/../../assets"

    @staticmethod
    def audio(name: str) -> str:
        return PathFinder.assets() + f'/audio/{name}'

    @staticmethod
    def sprite(name: str) -> str:
        return PathFinder.assets() + f'/sprites/{name}'
