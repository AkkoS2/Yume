# bibliotecas
from helpers.assets import embed
from discord.ext import commands
from discord import app_commands
import discord


# realiza a criação da classe cog
class Help(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help is Ready!!')

    # help
    @app_commands.choices(category=[
        discord.app_commands.Choice(name='Fun', value=1),
        discord.app_commands.Choice(name='Image', value=2),
        discord.app_commands.Choice(name='Moderation', value=3),
        discord.app_commands.Choice(name='Music', value=4),
        discord.app_commands.Choice(name='NSFW', value=5),
        discord.app_commands.Choice(name='Roleplay', value=6),
        discord.app_commands.Choice(name='Actions', value=7),
        discord.app_commands.Choice(name='Search', value=8),
        discord.app_commands.Choice(name='Utility', value=9),
        discord.app_commands.Choice(name='Mathematics', value=10),
        discord.app_commands.Choice(name='Gambling', value=11),
        discord.app_commands.Choice(name='Economy', value=12),
        ])
    @app_commands.command(name='help', description='Need any help, cutie?')
    async def help(self, interaction: discord.Interaction, category: discord.app_commands.Choice[int], *, dm: bool):

        if dm is False:
            send_embed = interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            send_embed = interaction.user.send(embed=embed)
            await interaction.response.send_message('Check your DM, cutie~')

        if category.value == 1:
            embed.set_author(name='Help with Fun commands', icon_url=self.yume.user.avatar.url, url='https://github.com/AkkoS2/YumeBot')
            embed.add_field(name='Fortune Teller', value='TBD', inline=False)
            embed.add_field(name='Like', value='TBD', inline=False)
            embed.add_field(name='Quiz', value='TBD', inline=False)
            embed.add_field(name='Random Question', value='TBD', inline=False)
            embed.add_field(name='Rickroll', value='TBD', inline=False)
            embed.add_field(name='Random ASCII', value='TBD', inline=False)
            embed.add_field(name='Chaos Emerald', value='TBD', inline=False)
            embed.add_field(name='Vay Hek', value='TBD', inline=False)
            embed.add_field(name='Emoji to ASCII', value='TBD', inline=False)
            embed.add_field(name='Text to ASCII', value='TBD', inline=False)
            embed.add_field(name='Soon™', value='TBD', inline=False)
            embed.add_field(name='Roll', value='TBD', inline=False)
            embed.add_field(name='Luck', value='TBD', inline=False)
            embed.add_field(name='Jokes', value='TBD', inline=False)
            embed.add_field(name='Coin', value='TBD', inline=False)
            embed.add_field(name='Uwuify', value='TBD', inline=False)
            embed.add_field(name='Fortune Cookie', value='TBD', inline=False)
            embed.add_field(name='Rock, Paper, Scissors', value='TBD', inline=False)
            embed.add_field(name='Rate Things', value='TBD', inline=False)
            embed.add_field(name='Time to Duel', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 2:
            embed.set_author(name='Help with Image commands', icon_url=self.yume.user.avatar.url)
            embed.add_field(name='Tumblr', value='TBD', inline=False)
            embed.add_field(name='Imgur', value='TBD', inline=False)
            embed.add_field(name='Catboy', value='TBD', inline=False)
            embed.add_field(name='Catgirl', value='TBD', inline=False)
            embed.add_field(name='Cat', value='TBD', inline=False)
            embed.add_field(name='Dog', value='TBD', inline=False)
            embed.add_field(name='Reddit', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 3:
            embed.set_author(name='Help with Moderation commands', icon_url=self.yume.user.avatar.url)
            embed.add_field(name='Clear', value='TBD', inline=False)
            embed.add_field(name='Message Log', value='TBD', inline=False)
            embed.add_field(name='Staff Log', value='TBD', inline=False)
            embed.add_field(name='Create Category', value='TBD', inline=False)
            embed.add_field(name='Create Text Channel', value='TBD', inline=False)
            embed.add_field(name='Create Voice Channel', value='TBD', inline=False)
            embed.add_field(name='Delete Category', value='TBD', inline=False)
            embed.add_field(name='Delete Text Channel', value='TBD', inline=False)
            embed.add_field(name='Delete Voice Channel', value='TBD', inline=False)
            embed.add_field(name='Nuke Channel', value='TBD', inline=False)
            embed.add_field(name='Clone Channel', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 4:
            embed.set_author(name='Help with Music commands', icon_url=self.yume.user.avatar.url)
            embed.add_field(name='Join', value='TBD', inline=False)
            embed.add_field(name='Leave', value='TBD', inline=False)
            embed.add_field(name='Play', value='TBD', inline=False)
            embed.add_field(name='Now Playing', value='TBD', inline=False)
            embed.add_field(name='Pause', value='TBD', inline=False)
            embed.add_field(name='Stop', value='TBD', inline=False)
            embed.add_field(name='Skip', value='TBD', inline=False)
            embed.add_field(name='Repeat', value='TBD', inline=False)
            embed.add_field(name='Queue', value='TBD', inline=False)
            embed.add_field(name='Shuffle Queue', value='TBD', inline=False)
            embed.add_field(name='Queue Repeat', value='TBD', inline=False)
            embed.add_field(name='Reset', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 5:
            embed.set_author(name='Help with NSFW commands', icon_url=self.yume.user.avatar.url)
            embed.add_field(name='Yande.re', value='TBD', inline=False)
            embed.add_field(name='Rule34', value='TBD', inline=False)
            embed.add_field(name='Gelbooru', value='TBD', inline=False)
            embed.add_field(name='Safebooru', value='TBD', inline=False)
            embed.add_field(name='Danbooru', value='TBD', inline=False)
            embed.add_field(name='Konachan', value='TBD', inline=False)
            embed.add_field(name='Sankaku Complex', value='TBD', inline=False)
            embed.add_field(name='Lewd ASCII', value='TBD', inline=False)
            embed.add_field(name='E621', value='TBD', inline=False)
            embed.add_field(name='Reddit', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 6:
            embed.set_author(name='Help with Roleplay commands', icon_url=self.yume.user.avatar.url)
            embed.add_field(name='Hug', value='TBD', inline=False)
            embed.add_field(name='Slap', value='TBD', inline=False)
            embed.add_field(name='Kiss', value='TBD', inline=False)
            embed.add_field(name='Pat', value='TBD', inline=False)
            embed.add_field(name='Lick', value='TBD', inline=False)
            embed.add_field(name='Cuddle', value='TBD', inline=False)
            embed.add_field(name='Bite', value='TBD', inline=False)
            embed.add_field(name='Glare', value='TBD', inline=False)
            embed.add_field(name='Poke', value='TBD', inline=False)
            embed.add_field(name='Punch', value='TBD', inline=False)
            embed.add_field(name='Shoot', value='TBD', inline=False)
            embed.add_field(name='Stare', value='TBD', inline=False)
            embed.add_field(name='Stomp', value='TBD', inline=False)
            embed.add_field(name='Spank', value='TBD', inline=False)
            embed.add_field(name='Boop', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 7:
            embed.set_author(name='Help with Actions commands', icon_url=self.yume.user.avatar.url)
            embed.add_field(name='Arrest', value='TBD', inline=False)
            embed.add_field(name='Greet', value='TBD', inline=False)
            embed.add_field(name='Spook', value='TBD', inline=False)
            embed.add_field(name='Smug', value='TBD', inline=False)
            embed.add_field(name='Party', value='TBD', inline=False)
            embed.add_field(name='Ship', value='TBD', inline=False)
            embed.add_field(name='Kill', value='TBD', inline=False)
            embed.add_field(name='Clap', value='TBD', inline=False)
            embed.add_field(name='Dance', value='TBD', inline=False)
            embed.add_field(name='Shame', value='TBD', inline=False)
            embed.add_field(name='Facepalm', value='TBD', inline=False)
            embed.add_field(name='High Five', value='TBD', inline=False)
            embed.add_field(name='Laugh', value='TBD', inline=False)
            embed.add_field(name='Pout', value='TBD', inline=False)
            embed.add_field(name='Cheer', value='TBD', inline=False)
            embed.add_field(name='Purr', value='TBD', inline=False)
            embed.add_field(name='Sad', value='TBD', inline=False)
            embed.add_field(name='Shrug', value='TBD', inline=False)
            embed.add_field(name='Shy', value='TBD', inline=False)
            embed.add_field(name='Smile', value='TBD', inline=False)
            embed.add_field(name='Die', value='TBD', inline=False)
            embed.add_field(name='Wiggle', value='TBD', inline=False)
            embed.add_field(name='Wag', value='TBD', inline=False)
            embed.add_field(name='Cry', value='TBD', inline=False)
            embed.add_field(name='Run', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 8:
            embed.set_author(name='Help with Search commands', icon_url=self.yume.user.avatar.url)
            embed.add_field(name='Minecraft Server Status', value='TBD', inline=False)
            embed.add_field(name='Real Currency Converter', value='TBD', inline=False)
            embed.add_field(name='AniList API', value='TBD', inline=False)
            embed.add_field(name='MyAnimeList', value='TBD', inline=False)
            embed.add_field(name='Anime Episodes', value='TBD', inline=False)
            embed.add_field(name='Song Lyrics', value='TBD', inline=False)
            embed.add_field(name='Manga', value='TBD', inline=False)
            embed.add_field(name='Stock Market', value='TBD', inline=False)
            embed.add_field(name='Tl;Dr', value='TBD', inline=False)
            embed.add_field(name='Urban Dictionary', value='TBD', inline=False)
            embed.add_field(name='YouTube Playlist', value='TBD', inline=False)
            embed.add_field(name='YouTube Channel', value='TBD', inline=False)
            embed.add_field(name='Crypto Value', value='TBD', inline=False)
            embed.add_field(name='Anime Character', value='TBD', inline=False)
            embed.add_field(name='Spotify Song', value='TBD', inline=False)
            embed.add_field(name='Spotify Artist', value='TBD', inline=False)
            embed.add_field(name='Spotify Album', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 9:
            embed.set_author(name='Help with Utility commands', icon_url=self.yume.user.avatar.url)
            embed.add_field(name='Ping', value='TBD', inline=False)
            embed.add_field(name='Verify Status', value='TBD', inline=False)
            embed.add_field(name='Avatar', value='TBD', inline=False)
            embed.add_field(name='Waifu2x', value='TBD', inline=False)
            embed.add_field(name='Hexadecimal Color Generator', value='TBD', inline=False)
            embed.add_field(name='Password Generator', value='TBD', inline=False)
            embed.add_field(name='Colorize', value='TBD', inline=False)
            embed.add_field(name='Auto Role', value='TBD', inline=False)
            embed.add_field(name='Reaction Role', value='TBD', inline=False)
            embed.add_field(name='User Info', value='TBD', inline=False)
            embed.add_field(name='Server Info', value='TBD', inline=False)
            embed.add_field(name='Listen Chat Restriction', value='TBD', inline=False)
            embed.add_field(name='Ignore Chat Restriction', value='TBD', inline=False)
            embed.add_field(name='Blacklist', value='TBD', inline=False)
            embed.add_field(name='Whitelist', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 10:
            embed.set_author(name='Help with Math commands', icon_url=self.yume.user.avatar.url)
            embed.add_field(name='Addition', value='TBD', inline=False)
            embed.add_field(name='Subtraction', value='TBD', inline=False)
            embed.add_field(name='Division', value='TBD', inline=False)
            embed.add_field(name='Multiplication', value='TBD', inline=False)
            embed.add_field(name='Factorial', value='TBD', inline=False)
            embed.add_field(name='First Degree Equation', value='TBD', inline=False)
            embed.add_field(name='Second Degree Equation', value='TBD', inline=False)
            embed.add_field(name='Third Degree Equation', value='TBD', inline=False)
            embed.add_field(name='Arithmetic Progression', value='TBD', inline=False)
            embed.add_field(name='Geometric Progression', value='TBD', inline=False)
            embed.add_field(name='Simple Combination', value='TBD', inline=False)
            embed.add_field(name='Area of Plane Shapes', value='TBD', inline=False)
            embed.add_field(name='Volume of Solids', value='TBD', inline=False)
            embed.add_field(name='Trigonometric Ratios', value='TBD', inline=False)
            embed.add_field(name='Inverse Square Root', value='TBD', inline=False)
            embed.add_field(name='Square Root', value='TBD', inline=False)
            embed.set_footer(text='I hope this will be useful to you~')

            await send_embed

        if category.value == 11:
            await interaction.response.send_message("There's nothing here, yet...", ephemeral=True)

        if category.value == 12:
            await interaction.response.send_message("There's nothing here, yet...", ephemeral=True)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Help(yume))
