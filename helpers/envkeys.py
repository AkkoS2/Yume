import os


def saturn_key():
    return os.environ.get("SATURN_KEY", None)


def tenor_key():
    return os.environ.get("TENOR_KEY", None)


def giphy_key():
    return os.environ.get("GIPHY_KEY", None)


def deepai_key():
    return os.environ.get("DEEPAI_KEY", None)


def client_id():
    return os.environ.get("CLIENT_ID", None)


def client_secret():
    return os.environ.get("CLIENT_SECRET", None)


def user_agent():
    return os.environ.get("USER_AGENT", None)


def api_key():
    return os.environ.get("API_KEY", None)


def user_id():
    return os.environ.get("USER_ID", None)
