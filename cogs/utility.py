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
    @app_commands.command(name='ping', description='You can use this to verify my ping')
    async def ping(self, interaction: discord.Interaction):

        ping = round(self.yume.latency * 1000)
        await interaction.response.send_message(f'{ping}ms')

    # Avatar
    @app_commands.command(name='avatar', description="Sends a embed with the user's avatar")
    async def avatar(self, interaction: discord.Interaction, user: discord.Member = None):

        avatar = discord.Embed(color=discord.Color.random())
        avatar.set_author(name=f"This is your avatar! Look how cute it is!")
        avatar.set_image(url=interaction.user.avatar)

        if user is not None:
            avatar.set_image(url=user.avatar)
            avatar.set_author(name=f"This is {user.name}'s avatar! Cute isn't it?")

        await interaction.response.send_message(embed=avatar)

    # Currency
    @app_commands.command(name='currency', description="Let's you see the currency values")
    async def currency(self, interaction: discord.Interaction, *, currency1: str, amount: int, currency2: str):

        helpers.values = currency1, currency2, amount
        result = await helpers.currency_finder()

        await interaction.response.send_message(f"Yume thinks that **{amount} {currency1.upper()}** is equal to **{result} {currency2.upper()}**!!", ephemeral=True)


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Utility(yume))
