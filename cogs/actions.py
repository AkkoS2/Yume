# Bibliotecas utilizadas neste arquivo
from discord.ext import commands
from discord import app_commands
from utils import buttons
import discord


# Realiza a definição da classe cog
class Actions(commands.GroupCog, name='action'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # Avisa quando a classe cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Actions is Ready!')

    # Smug
    @app_commands.command(name='smug', description='Show your smugness~')
    async def smug(self, interaction: discord.Interaction):

        await interaction.response.send_message("Action commands are currently being reworked :c")

    # Party

    # Kill

    # Clap

    # Dance

    # Shame

    # Facepalm

    # Laugh

    # Pout

    # Purr

    # Shrug

    # Smile

    # Cry

    # Arrest

    # Greet

    # Sad

    # Shy

    # Bribe


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Actions(yume))
