# Bibliotecas
from workers.database import guild_settings_get
from utils.localization import get_language
from discord.ext import commands
from discord import app_commands
import logging
import discord


logger = logging.getLogger(__name__)


# Definição da classe Cog
class Utility(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # Avisa quando o cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Utility is Ready!')

    # Ping
    @app_commands.command(name="ping", description="You can use this to see my current latency.")
    async def ping(self, interaction: discord.Interaction):

        guild_id = interaction.guild_id if interaction.guild_id else 0
        lang, persona = await guild_settings_get(guild_id)

        latency = round(self.yume.latency * 1000)

        get_phrase = get_language(lang, "", "CommandPing", persona)
        phrase = get_phrase.format(ping = latency)

        await interaction.response.send_message(phrase)

    # Check Yume
    @app_commands.command(name='verify', description="You can use this to see if i'm working.")
    async def verify(self, interaction: discord.Interaction):

        guild_id = interaction.guild_id if interaction.guild_id else 0
        lang, persona = await guild_settings_get(guild_id)

        phrase = get_language(lang, "", "CommandVerifyStatus", persona)
        await interaction.response.send_message(phrase)



# Registra a classe nos Cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Utility(yume))
