# bibliotecas
from helpers.assets import embed
from discord.ext import commands
from discord import app_commands
import discord


# realiza a criação da classe cog
class Help(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help is Ready!!')

    # help
    @app_commands.choices(category=[
        discord.app_commands.Choice(name='Fun', value=1),
        discord.app_commands.Choice(name='Image', value=2),
        discord.app_commands.Choice(name='Moderation', value=3),
        discord.app_commands.Choice(name='Music', value=4),
        discord.app_commands.Choice(name='NSFW', value=5),
        discord.app_commands.Choice(name='Roleplay', value=6),
        discord.app_commands.Choice(name='Actions', value=7),
        discord.app_commands.Choice(name='Search', value=8),
        discord.app_commands.Choice(name='Utility', value=9),
        discord.app_commands.Choice(name='Mathematics', value=10),
        discord.app_commands.Choice(name='Gambling', value=11),
        discord.app_commands.Choice(name='Economy', value=12),
        ])
    @app_commands.command(name='help', description='Need any help, cutie?')
    async def help(self, interaction: discord.Interaction, category: discord.app_commands.Choice[int], *, dm: bool):

        if category.value == 1:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('1')

        if category.value == 2:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('2')

        if category.value == 3:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('3')

        if category.value == 4:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('4')

        if category.value == 5:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('5')

        if category.value == 6:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('6')

        if category.value == 7:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('7')

        if category.value == 8:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('8')

        if category.value == 9:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('9')

        if category.value == 10:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('10')

        if category.value == 11:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('11')

        if category.value == 12:

            if dm is True:
                await interaction.response.send_message('true')

            await interaction.response.send_message('12')


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Help(yume))
