# bibliotecas
from helpers.envkeys import kawaii_red, tenor_key, spotify_id, spotify_secret, genius_key
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import aiohttp
import spotipy
import random
import json

nekos_gif = None
kawaii_gif = None
tenor_gif = None
sub_reddit = None
spotify = None
ytube = None
lyrics = None
vocals = None


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

        is_safe = True
        video = False
        choice = random.randint(0, 25)

        title = data['data']['children'][choice]['data']['title']
        post_link = data['data']['children'][choice]['data']['permalink']
        author = data['data']['children'][choice]['data']['author']

        if data['data']['children'][choice]['data']['over_18'] is True:
            is_safe = False

        if data['data']['children'][choice]['data']['is_video'] is True:

            img_url = data['data']['children'][choice]['data']['media']['reddit_video']['fallback_url']
            video = True
            return img_url, is_safe, video, title, post_link, author

        if 'is_gallery' in data['data']['children'][choice]['data']:

            pic_id = data['data']['children'][choice]['data']['gallery_data']['items'][0]['media_id']
            img_type = data['data']['children'][choice]['data']['media_metadata'][pic_id]['m']
            extension = '.' + img_type[-3:]
            img_url = f"https://i.redd.it/{pic_id}" + extension
            return img_url, is_safe, video, title, post_link, author

        else:
            img_url = data['data']['children'][choice]['data']['url']
            return img_url, is_safe, video, title, post_link, author


def spotify_search():

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=spotify_id(), client_secret=spotify_secret()))

    result = sp.search(q=str(spotify), limit=1)
    fixing = json.dumps(result)
    data = json.loads(fixing)

    artist = data['tracks']['items'][0]['artists'][0]['external_urls']['spotify']
    album = data['tracks']['items'][0]['album']['external_urls']['spotify']
    song = data['tracks']['items'][0]['external_urls']['spotify']

    return artist, album, song
