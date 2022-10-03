import requests

nekos_gif = None


# nekos.best
def nekos_best():

    r = requests.get(f'https://nekos.best/api/v2/{nekos_gif}')

    if r.status_code == 200:

        data = r.json()
        return data['results'][0]['url']

    else:
        raise
