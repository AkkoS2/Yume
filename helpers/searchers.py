from helpers.envkeys import client_id, client_secret, user_agent
import redditeasy
import requests


reddit = None
gif = None


def reddit_searcher():

    post = redditeasy.Subreddit(client_id=client_id(),
                                client_secret=client_secret(),
                                user_agent=user_agent())
    outpout = post.get_post(subreddit=reddit)

    while outpout.content_type != redditeasy.ContentType.IMAGE:
        outpout = post.get_post(subreddit=reddit)

    else:
        title = outpout.title
        url = outpout.content
        posturl = outpout.post_url
        subname = outpout.subreddit_name
        print(outpout.content_type)
        return title, url, posturl, subname


def rp_search():

    r = requests.get(f'https://nekos.best/api/v2/{gif}')
    if r.status_code == 200:

        data = r.json()
        return data['results'][0]['url']
    else:
        raise
