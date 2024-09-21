import os


def yume_key():
    return os.environ.get("YUME_KEY")


def app_id():
    return os.environ.get("APP_ID")


def loghook():
    return os.environ.get("LOGHOOK")


def typohook():
    return os.environ.get("TYPOHOOK")


def sugghook():
    return os.environ.get("SUGGHOOK")


def ideahook():
    return os.environ.get("IDEAHOOK")
