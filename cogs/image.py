# Bibliotecas utilizadas neste arquivo
from utils.embeds import ImgEmbed
from utils import buttons, helpers
from discord.ext import commands
from discord import app_commands
import discord


# Realiza a definição da classe cog
class Image(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # Avisa quando a classe cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Image is Ready!')

    # Reddit
    @app_commands.command(name='reddit', description='Gets a image from the chosen subreddit')
    async def reddit(self, interaction: discord.Interaction, *, subreddit: str):

        helpers.sub_reddit = subreddit
        result = await helpers.reddit_search()
        url = 'https://reddit.com' + result[4]

        embed = discord.Embed(color=discord.Color.random())
        embed.set_author(name=result[3], url='https://reddit.com' + result[4])
        embed.set_footer(text=result[5] + f' on r/{subreddit}')
        embed.set_image(url=str(result[0]))

        nsfw_content = "Looks like the post I got is tagged as NSFW, you can try again or you can use a NSFW channel."

        if result[2] is True and result[1] is False and not interaction.channel.is_nsfw():
            await interaction.response.send_message(nsfw_content, ephemeral=True)

        elif result[2] is True and result[1] is False and interaction.channel.is_nsfw():
            await interaction.response.send_message(result[3] + '\n' + url)

        if result[2] is True and result[1] is True:
            await interaction.response.send_message(result[3] + '\n' + url)

        if result[1] is False and not interaction.channel.is_nsfw():
            await interaction.response.send_message(nsfw_content, ephemeral=True)

        if result[1] is True:
            await interaction.response.send_message(embed=embed)

        elif result[1] is False and interaction.channel.is_nsfw():
            await interaction.response.send_message(embed=embed)

    # Cachorrinhos
    @app_commands.command(name='dogs', description="Yume will give you a random image of a doggy!")
    async def dog(self, interaction: discord.Interaction):

        ImgEmbed.embed.set_image(url=f"{await helpers.doggy_finder()}")
        ImgEmbed.embed.set_author(name="Here's the doggy I've got for you!! Hope you like it~")

        await interaction.response.send_message(embed=ImgEmbed.embed)

    # Gatinhos
    @app_commands.command(name='cats', description="Yume will give you a random image of a kitty!")
    async def cat(self, interaction: discord.Interaction):

        ImgEmbed.embed.set_image(url=f"{await helpers.kitty_finder()}")
        ImgEmbed.embed.set_author(name="Here's the kitty I've got for you!! Hope you like it~")

        await interaction.response.send_message(embed=ImgEmbed.embed)

    # Waifus
    @app_commands.command(name="waifu", description="I'll give you a random image of a waifu")
    async def waifu(self, interaction: discord.Interaction):

        helpers.nekos_gif = 'waifu'
        ImgEmbed.embed.set_image(url = await helpers.nekos_best())
        ImgEmbed.embed.set_author(name="Here's the waifu Yume got for you!!")

        await interaction.response.send_message(embed=ImgEmbed.embed)

    # Husbandos
    @app_commands.command(name="husbando", description="I'll give you a random image of a husbando")
    async def husbando(self, interaction: discord.Interaction):

        helpers.nekos_gif = 'husbando'
        ImgEmbed.embed.set_image(url=await helpers.nekos_best())
        ImgEmbed.embed.set_author(name="Here's the husbando Yume got for you!!")

        await interaction.response.send_message(embed=ImgEmbed.embed)

    # Nekos
    @app_commands.command(name="neko", description="I'll give you a cute random image of a catgirl!")
    async def neko(self, interaction: discord.Interaction):

        helpers.nekos_gif = 'neko'
        ImgEmbed.embed.set_image(url=await helpers.nekos_best())
        ImgEmbed.embed.set_author(name="Here's the neko Yume got for you!!")

        await interaction.response.send_message(embed=ImgEmbed.embed)

    # Kitsunes
    @app_commands.command(name="kitsune", description="I'll give you a cute random image of a kitsune!")
    async def kitsune(self, interaction: discord.Interaction):

        helpers.nekos_gif = 'kitsune'
        ImgEmbed.embed.set_image(url=await helpers.nekos_best())
        ImgEmbed.embed.set_author(name="Here's the kitsune Yume got for you!!")

        await interaction.response.send_message(embed=ImgEmbed.embed)

    # Image Search


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Image(yume))
