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

        await interaction.response.send_message("Action commands are currently being reworked :c", view=view)

    # Party
    @app_commands.command(name='party', description="----")

    # Kill
    @app_commands.command(name='kill', description="----")

    # Clap
    @app_commands.command(name='clap', description="----")

    # Dance
    @app_commands.command(name='dance', description="----")

    # Shame
    @app_commands.command(name='shame', description="----")

    # Facepalm
    @app_commands.command(name='facepalm', description="----")

    # Laugh
    @app_commands.command(name='laugh', description="----")

    # Pout
    @app_commands.command(name='pout', description="----")

    # Purr
    @app_commands.command(name='purr', description="----")

    # Shrug
    @app_commands.command(name='shrug', description="----")

    # Smile
    @app_commands.command(name='smile', description="----")

    # Cry
    @app_commands.command(name='cry', description="----")

    # Arrest
    @app_commands.command(name='arrest', description="----")

    # Greet
    @app_commands.command(name='greet', description="----")

    # Sad
    @app_commands.command(name='sad', description="----")

    # Shy
    @app_commands.command(name='shy', description="----")

    # Bribe
    @app_commands.command(name='bribe', description="----")

    # Bark
    @app_commands.command(name='bark', description="----")

    # Meow
    @app_commands.command(name='meow', description="----")


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Actions(yume))
