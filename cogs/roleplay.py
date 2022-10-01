# bibliotecas
from discord.ext import commands
from discord import app_commands
from helpers import searchers
import discord


# realiza a criação da classe cog
class RolePlay(commands.GroupCog, name="rp"):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Roleplay is Ready!!')

    # hug
    @app_commands.command(name='hug', description='Give a hug to someone!')
    async def hug(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.roleplay_gif = 'hug'

        hug = discord.Embed(color=discord.Colour.random())
        hug.set_image(url=str(searchers.nekos_best()))
        hug.set_footer(text='Just lovely!')

        if user == interaction.user:

            hug.set_author(name='Feeling lonely? Come here, Yume is gonna hug you ❤️')
            await interaction.response.send_message(embed=hug)

        hug.set_author(name=f'{interaction.user.name} just hugged {user.name}!')
        await interaction.response.send_message(embed=hug)

    # slap
    @app_commands.command(name='slap', description='Slaps someone')
    async def slap(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.roleplay_gif = 'slap'

        slap = discord.Embed(color=discord.Colour.random())
        slap.set_image(url=str(searchers.nekos_best()))
        slap.set_footer(text='That was funny to watch... hehe~')

        if user == interaction.user:
            slap.set_author(name="If you insist... i'm so sorry...")
            await interaction.response.send_message(embed=slap)

        slap.set_author(name=f'{interaction.user.name} slapped {user.name}! I wonder if it hurts? hmm...')
        await interaction.response.send_message(embed=slap)

    # kiss
    @app_commands.command(name='kiss', description='Give a kiss to someone')
    async def kiss(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.roleplay_gif = 'kiss'

        kiss = discord.Embed(color=discord.Colour.random())
        kiss.set_image(url=str(searchers.nekos_best()))
        kiss.set_footer(text='it was really cute!')

        if user == interaction.user:
            kiss.set_author(name="Awwnn... Come here, Yume is gonna give you a kiss!")
            await interaction.response.send_message(embed=kiss)

        kiss.set_author(name=f'{interaction.user.name} just kissed {user.name}! In front of everyone!')
        await interaction.response.send_message(embed=kiss)

    # pat
    @app_commands.command(name='pat', description='You can pat someone')
    async def pat(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.roleplay_gif = 'pat'

        pat = discord.Embed(color=discord.Colour.random())
        pat.set_image(url=str(searchers.nekos_best()))
        pat.set_footer(text='Everyone should receive a little pat!')

        if user == interaction.user:
            pat.set_author(name="Seems that you are lonely... I'm gonna pat you, don't worry!")
            await interaction.response.send_message(embed=pat)

        pat.set_author(name=f'{interaction.user.name} just patted {user.name}! ❤️')
        await interaction.response.send_message(embed=pat)

    # lick
    @app_commands.command(name='lick', description='Licks the chosen user')
    async def lick(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.roleplay_gif = 'lick'

        lick = discord.Embed(color=discord.Colour.random())
        lick.set_image(url=str(searchers.nekos_best()))
        lick.set_footer(text='I wonder how it tastes...')

        if user == interaction.user:
            lick.set_author(name="I wasn't wanting to lick you... You... taste funny, are you taking showers?")
            await interaction.response.send_message('the command is not ready :p', ephemeral=True)

        lick.set_author(name=f'{interaction.user.name} licked {user.name}! why...?')
        await interaction.response.send_message('the command is not ready :p', ephemeral=True)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(RolePlay(yume))
