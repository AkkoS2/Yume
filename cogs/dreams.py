# Bibliotecas utilizadas neste arquivo
from discord.ext import commands
from discord import app_commands
import discord


# Realiza a definição da classe cog
class Dreams(commands.GroupCog, name='yume'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # Avisa quando a classe cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Yume is currently dreaming....')

    # verify
    @app_commands.command(name='status', description="Check if everything is fine with me...")
    async def verify(self, interaction: discord.Interaction):

        await interaction.response.send_message('Everything seems fine~', ephemeral=True)


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Dreams(yume))
