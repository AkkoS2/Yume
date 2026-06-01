# Bibliotecas utilizadas neste arquivo
from discord.ext import commands
from discord import app_commands
from utils import helpers
from uwuipy import Uwuipy
from utils import embeds
import discord
import random


# Realiza a definição da classe cog
class Fun(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # Avisa quando a classe cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun is Ready!')

    # Fortune Cookie
    @app_commands.command(name='fortune', description='Let me get a fortune cookie for you!')
    async def fortune(self, interaction: discord.Interaction):

        cookie = discord.File('./media/cookie.gif', filename='cookie.gif')
        fortune = random.choice(open('./texts/fortunes.txt').read().splitlines())

        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=fortune, icon_url=interaction.user.avatar.url)
        embed.set_image(url="attachment://cookie.gif")
        embed.set_footer(text="And that's what the cookie said to Yume.")

        await interaction.response.send_message(embed=embed, file=cookie)

    # Reverse Text
    @app_commands.command(name='reverse', description='?naem uoy od tahW')
    async def reverse(self, interaction: discord.Interaction, text: str):

        await interaction.response.send_message(text[::-1])

    # Roll
    @app_commands.command(name='roll', description='Roll some points. Score is not tracked.')
    async def roll(self, interaction: discord.Interaction):

        points = random.randint(0, 2147483647)

        if points == 727:
            await interaction.response.send_message(f'**{points}!! WYSI!! WYFSI!!!!!**')

        if points == 4000:
            await interaction.response.send_message(f'Q U A T R O   M I L   P O N T O S.')
        
        if points == 2147483647:
            await interaction.response.send_message(f'You maxed out the 32-bit signed integer limit with **{points}** points!')
           
        await interaction.response.send_message(f"You rolled **{points}** points. Yume is always happy to roll for you at any time~")

    # 8Ball
    @app_commands.command(name='8ball', description='Let the almighty 8-ball answer your questions~!')
    async def eightball(self, interaction: discord.Interaction, *, question: str):

        answers = random.choice(open('./texts/8ball.txt').read().splitlines())
        await interaction.response.send_message(answers)

    # Uwuify
    @app_commands.command(name='uwuify', description='i-it makes you s-s-speak w-wike (˘ε˘) t-t-t-this?!?! >/////<')
    async def uwuify(self, interaction: discord.Interaction, *, phrase: str):

        uwu = Uwuipy(None, 0.3, 0.3, 0.10, 1, False, 4)
        await interaction.response.send_message(uwu.uwuify(phrase))

    # Twitter Personality
    @app_commands.command(name='twitter-personality', description='An AI generated personality of an X profile.')
    async def twt_persona(self, interaction: discord.Interaction, *, twitter_handle: str):

        helpers.profile = twitter_handle
        result = await helpers.twtpersonality()

        embed = discord.Embed(title=f"{result[1]}", url=f"https://x.com/{twitter_handle}", description=f"{result[2]}", color=discord.Color.random())
        embed.set_author(name="Wordware Twitter Personality", url=f"https://twitter.wordware.ai/{twitter_handle}", icon_url=embeds.txtlink[6])
        embed.set_thumbnail(url=f"{result[0]['src']}")

        await interaction.response.send_message(embed=embed)

    # Twitter Compatibility
    @app_commands.command(name='twitter-compatibility', description="----")


    # Ship
    @app_commands.command(name='ship', description="----")


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Fun(yume))
