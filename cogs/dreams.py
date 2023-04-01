# bibliotecas
from discord.ext import commands
from discord import app_commands
import discord


# realiza a criação da classe cog
class Dreams(commands.GroupCog, name='yume'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Yume dreams are working!')

    # verify
    @app_commands.command(name='status', description='Check if everything is fine with me')
    async def verify(self, interaction: discord.Interaction):

        await interaction.response.send_message(f'Everything looks fine here, no problems!', ephemeral=True)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Dreams(yume))
