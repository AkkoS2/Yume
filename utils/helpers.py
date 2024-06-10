# Bibliotecas utilizadas neste arquivo
import aiohttp
import random
import json


# Variáveis Globais
sub_reddit = None


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
