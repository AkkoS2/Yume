#Bibliotecas
import os


def yume_key():
    return os.environ.get("YUME_KEY")


def app_id():
    return os.environ.get("APP_ID")


def logger_hook():
    return os.environ.get("LOGGER_HOOK")


def typo_hook():
    return os.environ.get("TYPO_HOOK")


def suggestion_hook():
    return os.environ.get("SUGGESTION_HOOK")
