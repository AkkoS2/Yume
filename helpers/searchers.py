# bibliotecas
from helpers.envkeys import kawaii_red
import requests

nekos_gif = None
kawaii_gif = None


# nekos.best
def nekos_best():

    r = requests.get(f'https://nekos.best/api/v2/{nekos_gif}')

    if r.status_code == 200:

        data = r.json()
        return data['results'][0]['url']

    else:
        raise


# kawaii.red
def kawaii_api():

    r = requests.get(f'https://kawaii.red/api/gif/{kawaii_gif}/token={kawaii_red()}&filter=[]/')

    if r.status_code == 200:

        data = r.json()
        return data['response']

    else:
        raise
