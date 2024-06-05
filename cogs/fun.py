# Bibliotecas utilizadas neste arquivo
from utils.embeds import GenericEmbed
from discord.ext import commands
from discord import app_commands
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
        lines = open('./texts/fortunes.txt').read().splitlines()
        fortune = random.choice(lines)

        embed = GenericEmbed.embed
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


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Fun(yume))
