from utils.envkeys import logger_hook
from dotenv import load_dotenv
import threading
import requests
import logging


class DiscordWHook(logging.Handler):
    def __init__(self, hook_url):
        super().__init__()
        self.hook_url = hook_url

    def emit(self, record):
        entry = self.format(record)
        payload = {"content": f"```{entry}```"}

        threading.Thread(target=self.send_log, args=(payload,), daemon=True).start()

    def send_log(self, payload):
        requests.post(self.hook_url, json=payload, timeout=1)


load_dotenv()

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)
hook_url = f"{str(logger_hook())}"
discord_handler = DiscordWHook(hook_url)
formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
discord_handler.setFormatter(formatter)

logger.addHandler(discord_handler)
