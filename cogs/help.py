# bibliotecas
from discord.ext import commands
import discord


# inicializa o cog
class Help(commands.Cog):
    def __init__(self, saturn):
        self.saturn = saturn

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help is Ready!')

    # help
    @commands.command(aliases=['ajuda'])
    async def help(self, ctx, *, category: str = None):

        file01 = discord.File('media/Saturn01.png', filename='Saturn01.png')
        file02 = discord.File('media/Saturn02.png', filename='Saturn02.png')

        if category is None:

            help_main = discord.Embed(description=f'```Utilize <prefixo> <categoria> para ver os comandos disponíveis '
                                                  f'em cada categoria (ex: s!help utility)```', color=discord.Colour.random())
            help_main.set_author(name='Saturn helps you!', icon_url='attachment://Saturn02.png')
            help_main.add_field(name='🔮 Features', value='11 comandos.', inline=True)
            help_main.add_field(name='🎉 Fun', value='20 comandos.', inline=True)
            help_main.add_field(name='🖼️ Image', value='22 comandos.', inline=True)
            help_main.add_field(name='🛡️ Moderation', value='16 comandos.', inline=True)
            help_main.add_field(name='🎧 Music', value='12 comandos.', inline=True)
            help_main.add_field(name='🔞 NSFW', value='20 comandos.', inline=True)
            help_main.add_field(name='🎭 Roleplay', value='44 comandos.', inline=True)
            help_main.add_field(name='🔎 Search', value='17 comandos', inline=True)
            help_main.add_field(name='🛠️ Utility', value='17 comandos.', inline=True)
            help_main.add_field(name='🧮 Math', value='14 comandos.', inline=True)
            help_main.add_field(name='🎲 Gambling', value='TBD', inline=True)
            help_main.add_field(name='🏦 Economy', value='TBD', inline=True)
            help_main.set_footer(text='Concluído: 42/193* (21%).')

            await ctx.send(file=file02, embed=help_main)

        elif category.lower() == 'features':

            features = discord.Embed(description='```Features```', color=discord.Colour.random())
            features.set_author(name='Features', icon_url='attachment://Saturn01.png')
            features.add_field(name='Reddit Search', value='01', inline=False)
            features.add_field(name='Custom Prefix', value='02', inline=False)
            features.add_field(name='Help Command', value='03', inline=False)
            features.add_field(name='DM Command List', value='04', inline=False)
            features.add_field(name='Server Language', value='05', inline=False)
            features.add_field(name='Support', value='06', inline=False)
            features.add_field(name='Command Categories', value='07', inline=False)
            features.add_field(name='Disable Command', value='08', inline=False)
            features.add_field(name='Enable Command', value='09', inline=False)
            features.add_field(name='Join Message', value='10', inline=False)
            features.add_field(name='Leave Message', value='11', inline=False)
            features.set_footer(text='Features')

            await ctx.send(file=file01, embed=features)

        elif category.lower() == 'fun':

            fun = discord.Embed(description='```Fun```', color=discord.Colour.random())
            fun.set_author(name='Fun', icon_url='attachment://Saturn01.png')
            fun.add_field(name='Fortune Teller', value='0', inline=False)
            fun.add_field(name='Like', value='0', inline=False)
            fun.add_field(name='Quiz', value='0', inline=False)
            fun.add_field(name='Question', value='0', inline=False)
            fun.add_field(name='Rickroll', value='0', inline=False)
            fun.add_field(name='Random ASCII', value='0', inline=False)
            fun.add_field(name='Chaos Emerald', value='0', inline=False)
            fun.add_field(name='Vay Hek', value='0', inline=False)
            fun.add_field(name='Emoji ASCII', value='0', inline=False)
            fun.add_field(name='Text ASCII', value='0', inline=False)
            fun.add_field(name='SoonTM', value='0', inline=False)
            fun.add_field(name='Roll', value='0', inline=False)
            fun.add_field(name='Luck', value='0', inline=False)
            fun.add_field(name='Joke', value='0', inline=False)
            fun.add_field(name='Coin', value='0', inline=False)
            fun.add_field(name='Uwuify', value='0', inline=False)
            fun.add_field(name='Fortune Cookie', value='0', inline=False)
            fun.add_field(name='Jankenpon', value='0', inline=False)
            fun.add_field(name='Rate', value='0', inline=False)
            fun.add_field(name='Time to Duel', value='0', inline=False)
            fun.set_footer(text='Fun')

            await ctx.send(file=file01, embed=fun)

        elif category.lower() == 'image':

            image = discord.Embed(description='```Image```', color=discord.Colour.random())
            image.set_author(name='Image', icon_url='attachment://Saturn01.png')
            image.add_field(name='r/softwaregore', value='0', inline=False)
            image.add_field(name='r/memeframe', value='0', inline=False)
            image.add_field(name='r/cosplay', value='0', inline=False)
            image.add_field(name='r/memes', value='0', inline=False)
            image.add_field(name='r/unixsocks', value='0', inline=False)
            image.add_field(name='r/formuladank', value='0', inline=False)
            image.add_field(name='r/wholesomeanimemes', value='0', inline=False)
            image.add_field(name='r/anime_irl', value='0', inline=False)
            image.add_field(name='r/mechanicalkeyboards', value='0', inline=False)
            image.add_field(name='r/animemes', value='0', inline=False)
            image.add_field(name='r/goodanimemes', value='0', inline=False)
            image.add_field(name='r/programminghorror', value='0', inline=False)
            image.add_field(name='r/badcode', value='0', inline=False)
            image.add_field(name='Tenor', value='0', inline=False)
            image.add_field(name='Giphy', value='0', inline=False)
            image.add_field(name='Cat Images', value='0', inline=False)
            image.add_field(name='Dog Images', value='0', inline=False)
            image.add_field(name='Catgirl Images', value='0', inline=False)
            image.add_field(name='Catboy Images', value='0', inline=False)
            image.add_field(name='Random Reddit Images', value='0', inline=False)
            image.add_field(name='Imgur', value='0', inline=False)
            image.add_field(name='Tumblr', value='0', inline=False)
            image.set_footer(text='Image')

            await ctx.send(file=file01, embed=image)

        elif category.lower() == 'moderation':

            moderation = discord.Embed(description='```Moderation```', color=discord.Colour.random())
            moderation.set_author(name='Moderation', icon_url='attachment://Saturn01.png')
            moderation.add_field(name='Clear', value='0', inline=False)
            moderation.add_field(name='Clone', value='0', inline=False)
            moderation.add_field(name='Nuke', value='0', inline=False)
            moderation.add_field(name='Delete Voice', value='0', inline=False)
            moderation.add_field(name='Create Voice', value='0', inline=False)
            moderation.add_field(name='Delete Text', value='0', inline=False)
            moderation.add_field(name='Create Text', value='0', inline=False)
            moderation.add_field(name='Delete Category', value='0', inline=False)
            moderation.add_field(name='Create Category', value='0', inline=False)
            moderation.add_field(name='Staff Log', value='0', inline=False)
            moderation.add_field(name='Message Log', value='0', inline=False)
            moderation.add_field(name='Softban', value='0', inline=False)
            moderation.add_field(name='Ban', value='0', inline=False)
            moderation.add_field(name='Kick', value='0', inline=False)
            moderation.add_field(name='Timeout', value='0', inline=False)
            moderation.add_field(name='Warn', value='0', inline=False)
            moderation.set_footer(text='Moderation')

            await ctx.send(file=file01, embed=moderation)

        elif category.lower() == 'music':

            music = discord.Embed(description='```Music```', color=discord.Colour.random())
            music.set_author(name='Music', icon_url='attachment://Saturn01.png')
            music.add_field(name='Join', value='0', inline=False)
            music.add_field(name='Leave', value='0', inline=False)
            music.add_field(name='Play', value='0', inline=False)
            music.add_field(name='Now Playing', value='0', inline=False)
            music.add_field(name='Pause', value='0', inline=False)
            music.add_field(name='Stop', value='0', inline=False)
            music.add_field(name='Skip', value='0', inline=False)
            music.add_field(name='Repeat', value='0', inline=False)
            music.add_field(name='Queue', value='0', inline=False)
            music.add_field(name='Shuffle Queue', value='0', inline=False)
            music.add_field(name='Queue Repeat', value='0', inline=False)
            music.add_field(name='Reset', value='0', inline=False)
            music.set_footer(text='Music')

            await ctx.send(file=file01, embed=music)

        elif category.lower() == 'nsfw':

            nsfw = discord.Embed(description='```NSFW```', color=discord.Colour.random())
            nsfw.set_author(name='NSFW', icon_url='attachment://Saturn01.png')
            nsfw.add_field(name='Yande.re', value='0', inline=False)
            nsfw.add_field(name='Rule34', value='0', inline=False)
            nsfw.add_field(name='r/Paizuri', value='0', inline=False)
            nsfw.add_field(name='r/Hentai', value='0', inline=False)
            nsfw.add_field(name='r/Ecchi', value='0', inline=False)
            nsfw.add_field(name='r/HQHentai', value='0', inline=False)
            nsfw.add_field(name='r/AlmostHentai', value='0', inline=False)
            nsfw.add_field(name='r/UncensoredHentai', value='0', inline=False)
            nsfw.add_field(name='r/SubwayHentai', value='0', inline=False)
            nsfw.add_field(name='r/TrapHentai', value='0', inline=False)
            nsfw.add_field(name='r/ThighDeology', value='0', inline=False)
            nsfw.add_field(name='r/HentaiWorldInfo', value='0', inline=False)
            nsfw.add_field(name='r/Hentai_Gif', value='0', inline=False)
            nsfw.add_field(name='r/ElegantR34', value='0', inline=False)
            nsfw.add_field(name='Safebooru', value='0', inline=False)
            nsfw.add_field(name='Gelbooru', value='0', inline=False)
            nsfw.add_field(name='Danbooru', value='0', inline=False)
            nsfw.add_field(name='Konachan', value='0', inline=False)
            nsfw.add_field(name='Lewd ASCII', value='0', inline=False)
            nsfw.add_field(name='E621', value='0', inline=False)
            nsfw.set_footer(text='NSFW')

            await ctx.send(file=file01, embed=nsfw)

        elif category.lower() == 'roleplay':

            roleplay = discord.Embed(description='```Roleplay```', color=discord.Colour.random())
            roleplay.set_author(name='Roleplay', icon_url='attachment://Saturn01.png')
            roleplay.add_field(name='Hug', value='0', inline=False)
            roleplay.add_field(name='Slap', value='0', inline=False)
            roleplay.add_field(name='Kiss', value='0', inline=False)
            roleplay.add_field(name='Pat', value='0', inline=False)
            roleplay.add_field(name='Lick', value='0', inline=False)
            roleplay.add_field(name='Arrest', value='0', inline=False)
            roleplay.add_field(name='Cuddle', value='0', inline=False)
            roleplay.add_field(name='Smug', value='0', inline=False)
            roleplay.add_field(name='Party', value='0', inline=False)
            roleplay.add_field(name='Ship', value='0', inline=False)
            roleplay.add_field(name='Kill License', value='0', inline=False)
            roleplay.add_field(name='Bite', value='0', inline=False)
            roleplay.add_field(name='Clap', value='0', inline=False)
            roleplay.add_field(name='Dance', value='0', inline=False)
            roleplay.add_field(name='Cringe', value='0', inline=False)
            roleplay.add_field(name='Facepalm', value='0', inline=False)
            roleplay.add_field(name='Glare', value='0', inline=False)
            roleplay.add_field(name='High Five', value='0', inline=False)
            roleplay.add_field(name='Laugh', value='0', inline=False)
            roleplay.add_field(name='Poke', value='0', inline=False)
            roleplay.add_field(name='Pout', value='0', inline=False)
            roleplay.add_field(name='Punch', value='0', inline=False)
            roleplay.add_field(name='Cheer', value='0', inline=False)
            roleplay.add_field(name='Purr', value='0', inline=False)
            roleplay.add_field(name='Sad', value='0', inline=False)
            roleplay.add_field(name='Shoot', value='0', inline=False)
            roleplay.add_field(name='Shrug', value='0', inline=False)
            roleplay.add_field(name='Shy', value='0', inline=False)
            roleplay.add_field(name='Smile', value='0', inline=False)
            roleplay.add_field(name='Stare', value='0', inline=False)
            roleplay.add_field(name='Stomp', value='0', inline=False)
            roleplay.add_field(name='Die', value='0', inline=False)
            roleplay.add_field(name='Wiggle', value='0', inline=False)
            roleplay.add_field(name='Wag', value='0', inline=False)
            roleplay.add_field(name='Divorce', value='0', inline=False)
            roleplay.add_field(name='Accept Marriage', value='0', inline=False)
            roleplay.add_field(name='Decline Marriage', value='0', inline=False)
            roleplay.add_field(name='Marriage', value='0', inline=False)
            roleplay.add_field(name='Inspire', value='0', inline=False)
            roleplay.add_field(name='Spank', value='0', inline=False)
            roleplay.add_field(name='Boop', value='0', inline=False)
            roleplay.add_field(name='Cry', value='0', inline=False)
            roleplay.add_field(name='Greet', value='0', inline=False)
            roleplay.add_field(name='Run', value='0', inline=False)
            roleplay.set_footer(text='Roleplay')

            await ctx.send(file=file01, embed=roleplay)

        elif category.lower() == 'search':

            search = discord.Embed(description='```Search````', color=discord.Colour.random())
            search.set_author(name='Search', icon_url='attachment://Saturn01.png')
            search.add_field(name='Spotify Album', value='0', inline=False)
            search.add_field(name='Spotify Artist', value='0', inline=False)
            search.add_field(name='Spotify Song Search', value='0', inline=False)
            search.add_field(name='Anime Character', value='0', inline=False)
            search.add_field(name='Crypto Value', value='0', inline=False)
            search.add_field(name='YouTube Channel', value='0', inline=False)
            search.add_field(name='YouTube Playlist', value='0', inline=False)
            search.add_field(name='Urban Dictionary', value='0', inline=False)
            search.add_field(name='TL;DR', value='0', inline=False)
            search.add_field(name='Stock Market', value='0', inline=False)
            search.add_field(name='Manga', value='0', inline=False)
            search.add_field(name='Song Lyrics', value='0', inline=False)
            search.add_field(name='Anime Episodes', value='0', inline=False)
            search.add_field(name='MyAnimeList API', value='0', inline=False)
            search.add_field(name='AniList API', value='0', inline=False)
            search.add_field(name='Minecraft Server Status', value='0', inline=False)
            search.add_field(name='Real Money Value', value='0', inline=False)
            search.set_footer(text='Search')

            await ctx.send(file=file01, embed=search)

        elif category.lower() == 'utility':

            utility = discord.Embed(description='```Utility```', color=discord.Colour.random())
            utility.set_author(name='Utility', icon_url='attachment://Saturn01.png')
            utility.add_field(name='Ping', value='0', inline=False)
            utility.add_field(name='Verify Status', value='0', inline=False)
            utility.add_field(name='Avatar', value='0', inline=False)
            utility.add_field(name='Waifu2x', value='0', inline=False)
            utility.add_field(name='Hex Color Generate', value='0', inline=False)
            utility.add_field(name='Password Generate', value='0', inline=False)
            utility.add_field(name='Colorize', value='0', inline=False)
            utility.add_field(name='AutoRole', value='0', inline=False)
            utility.add_field(name='Reaction Role', value='0', inline=False)
            utility.add_field(name='User Info', value='0', inline=False)
            utility.add_field(name='Server Info', value='0', inline=False)
            utility.add_field(name='Ignore Chat Restriction', value='0', inline=False)
            utility.add_field(name='Listen to Chat Restriction', value='0', inline=False)
            utility.add_field(name='Blacklist', value='0', inline=False)
            utility.add_field(name='Whitelist', value='0', inline=False)
            utility.add_field(name='Bot Channel', value='0', inline=False)
            utility.add_field(name='Free Channel', value='0', inline=False)
            utility.set_footer(text='Utility')

            await ctx.send(file=file01, embed=utility)

        elif category.lower() == 'math':

            math = discord.Embed(description='```Math```', color=discord.Colour.random())
            math.set_author(name='Math', icon_url='attachment://Saturn01.png')
            math.add_field(name='Addition', value='0', inline=False)
            math.add_field(name='Subtraction', value='0', inline=False)
            math.add_field(name='Division', value='0', inline=False)
            math.add_field(name='Multiplication', value='0', inline=False)
            math.add_field(name='Factorial', value='0', inline=False)
            math.add_field(name='Arithmetic Progression', value='0', inline=False)
            math.add_field(name='Geometric Progression', value='0', inline=False)
            math.add_field(name='First Degree Equation', value='0', inline=False)
            math.add_field(name='Quadratic Equation', value='0', inline=False)
            math.add_field(name='Cubic Equation', value='0', inline=False)
            math.add_field(name='Simple Combination', value='0', inline=False)
            math.add_field(name='Area of Plane Shapes', value='0', inline=False)
            math.add_field(name='Volume of Solids', value='0', inline=False)
            math.add_field(name='Trigonometric Ratios', value='0', inline=False)
            math.set_footer(text='Math')

            await ctx.send(file=file01, embed=math)

        elif category.lower() == 'gambling':

            gambling = discord.Embed(description='```Gambling```', color=discord.Colour.random())
            gambling.set_author(name='Gambling', icon_url='attachment://Saturn01.png')
            gambling.add_field(name='TBD', value='0', inline=False)
            gambling.set_footer(text='Gambling')

            await ctx.send(file=file01, embed=gambling)

        elif category.lower() == 'economy':

            economy = discord.Embed(description='```Economy```', color=discord.Colour.random())
            economy.set_author(name='Economy', icon_url='attachment://Saturn01.png')
            economy.add_field(name='TBD', value='0', inline=False)
            economy.set_footer(text='Economy')

            await ctx.send(file=file01, embed=economy)


# registra a classe no cogs
def setup(saturn):
    saturn.add_cog(Help(saturn))
