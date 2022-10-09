# bibliotecas
from discord.ext import commands
from discord import app_commands
from helpers.assets import embed
from helpers import searchers
import discord


# realiza a criação da classe cog
class Actions(commands.GroupCog, name='action'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Actions is Ready!!')

    # smug
    @app_commands.command(name='smug', description='Show your smugness')
    async def smug(self, interaction: discord.Interaction, user: discord.Member = None):

        searchers.nekos_gif = 'smug'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text='So much smugness!')

        if user is None or user == interaction.user:
            embed.set_author(name=f'{interaction.user.name} is smugging!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is smugging at {user.name}')
        await interaction.response.send_message(embed=embed)

    # party
    @app_commands.command(name='party', description="It's a party")
    async def party(self, interaction: discord.Interaction, user: discord.Member = None):

        searchers.kawaii_gif = 'party'
        embed.set_image(url=str(searchers.kawaii_api()))
        embed.set_footer(text='I wonder if parties are fun?')

        if user is None or user == interaction.user:
            embed.set_author(name=f'Yume is gonna party with you!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is partying with {user.name}!')
        await interaction.response.send_message(embed=embed)

    # kill
    @app_commands.command(name='kill', description="People die if they are killed...")
    async def kill(self, interaction: discord.Interaction, user: discord.Member = None):

        searchers.kawaii_gif = 'kill'
        embed.set_image(url=str(searchers.kawaii_api()))
        embed.set_footer(text='Why you have to do this?')

        if user is None or user == interaction.user:
            embed.set_author(name=f"{interaction.user.name} Just killed itself... I'm gonna miss you")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} killed {user.name}, why????? YOU MONSTER')
        await interaction.response.send_message(embed=embed)

    # clap
    @app_commands.command(name='clap', description='Applause for no reason')
    async def clap(self, interaction: discord.Interaction, user: discord.Member = None):

        searchers.kawaii_gif = 'clap'
        embed.set_image(url=str(searchers.kawaii_api()))
        embed.set_footer(text='Claps are too loud for me but, continue as you like!')

        if user is None or user == interaction.user:
            embed.set_author(name=f'{interaction.user.name} is clapping!!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} started clapping with {user.name}')
        await interaction.response.send_message(embed=embed)

    # dance
    @app_commands.command(name='dance',description='Looks like you like dancing...')
    async def dance(self, interaction: discord.Interaction, user: discord.Member = None):

        searchers.nekos_gif = 'dance'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text="Yume doesn't know how to dance, so i'm gonna keep watching")

        if user is None or user == interaction.user:
            embed.set_author(name=f'{interaction.user.name} started dancing, it looks fun!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is dancing with {user.name}, how cute!~')
        await interaction.response.send_message(embed=embed)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Actions(yume))
