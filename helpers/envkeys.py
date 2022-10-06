import os


def yume_key():
    return os.environ.get("YUME_KEY", None)


def deepai_key():
    return os.environ.get("DEEPAI_KEY", None)


def app_id():
    return os.environ.get("APP_ID", None)


def kawaii_red():
    return os.environ.get("KAWAII_RED", None)
