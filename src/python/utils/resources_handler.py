import os


def getFont(name: str = "Roboto-Regular.ttf") -> str:  # {
    localPath: str = os.path.split(os.path.split(os.path.split(__file__)[0])[0])[0]
    return os.path.join(localPath, "res", name)
# }
