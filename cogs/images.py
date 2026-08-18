# Bibliotecas
from workers.database import guild_settings_get
from utils.localization import get_language
from assets.embeds import AvatarEmbed
from discord.ext import commands
from discord import app_commands
import logging
import discord


logger = logging.getLogger(__name__)


# Definição da classe Cog
class Images(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # Avisa quando Cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Images is Ready!')

    # Avatar
    @app_commands.command(name="avatar", description="I'll give you anyone's avatar!")
    async def avatar(self, interaction: discord.Interaction, user: discord.Member = None):

        guild_id = interaction.guild_id if interaction.guild_id else 0
        lang, persona = await guild_settings_get(guild_id)


        if user is None:
            user = interaction.user


        if user.id == interaction.user.id:
            json_key = "CommandAvatarSelf"

            url_avatar_global = user.avatar.url
            url_avatar_server = user.display_avatar.url

        elif user.id == self.yume.user.id:
            json_key = "CommandAvatarYume"

            url_avatar_global = user.avatar.url
            url_avatar_server = user.display_avatar.url

        else:
            json_key = "CommandAvatarOther"

            url_avatar_global = user.avatar.url
            url_avatar_server = user.display_avatar.url


        get_phrase = get_language(lang, "", json_key, persona)
        phrase = get_phrase.format(user = user.display_name)



        embed = AvatarEmbed.embed
        embed.set_author(name=f"{phrase}")

        embed.set_thumbnail(url=None)

        if url_avatar_server != url_avatar_global:
            embed.set_thumbnail(url=url_avatar_global)

        embed.set_image(url=url_avatar_server)
        embed.set_footer(text="From Yume, with love~ 🌸", icon_url=f"{str(self.yume.user.avatar.url)}")

        await interaction.response.send_message(embed=embed)


    # Banner
    # @app_commands.command(name="banner", description="")
    # async def banner(self, interaction: discord.Interaction, user: discord.Member = None):

    #     guild_id = interaction.guild_id if interaction.guild_id else 0
    #     lang, persona = await guild_settings_get(guild_id)


# Registra a classe nos Cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Images(yume))