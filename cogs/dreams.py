# Bibliotecas utilizadas neste arquivo
from utils.embeds import GenericEmbed, InfoEmbed
from discord.ext import commands
from discord import app_commands
from utils import modals
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

    # Verify
    @app_commands.command(name='status', description="Check if everything is fine with me...")
    async def verify(self, interaction: discord.Interaction):

        await interaction.response.send_message('Everything seems fine~', ephemeral=True)

    # Information
    @app_commands.command(name='info', description="Yume's useful things and links")
    async def info(self, interaction: discord.Interaction):

        await interaction.response.send_message(embed=InfoEmbed.iembed, ephemeral=True)

    # Typo Report
    @app_commands.command(name='typo', description="a way to report any typos you've found so far!")
    async def typo(self, interaction: discord.Interaction):

        typo = modals.TypoModal()
        await interaction.response.send_modal(typo)

    # Suggestions
    @app_commands.command(name='suggestion', description="you can give suggestions on how to improve me!")
    async def suggestion(self, interaction: discord.Interaction):

        suggestion = modals.SuggestionModal()
        await interaction.response.send_modal(suggestion)

    # Command Ideas
    @app_commands.command(name='ideas', description="have any command ideas? share them with me~")
    async def ideas(self, interaction: discord.Interaction):

        ideas = modals.IdeaModal()
        await interaction.response.send_modal(ideas)


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Dreams(yume))
