# bibliotecas
from helpers.texts import eightball
from discord.ext import commands
from discord import app_commands
from helpers.assets import embed
from uwuipy import uwuipy
import discord
import Joking
import random
import json


# realiza a criação da classe cog
class Fun(commands.Cog):
    def __init(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun is Ready!!')

    # Fortune Cookie
    @app_commands.command(name='fortune', description='Let me check your fortune with cookies!')
    async def fortune(self, interaction: discord.Interaction):

        cookie = discord.File('./media/cookie.gif', filename='cookie.gif')
        lines = open('./helpers/fortunes.txt').read().splitlines()
        fortune = random.choice(lines)

        embed.set_author(name=fortune, icon_url=interaction.user.avatar.url)
        embed.set_image(url='attachment://cookie.gif')
        embed.set_footer(text="This is what the cookie said to Yume!")
        await interaction.response.send_message(embed=embed, file=cookie)

    # Uwuify
    @app_commands.command(name='uwuify', description='it makes you s-s-speak w-wike (˘ε˘) t-t-t-this?!?!')
    async def uwuify(self, interaction: discord.Interaction, *, phrase: str):

        uwu = uwuipy(None, 0.3, 0.3, 0.2, 1)
        await interaction.response.send_message(uwu.uwuify(phrase))

    # 8ball
    @app_commands.command(name='8ball', description='let the 8 ball gives you a answer!')
    async def eightball(self, interaction: discord.Interaction, *, question: str):

        answer = random.choice(eightball())
        await interaction.response.send_message(answer)

    # Vay Hek
    @app_commands.command(name='vayhek', description='Why are these fools still breathing my air?!?!')
    async def vayhek(self, interaction: discord.Interaction):

        vay = discord.File('./media/Vay_Hek.mp4', filename='Vay_Hek.mp4')
        hek = 'WHY ARE THESE FOOLS STILL BREATHING MY AIR?!?!?!?!'
        await interaction.response.send_message(hek, file=vay)

    # SoonTM
    @app_commands.command(name='soon', description='SoonTM')
    async def soon(self, interaction: discord.Interaction):

        soontm = discord.File('./media/soonTM.jpg', filename='soonTM.jpg')
        await interaction.response.send_message('soon™', file=soontm)

    # Jokes
    @app_commands.command(name='joke', description="I'll tell you a random dad joke!")
    async def joke(self, interaction: discord.Interaction):

        await interaction.response.send_message(Joking.random_dad_joke())

    # Coin
    @app_commands.choices(side=[
        discord.app_commands.Choice(name='Heads', value='heads'),
        discord.app_commands.Choice(name='Tails', value='tails')
    ])
    @app_commands.command(name='coin', description="I'm gonna toss a coin, you will try to guess wich side it landed!")
    async def coin(self, interaction: discord.Interaction, side: discord.app_commands.Choice[str]):

        value = random.randint(0, 100)
        toss = 'heads', 'tails'
        result = random.choice(toss)
        coin = discord.File('./media/Coin.gif', filename='Coin.gif')

        f = open('./helpers/urlgifs.json')
        data = json.load(f)

        if value == 100:
            embed.set_author(name='The result is... Middle!! What??')
            embed.set_image(url='attachment://coin.gif')
            await interaction.response.send_message(embed=embed, file=coin)

        if side.value.lower() == result:
            embed.set_author(name=f'And the result is.... {result.upper()}! Congratulations!!')
            embed.set_image(url=str(data['gifs']['toss']['urls'][random.randint(0, 3)]))
            await interaction.response.send_message(embed=embed)

        else:
            embed.set_author(name=f"Uhh... Looks like you're wrong... The result was {result.upper()}")
            embed.set_image(url=str(data['gifs']['toss']['urls'][random.randint(0, 3)]))
            await interaction.response.send_message(embed=embed)

    # jankenpon
    @app_commands.choices(choice=[
        discord.app_commands.Choice(name='Rock', value='rock'),
        discord.app_commands.Choice(name='Paper', value='paper'),
        discord.app_commands.Choice(name='Scissors', value='scissors')
    ])
    @app_commands.command(name='rps', description='Lets play Rock, Paper, Scissors!')
    async def rps(self, interaction: discord.Interaction, choice: discord.app_commands.Choice[str]):

        rps = 'rock', 'paper', 'scissors'
        yume_choice = random.choice(rps)

        if yume_choice == choice.value:
            await interaction.response.send_message('Aiko desho!')
        elif yume_choice == 'rock' and choice.value == 'scissors' or yume_choice == 'paper' and choice.value == 'rock' or yume_choice == 'scissors' and choice.value == 'paper':
            await interaction.response.send_message(f"I'm the winner ehehe~")
        else:
            await interaction.response.send_message(f"You're the winner, congrats!")

    # invert
    @app_commands.command(name='invert', description='?naem uoy od tahW')
    async def invert(self, interaction: discord.Interaction, text: str):

        await interaction.response.send_message(text[::-1])


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Fun(yume))
