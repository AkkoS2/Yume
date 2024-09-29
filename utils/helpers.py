# Bibliotecas utilizadas neste arquivo
from utils.envkeys import dogs_key, cats_key
from bs4 import BeautifulSoup
import aiohttp
import random
import json


# Variáveis Globais
sub_reddit = None
nekos_gif = None
values = None
dogcat = None


# Reddit Search
async def reddit_search():

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://reddit.com/r/{sub_reddit}.json") as r:
            data = await r.json()

        is_safe = True
        is_video = False
        choice = random.randint(0, 25)
        base_path = data['data']['children'][choice]['data']

        title = base_path['title']
        post_link = base_path['permalink']
        author = base_path['author']

        if base_path['over_18'] is True:
            is_safe = False

        if base_path['is_video'] is True:

            img_url = base_path['media']['reddit_video']['fallback_url']
            is_video = True

            return img_url, is_safe, is_video, title, post_link, author

        if 'is_gallery' in base_path:

            pic_id = base_path['gallery_data']['items'][0]['media_id']
            img_type = base_path['media_metadata'][pic_id]['m']
            extension = '.' + img_type[-3:]
            img_url = f"https://i.redd.it/{pic_id}" + extension

            return img_url, is_safe, is_video, title, post_link, author

        else:
            img_url = base_path['url']
            return img_url, is_safe, is_video, title, post_link, author


# Nekos.best
async def nekos_best():

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://nekos.best/api/v2/{nekos_gif}") as r:
            data = await r.json()

        return data['results'][0]['url']


# Currency Finder
async def currency_finder():

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://x-rates.com/calculator/?from={values[0]}&to={values[1]}&amount={values[2]}") as r:
            data = await r.text()

            little_soup = BeautifulSoup(data, 'html.parser')
            value = little_soup.find("span", class_="ccOutputRslt").get_text()

            return value[:-7]


# Cats and Dogs
async def catdog():

    if dogcat == "thedogapi":
        key = dogs_key()
    else:
        key = cats_key()

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.{dogcat}.com/v1/images/search?limit=10&api_key={key}") as r:
            data = await r.json()

            return data[random.randint(0, 9)]['url']
