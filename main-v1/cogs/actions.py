# bibliotecas
from discord.ext import commands
from discord import app_commands
from utils.assets import embed
from utils import helpers
import discord
import random
import json


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

        helpers.nekos_gif = 'smug'
        embed.set_image(url=str(helpers.nekos_best()))
        embed.set_footer(text='So much smugness!')

        if user is None or user == interaction.user:
            embed.set_author(name=f'{interaction.user.name} is smugging!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is smugging at {user.name}')
        await interaction.response.send_message(embed=embed)

    # party
    @app_commands.command(name='party', description="It's a party")
    async def party(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'party'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text='I wonder if parties are fun?')

        if user is None or user == interaction.user:
            embed.set_author(name=f'Yume is gonna party with you!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is partying with {user.name}!')
        await interaction.response.send_message(embed=embed)

    # kill
    @app_commands.command(name='kill', description="People die if they are killed...")
    async def kill(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'kill'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text='Why you have to do this?')

        if user is None or user == interaction.user:
            embed.set_author(name=f"{interaction.user.name} Just killed itself... I'm gonna miss you")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} killed {user.name}, why????? YOU MONSTER')
        await interaction.response.send_message(embed=embed)

    # clap
    @app_commands.command(name='clap', description='Applause for no reason')
    async def clap(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'clap'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text='Claps are too loud for me but, continue as you like!')

        if user is None or user == interaction.user:
            embed.set_author(name=f'{interaction.user.name} is clapping!!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} started clapping with {user.name}')
        await interaction.response.send_message(embed=embed)

    # dance
    @app_commands.command(name='dance', description='Looks like you like dancing...')
    async def dance(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.nekos_gif = 'dance'
        embed.set_image(url=str(helpers.nekos_best()))
        embed.set_footer(text="Yume doesn't know how to dance, so i'm gonna keep watching")

        if user is None or user == interaction.user:
            embed.set_author(name=f'{interaction.user.name} started dancing, it looks fun!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is dancing with {user.name}, how cute!~')
        await interaction.response.send_message(embed=embed)

    # shame
    @app_commands.command(name='shame', description="i'm ashamed... and it's somebody's fault.")
    async def shame(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'shame'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text="that's kinda cringe, not gonna lie")

        if user is None or user == interaction.user:
            embed.set_author(name=f'{interaction.user.name} is ashamed with himself!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is ashamed about {user.name}, why?')
        await interaction.response.send_message(embed=embed)

    # facepalm
    @app_commands.command(name='facepalm', description="facepalm because that was dumb")
    async def facepalm(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'facepalm'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text="that's uh... nevermind...")

        if user is None or user == interaction.user:
            embed.set_author(name=f'sigh....')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} facepalmed because of {user.name}!')
        await interaction.response.send_message(embed=embed)

    # laugh
    @app_commands.command(name='laugh', description="everyone likes to laugh")
    async def laugh(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'laugh'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text="hehe~")

        if user is None or user == interaction.user:
            embed.set_author(name=f'You know, laughing alone because of nothing is kinda creepy')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is laughing with {user.name}, did something funny happened?')
        await interaction.response.send_message(embed=embed)

    # pout
    @app_commands.command(name='pout', description="hmpf")
    async def pout(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.nekos_gif = 'pout'
        embed.set_image(url=str(helpers.nekos_best()))
        embed.set_footer(text="I'm not talking, hmpf!")

        if user is None or user == interaction.user:
            embed.set_author(name=f'Did something happened with {interaction.user.name}?')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{user.name} is making {interaction.user.name} being a pouty!')
        await interaction.response.send_message(embed=embed)

    # purr
    @app_commands.command(name='purr', description="nyaa~")
    async def purr(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'purr'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text="nyaa nyaan~")

        if user is None or user == interaction.user:
            embed.set_author(name=f'Do you think you are a little kitty, huh?')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is purring at {user.name}....')
        await interaction.response.send_message(embed=embed)

    # shrug
    @app_commands.command(name='shrug', description="i have no idea")
    async def shrug(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.nekos_gif = 'shrug'
        embed.set_image(url=str(helpers.nekos_best()))
        embed.set_footer(text="i don't know, why?")

        if user is None or user == interaction.user:
            embed.set_author(name=f'Hey look! {interaction.user.name} is shrugging!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} started shrugging at {user.name}, is there a reason?')
        await interaction.response.send_message(embed=embed)

    # smile
    @app_commands.command(name='smile', description="happy times, hehe")
    async def smile(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.nekos_gif = 'smile'
        embed.set_image(url=str(helpers.nekos_best()))
        embed.set_footer(text="Happy times are so comfy~")

        if user is None or user == interaction.user:
            embed.set_author(name=f'You should always smile, {interaction.user.name}!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is smiling at {user.name}, how cute~')
        await interaction.response.send_message(embed=embed)

    # die
    @app_commands.command(name='die', description="you're ded")
    async def die(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'die'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text="Hey, I think this person just died, what do?")

        if user is None or user == interaction.user:
            embed.set_author(name=f'{interaction.user.name} died, somebody call an ambule!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{user.name} just made {interaction.user.name} die, how mean!')
        await interaction.response.send_message(embed=embed)

    # wiggle
    @app_commands.command(name='wiggle', description="you like to wiggle")
    async def highfive(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'wiggle'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text="Wiggle again! Please!")

        if user is None or user == interaction.user:
            embed.set_author(name=f"It seems that {interaction.user.name} likes to wiggle")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is wiggling with {user.name}, so cute!')
        await interaction.response.send_message(embed=embed)

    # cry
    @app_commands.command(name='cry', description="sobs")
    async def cry(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.nekos_gif = 'cry'
        embed.set_image(url=str(helpers.nekos_best()))
        embed.set_footer(text="What happened? Why are you crying?")

        if user is None or user == interaction.user:
            embed.set_author(name=f"Why are you crying, {interaction.user.name} did something happened?")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{user.name} is mean and made {interaction.user.name} cry')
        await interaction.response.send_message(embed=embed)

    # run
    @app_commands.command(name='run', description="let's run away")
    async def run(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'run'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text="Faster! Faster! You're too slow!")

        if user is None or user == interaction.user:
            embed.set_author(name=f'Why are you running away, {interaction.user.name}?')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is running away from {user.name}, maybe I should run away too?')
        await interaction.response.send_message(embed=embed)

    # highfive
    @app_commands.command(name='highfive', description="high fives, and more high fives")
    async def highfive(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.kawaii_gif = 'highfive'
        embed.set_image(url=str(helpers.kawaii_api()))
        embed.set_footer(text="High Five! Do it again!")

        if user is None or user == interaction.user:
            embed.set_author(name=f'Yume is going to do a high five with you, come here!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} did a high five with {user.name}!')
        await interaction.response.send_message(embed=embed)

    # arrest
    @app_commands.command(name='arrest', description="Let's arrest someone!")
    async def arrest(self, interaction: discord.Interaction, user: discord.Member = None):

        f = open('./utils/urlgifs.json')
        data = json.load(f)

        embed.set_image(url=str(data['gifs']['arrest']['urls'][random.randint(0, 7)]))
        embed.set_footer(text="Ohh! So you're our new guest at the prison??")

        if user is None or user == interaction.user:
            embed.set_author(name=f"You're under arrest, do not resist!")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} just arrested {user.name}, why??')
        await interaction.response.send_message(embed=embed)

    # greet
    @app_commands.command(name='greet', description="Greets someone, that's it")
    async def greet(self, interaction: discord.Interaction, user: discord.Member = None):

        f = open('./utils/urlgifs.json')
        data = json.load(f)

        embed.set_image(url=str(data['gifs']['greet']['urls'][random.randint(0, 9)]))
        embed.set_footer(text='Hello there!!')

        if user is None or user == interaction.user:
            embed.set_author(name=f"You wanted to be greeted, huh? Then I'm gonna do it~")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} greeted {user.name}, so nice to see it!!')
        await interaction.response.send_message(embed=embed)

    # cheer
    @app_commands.command(name='cheer', description='Do you want to cheer something or someone?')
    async def cheer(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.tenor_gif = 'cheer anime'
        embed.set_image(url=str(helpers.tenor()))
        embed.set_footer(text="Let's all do it together next time!")

        if user is None or user == interaction.user:
            embed.set_author(name=f"Since you want this, I'm gonna do it!")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'Look! {interaction.user.name} is cheering with {user.name}!')
        await interaction.response.send_message(embed=embed)

    # sad
    @app_commands.command(name='sad', description='Be sad at someone or because of someone :c')
    async def sad(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.tenor_gif = 'sad anime'
        embed.set_image(url=str(helpers.tenor()))
        embed.set_footer(text="I Wonder what happened...")

        if user is None or user == interaction.user:
            embed.set_author(name=f"Did something happened? Are you alright?")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'Perhaps {user.name} made {interaction.user.name} sad?')
        await interaction.response.send_message(embed=embed)

    # shy
    @app_commands.command(name='shy', description="Are you shy?? That's adorable...")
    async def shy(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.tenor_gif = 'shy anime'
        embed.set_image(url=str(helpers.tenor()))
        embed.set_footer(text="You're so cute when you are shy~")

        if user is None or user == interaction.user:
            embed.set_author(name=f"Did you just made yourself shy about yourself? How cute~")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is acting shy in front of {user.name}!')
        await interaction.response.send_message(embed=embed)

    # wag
    @app_commands.command(name='wag', description='Wanna wag at someone? I can help!')
    async def wag(self, interaction: discord.Interaction, user: discord.Member = None):

        helpers.tenor_gif = 'wag anime'
        embed.set_image(url=str(helpers.tenor()))
        embed.set_footer(text="That's.... cute....")

        if user is None or user == interaction.user:
            embed.set_author(name=f"Why are you wagging at yourself?")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'Everyone Look! {interaction.user.name} is wagging at {user.name}!')
        await interaction.response.send_message(embed=embed)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Actions(yume))
