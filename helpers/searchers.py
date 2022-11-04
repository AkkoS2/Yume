# bibliotecas
from helpers.envkeys import kawaii_red, tenor_key
import requests
import aiohttp
import random

nekos_gif = None
kawaii_gif = None
tenor_gif = None
sub_reddit = None


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


# tenor
def tenor():

    api_key = tenor_key()
    lmt = 50
    request = tenor_gif

    r = requests.get('https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s' % (request, api_key, lmt))
    if r.status_code == 200:

        data = r.json()
        if len(data['results']) < 1:
            raise

        return data['results'][random.randint(0, 50)]['media'][0]['gif']['url']

    else:
        raise


# reddit search
async def reddit_search():
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://reddit.com/r/{sub_reddit}.json") as r:
            data = await r.json()

        if data['data']['children'][random.randint(0, 25)]['data']['over_18'] is True:

            return "that's lewd"

        return "That's safe!"
        # print(data['data']['children'][random.randint(0, 25)]['data']['url'])
