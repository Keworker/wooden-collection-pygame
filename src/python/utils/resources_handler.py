import os


def getFont(name: str = "Roboto-Regular.ttf") -> str:  # {
    """
    Returns path to font file (by default 'Roboto-Regular' font).
    :param name: Name of font
    :return: Path to the `.ttf` file
    """
    localPath: str = os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]
    return os.path.join(localPath, "res", name)
# }
