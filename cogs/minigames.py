# Bibliotecas
from workers.database import guild_settings_get
from utils.localization import get_language
from discord.ext import commands
from discord import app_commands
import discord
import logging


logger = logging.getLogger(__name__)


# Definição classe Cog
class Minigames(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # Avisa quando Cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Minigames is Ready!')


    # 8Ball
    @app_commands.command(name="8ball", description="may the all-mighty ball answer you!")
    async def eightball(self, interaction: discord.Interaction, question: str):

        guild_id = interaction.guild_id if interaction.guild_id else 0
        lang, _ = await guild_settings_get(guild_id)

        answer = get_language(lang, "8ball", "Answers")
        await interaction.response.send_message(answer)


    # Fortune Cookie
    @app_commands.command(name="fortune", description="want a fortune cookie?~")
    async def fortune(self, interaction: discord.Interaction):

        guild_id = interaction.guild_id if interaction.guild_id else 0
        lang, _ = await guild_settings_get(guild_id)

        cookies = get_language(lang, "fortune_cookie", "Fortunes")
        await interaction.response.send_message(cookies)


# Registra a classe nos Cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Minigames(yume))
