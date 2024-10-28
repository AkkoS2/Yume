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
    @app_commands.command(name='roll', description='Rolls a random value to you...')
    async def roll(self, interaction: discord.Interaction):

        points = random.randint(0, 1000)

        if points == 727:
            await interaction.response.send_message(f'**{points}!! WYSI!! WYFSI!!!!!**')

        await interaction.response.send_message(f"You've got **{points}** points! what do you think?? wanna try again?")

    # 8Ball
    @app_commands.command(name='8ball', description='Let the almighty 8Ball answer your questions~')
    async def eightball(self, interaction: discord.Interaction, *, question: str):

        answers = random.choice(open('./texts/8ball.txt').read().splitlines())
        await interaction.response.send_message(answers)

    # Uwuify
    @app_commands.command(name='uwuify', description='it makes you s-s-speak w-wike (˘ε˘) t-t-t-this?!?!')
    async def uwuify(self, interaction: discord.Interaction, *, phrase: str):

        uwu = Uwuipy(None, 0.3, 0.3, 0.10, 1, False, 4)
        await interaction.response.send_message(uwu.uwuify(phrase))

    # Twitter Personality
    @app_commands.command(name='twitter-personality', description='an AI generated personality of a twitter profile')
    async def twt_persona(self, interaction: discord.Interaction, *, twitter_handle: str):

        helpers.profile = twitter_handle
        result = await helpers.twtpersonality()

        embed = discord.Embed(title=f"{result[1]}", url=f"https://x.com/{twitter_handle}", description=f"{result[2]}", color=discord.Color.random())
        embed.set_author(name="Wordware Twitter Personality", url=f"https://twitter.wordware.ai/{twitter_handle}", icon_url=embeds.txtlink[6])
        embed.set_thumbnail(url=f"{result[0]['src']}")

        await interaction.response.send_message(embed=embed, ephemeral=True)

    # Twitter Compatibility

    # Ship


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Fun(yume))
