# bibliotecas
from helpers.envkeys import tenor_key, giphy_key
from discord.ext import commands
from helpers import searchers
import requests
import discord


# inicializa o cog
class Image(commands.Cog):
    def __init__(self, saturn):
        self.saturn = saturn

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Image is Ready!')

    # tenor
    @commands.command(aliases=['gif1'])
    async def tenor(self, ctx, *, message):

        api_key = tenor_key()
        lmt = 50
        request = message

        r = requests.get('https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s' % (request, api_key, lmt))
        if r.status_code == 200:

            data = r.json()
            if len(data['results']) < 1:
                await ctx.reply('Não achei nada com esse nome :c', mention_author=False)
                return

            tenor_embed = discord.Embed(color=discord.Colour.random())
            url = data['results'][0]['media'][0]['gif']['url']
            tenor_embed.set_image(url=url)

            send = await ctx.send(embed=tenor_embed)
            emojis = '⬅', '🆗', '➡'

            for i in range(len(emojis)):
                await send.add_reaction(emoji=emojis[i])

        else:
            await ctx.reply('Parece que deu algum problema com a API, desculpa :c', mention_author=False)

    # giphy
    @commands.command(aliases=['gif2'])
    async def giphy(self, ctx, *, message):

        api_key = giphy_key()
        request = message
        lmt = 50

        r = requests.get('https://api.giphy.com/v1/gifs/search?api_key=%s&q=%s&limit=%s&offset=0&rating=g&lang=en' %
                         (api_key, request, lmt))
        if r.status_code == 200:

            data = r.json()
            if len(data['data']) < 1:
                await ctx.reply('Não achei nada com esse nome :c', mention_author=False)
                return

            giphy_embed = discord.Embed(color=discord.Colour.random())
            url = data['data'][1]['images']['original']['url']
            giphy_embed.set_image(url=url)

            send = await ctx.send(embed=giphy_embed)
            emojis = '⬅', '🆗', '➡'

            for i in range(len(emojis)):
                await send.add_reaction(emoji=emojis[i])
        else:
            await ctx.reply('Parece que deu algum problema com a API, desculpa :c', mention_author=False)

    # r/memeframe
    @commands.command()
    async def memeframe(self, ctx):

        searchers.reddit = 'memeframe'
        result = searchers.reddit_searcher()

        frame = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        frame.set_author(name=f'r/{result[3]}', url=str(result[2]))
        frame.set_image(url=str(result[1]))
        await ctx.send(embed=frame)

    # r/softwaregore
    @commands.command()
    async def softwaregore(self, ctx):

        searchers.reddit = 'softwaregore'
        result = searchers.reddit_searcher()

        software = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        software.set_author(name=f'r/{result[3]}', url=str(result[2]))
        software.set_image(url=str(result[1]))
        await ctx.send(embed=software)

    # r/cosplay
    @commands.command()
    async def cosplay(self, ctx):

        searchers.reddit = 'cosplay'
        result = searchers.reddit_searcher()

        cosplays = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        cosplays.set_author(name=f'r/{result[3]}', url=str(result[2]))
        cosplays.set_image(url=str(result[1]))
        await ctx.send(embed=cosplays)

    # r/memes
    @commands.command()
    async def memes(self, ctx):

        searchers.reddit = 'memes'
        result = searchers.reddit_searcher()

        meme = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        meme.set_author(name=f'r/{result[3]}', url=str(result[2]))
        meme.set_image(url=str(result[1]))
        await ctx.send(embed=meme)

    # r/unixsocks
    @commands.command(aliases=['unix'])
    async def unixsocks(self, ctx):

        searchers.reddit = 'unixsocks'
        result = searchers.reddit_searcher()

        unix = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        unix.set_author(name=f'r/{result[3]}', url=str(result[2]))
        unix.set_image(url=str(result[1]))
        await ctx.send(embed=unix)

    # r/formuladank
    @commands.command(aliases=['fdank'])
    async def formuladank(self, ctx):

        searchers.reddit = 'formuladank'
        result = searchers.reddit_searcher()

        dank = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        dank.set_author(name=f'r/{result[3]}', url=str(result[2]))
        dank.set_image(url=str(result[1]))
        await ctx.send(embed=dank)

    # r/wholesomeanimemes
    @commands.command()
    async def wholesomeanimemes(self, ctx):

        searchers.reddit = 'wholesomeanimemes'
        result = searchers.reddit_searcher()

        wholesome = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        wholesome.set_author(name=f'r/{result[3]}', url=str(result[2]))
        wholesome.set_image(url=str(result[1]))
        await ctx.send(embed=wholesome)

    # r/anime_irl
    @commands.command(aliases=['animeirl'])
    async def anime_irl(self, ctx):

        searchers.reddit = 'anime_irl'
        result = searchers.reddit_searcher()

        anirl = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        anirl.set_author(name=f'r/{result[3]}', url=str(result[2]))
        anirl.set_image(url=str(result[1]))
        await ctx.send(embed=anirl)

    # r/mechanicalkeyboards
    @commands.command(aliases=['keyboards'])
    async def mechanicalkeyboards(self, ctx):

        searchers.reddit = 'mechanicalkeyboards'
        result = searchers.reddit_searcher()

        mkeys = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        mkeys.set_author(name=f'r/{result[3]}', url=str(result[2]))
        mkeys.set_image(url=str(result[1]))
        await ctx.send(embed=mkeys)

    # r/Animemes
    @commands.command(aliases=['animeme'])
    async def animemes(self, ctx):

        searchers.reddit = 'Animemes'
        result = searchers.reddit_searcher()

        animeme = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        animeme.set_author(name=f'r/{result[3]}', url=str(result[2]))
        animeme.set_image(url=str(result[1]))
        await ctx.send(embed=animeme)

    # r/goodanimemes
    @commands.command()
    async def goodanimemes(self, ctx):

        searchers.reddit = 'goodanimemes'
        result = searchers.reddit_searcher()

        goodanimeme = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        goodanimeme.set_author(name=f'r/{result[3]}', url=str(result[2]))
        goodanimeme.set_image(url=str(result[1]))
        await ctx.send(embed=goodanimeme)

    # r/programminghorror
    @commands.command()
    async def programminghorror(self, ctx):

        searchers.reddit = 'programminghorror'
        result = searchers.reddit_searcher()

        proghorror = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        proghorror.set_author(name=f'r/{result[3]}', url=str(result[2]))
        proghorror.set_image(url=str(result[1]))
        await ctx.send(embed=proghorror)

    # r/badcode
    @commands.command()
    async def badcode(self, ctx):

        searchers.reddit = 'badcode'
        result = searchers.reddit_searcher()

        badcodes = discord.Embed(description=f'**{str(result[0])}**', color=discord.Colour.random())
        badcodes.set_author(name=f'r/{result[3]}', url=str(result[2]))
        badcodes.set_image(url=str(result[1]))
        await ctx.send(embed=badcodes)


# registra a classe no cogs
def setup(saturn):
    saturn.add_cog(Image(saturn))
