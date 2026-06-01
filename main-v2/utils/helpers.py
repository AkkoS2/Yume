# Bibliotecas utilizadas neste arquivo
from utils.envkeys import cats_key
from bs4 import BeautifulSoup
import aiohttp
import random
import json


# Variáveis Globais
sub_reddit = None
nekos_gif = None
values = None
profile = None


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
        async with session.get(f"https://www.xe.com/currencyconverter/convert/?Amount={values[2]}&From={values[0]}&To={values[1]}") as r:
            data = await r.text()

            little_soup = BeautifulSoup(data, 'html.parser')
            texts = little_soup.find(class_="sc-423c2a5f-1 gPUWGS").get_text()
            print(texts)
            return texts


# Cats
async def kitty_finder():

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.thecatapi.com/v1/images/search?limit=10&api_key={cats_key()}") as r:
            data = await r.json()

            return data[random.randint(0, 9)]['url']


# Dogs
async def doggy_finder():

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://dog.ceo/api/breeds/image/random") as r:
            data = await r.json()

            return data['message']


# Twitter Profile Personality
async def twtpersonality():

    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://twitter.wordware.ai/{profile}") as r:
            data = await r.text()

            little_soup = BeautifulSoup(data, 'html.parser')
            texts = little_soup.find(class_="text-xl font-bold").get_text()

            icon = little_soup.find("img", class_="max-h-24 min-h-24 w-full min-w-24 max-w-24 rounded-full border border-gray-300")
            bio = little_soup.find(class_="max-w-sm text-sm").get_text()
            emojis = little_soup.find(class_="text-center text-4xl tracking-widest").get_text()
            summary = little_soup.find("p", class_="mb-2 last:mb-0").get_text()
            roast = little_soup.find(class_="p-6 pt-0 flex flex-col text-gray-700").get_text()

            formatting = (f"**Bio:**\n"
                          f"{bio}\n"
                          f"\n"
                          f"**Profile Summary:**\n"
                          f"{emojis}\n"
                          f"{summary}\n"
                          f"\n"
                          f"**AI Profile Roasting:**\n"
                          f"{roast}\n")

            return icon, texts, formatting
