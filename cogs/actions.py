# Bibliotecas utilizadas neste arquivo
from utils.buttons import ActionButtons
from discord.ext import commands
from discord import app_commands
from utils import helpers
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

        helpers.nekos_gif = 'smug'
        embed = discord.Embed(color=discord.Color.random(), description=f'{interaction.user.display_name} is smugging~')
        embed.set_image(url=str(await helpers.nekos_best()))
        embed.set_footer(text='So much smugness!')

        await interaction.response.send_message(embed=embed)

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
