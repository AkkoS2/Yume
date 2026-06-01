# Bibliotecas utilizadas neste arquivo
from discord.ext import commands
from discord import app_commands
from utils import helpers
import discord


# Realiza a definição da classe cog
class Utility(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # Avisa quando a classe cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Utility is Ready!')

    # Ping
    @app_commands.command(name='ping', description='Use this tool to check Yume\'s latency.')
    async def ping(self, interaction: discord.Interaction):

        ping = round(self.yume.latency * 1000)
        await interaction.response.send_message(f'{ping}ms')

    # Avatar
    @app_commands.command(name='avatar', description="Sends an embed with the user's avatar.")
    async def avatar(self, interaction: discord.Interaction, user: discord.Member = None):

        avatar = discord.Embed(color=discord.Color.random())
        avatar.set_author(name=f"This is your avatar! Look how cute it is!")
        avatar.set_image(url=interaction.user.avatar)

        if user is not None:
            avatar.set_image(url=user.avatar)
            avatar.set_author(name=f"This is {user.name}'s avatar! Cute, isn't it?")

        await interaction.response.send_message(embed=avatar)

    # Currency
    @app_commands.command(name='currency', description="Check out current world exchange rates!")

    # Weather
    @app_commands.command(name='weather', description="Yume will check the weather in any part of Earth!")


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Utility(yume))
