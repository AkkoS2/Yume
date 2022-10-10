# bibliotecas
from discord.ext import commands
from discord import app_commands
from helpers.assets import embed
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

        searchers.nekos_gif = 'hug'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text='Just lovely!')

        if user == interaction.user:
            embed.set_author(name='Feeling lonely? Come here, Yume is gonna hug you ❤️')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} just hugged {user.name}!')
        await interaction.response.send_message(embed=embed)

    # slap
    @app_commands.command(name='slap', description='Slaps someone')
    async def slap(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.nekos_gif = 'slap'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text='That was funny to watch... hehe~')

        if user == interaction.user:
            embed.set_author(name="If you insist... i'm so sorry...")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} slapped {user.name}! I wonder if it hurts? hmm...')
        await interaction.response.send_message(embed=embed)

    # kiss
    @app_commands.command(name='kiss', description='Give a kiss to someone')
    async def kiss(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.nekos_gif = 'kiss'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text='it was really cute!')

        if user == interaction.user:
            embed.set_author(name="Awwnn... Come here, Yume is gonna give you a kiss!")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} just kissed {user.name}! In front of everyone!')
        await interaction.response.send_message(embed=embed)

    # pat
    @app_commands.command(name='pat', description='You can pat someone')
    async def pat(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.nekos_gif = 'pat'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text='Everyone should receive a little pat!')

        if user == interaction.user:
            embed.set_author(name="Seems that you are lonely... I'm gonna pat you, don't worry!")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} just patted {user.name}! ❤️')
        await interaction.response.send_message(embed=embed)

    # bite
    @app_commands.command(name='bite', description='Bites someone, just make sure to not hurt them')
    async def bite(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.nekos_gif = 'bite'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text='Does it hurt? Maybe it was too strong?')

        if user == interaction.user:
            embed.set_author(name="I'm gonna bite you then. Is here a good place?")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} has bitten {user.name}, I wonder why?')
        await interaction.response.send_message(embed=embed)

    # stare
    @app_commands.command(name='stare', description='Just... stare at someone for no reason')
    async def stare(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.nekos_gif = 'stare'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text='Careful to not stare too much, they may notice it...')

        if user == interaction.user:
            embed.set_author(name="I'm gonna stare at you then... please don't look away!")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is staring at {user.name}, strange...')
        await interaction.response.send_message(embed=embed)

    # shoot
    @app_commands.command(name='shoot', description='Shoots a user, careful to not kill them')
    async def shoot(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.nekos_gif = 'shoot'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text="Oh my God, are you okay? I'm calling a ambulance, stay strong, please!")

        if user == interaction.user:
            embed.set_author(name="I wasn't wanting to shoot you but, that might be.... hehe~")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} just shot {user.name}, should we call the police?')
        await interaction.response.send_message(embed=embed)

    # punch
    @app_commands.command(name='punch', description='Punches someone!')
    async def punch(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.nekos_gif = 'punch'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text='That actually might have been painful, I guess?')

        if user == interaction.user:
            embed.set_author(name="I usually don't like punching people, but since you asked so nicely~")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} punched {user.name}, how strong was it..?')
        await interaction.response.send_message(embed=embed)

    # poke
    @app_commands.command(name='poke', description='Pokes another user, if you want to')
    async def poke(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.nekos_gif = 'poke'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text='Is it annoying to keep poking people?')

        if user == interaction.user:
            embed.set_author(name='Yume likes poking others, come here!!!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} poked {user.name}. I want to poke them too!')
        await interaction.response.send_message(embed=embed)

    # cuddle
    @app_commands.command(name='cuddle', description='Stop being annoying, cuddle with someone instead')
    async def cuddle(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.nekos_gif = 'cuddle'
        embed.set_image(url=str(searchers.nekos_best()))
        embed.set_footer(text="That was one of the most cute things I've ever seen")

        if user == interaction.user:
            embed.set_author(name='Seems like you are always alone, huh? come here, cutie!')
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is cuddling with {user.name}, do not interrupt them!')
        await interaction.response.send_message(embed=embed)

    # lick
    @app_commands.command(name='lick', description='Licks another user or even yourself')
    async def lick(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.kawaii_gif = 'lick'
        embed.set_image(url=str(searchers.kawaii_api()))
        embed.set_footer(text='How does it taste?')

        if user == interaction.user:
            embed.set_author(name="I really didn't want to lick you, but since you asked for it...")
            await interaction.response.send_message(embed=embed)

        if user.id == 944414497966264321:
            embed.set_author(name="Do you really like licking metal? You can keep licking then...")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is licking {user.name}, I wonder why.... Does it taste good?')
        await interaction.response.send_message(embed=embed)

    # stomp
    @app_commands.command(name='stomp', description='Stomps another user, be careful to not hurt them')
    async def stomp(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.kawaii_gif = 'stomp'
        embed.set_image(url=str(searchers.kawaii_api()))
        embed.set_footer(text="Looks like it's hurting... but it's funny to watch~")

        if user == interaction.user:
            embed.set_author(name="You asked for it, come here! and don't even think of running away~")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} stomped {user.name}, maybe they liked it...')
        await interaction.response.send_message(embed=embed)

    # boop
    @app_commands.command(name='boop', description="boop another user, that's it")
    async def boop(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.kawaii_gif = 'boop'
        embed.set_image(url=str(searchers.kawaii_api()))
        embed.set_footer(text="Hey~ this is funny hehe~")

        if user == interaction.user:
            embed.set_author(name="I like doing this, it's funny and cute!")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} has boop {user.name}, this is cute, please continue!')
        await interaction.response.send_message(embed=embed)

    # glare
    @app_commands.command(name='glare', description='why are you glaring at me?')
    async def glare(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.tenor_gif = 'anime glare'
        embed.set_image(url=str(searchers.tenor()))
        embed.set_footer(text="Someone's glaring so much~")

        if user == interaction.user:
            embed.set_author(name="Yume is going to glare at you, hope you don't mind~")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'{interaction.user.name} is glaring at {user.name} so intensely!')
        await interaction.response.send_message(embed=embed)

    # spank
    @app_commands.command(name='spank', description='spanks someone!')
    async def spank(self, interaction: discord.Interaction, *, user: discord.Member):

        searchers.tenor_gif = 'anime spank'
        embed.set_image(url=str(searchers.tenor()))
        embed.set_footer(text="Looks like someone's has been naughty...")

        if user == interaction.user:
            embed.set_author(name="This will probably hurt, i'm sorry")
            await interaction.response.send_message(embed=embed)

        embed.set_author(name=f'I wonder why {interaction.user.name} is spanking {user.name}...')
        await interaction.response.send_message(embed=embed)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(RolePlay(yume))
