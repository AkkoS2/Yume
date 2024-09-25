# bibliotecas
from utils.embeds import GenericEmbed
from discord.ext import commands
from discord import app_commands
from utils import helpers
import discord


# Realiza a definição da classe cog
class RolePlay(commands.GroupCog, name='rp'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # Avisa quando a classe cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Roleplay is ready!')

    # hug
    @app_commands.command(name='hug', description='Give a hug to someone!')
    async def hug(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'hug'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text='Just lovely!!!')

        if user == interaction.user:
            GenericEmbed.embed.set_author("Feeling Lonely? Come here, Yume is gonna hug you~ ❤️")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{interaction.user.display_name} just hugged {user.display_name}!")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # slap
    @app_commands.command(name='slap', description='Slaps someone')
    async def slap(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'slap'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text='That was funny to watch... hehe~')

        if user == interaction.user:
            GenericEmbed.embed.set_author("If you insist... i'm so sorry...")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{interaction.user.display_name} slapped {user.display_name}! I wonder what happened...")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # kiss
    @app_commands.command(name='kiss', description='Kisses someone.')
    async def kiss(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'kiss'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text='It was really cute!')

        if user == interaction.user:
            GenericEmbed.embed.set_author("Awwnn... Come here, Yume is gonna give you a kiss!")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{interaction.user.display_name} just kissed {user.display_name}! In front of everyone!")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # pat
    @app_commands.command(name='pat', description='You can pat someone')
    async def pat(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'pat'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text='Everyone should receive a little pat!')

        if user == interaction.user:
            GenericEmbed.embed.set_author("Seems that you are lonely... I'm gonna pat you, don't worry!")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{interaction.user.display_name} is patting {user.display_name}! ❤️")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # bite
    @app_commands.command(name='bite', description='Bites someone, just make sure to not hurt them')
    async def bite(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'bite'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text='Does it hurt? Maybe it was too strong?')

        if user == interaction.user:
            GenericEmbed.embed.set_author("I'm gonna bite you then.... Kinda chewy.....")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{interaction.user.display_name} is biting {user.display_name}, why??")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # stare
    @app_commands.command(name='stare', description='Just... stare at someone for no reason')
    async def stare(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'stare'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text='Be careful not to stare for too long - they might notice!')

        if user == interaction.user:
            GenericEmbed.embed.set_author("I'm gonna stare at you then... please don't look away!")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{interaction.user.display_name} is staring at {user.display_name}.....")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # shoot
    @app_commands.command(name='shoot', description='Shoots a user, careful to not kill them')
    async def shoot(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'shoot'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text="Oh my God, are you okay? I'm calling an ambulance, stay strong, please!")

        if user == interaction.user:
            GenericEmbed.embed.set_author("Suuuree.... hehe~")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{user.display_name} just got shot by {interaction.user.display_name}!!! Should we call the police?")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # punch
    @app_commands.command(name='punch', description='Punches someone!')
    async def punch(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'punch'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text='That actually might have been painful, I guess?')

        if user == interaction.user:
            GenericEmbed.embed.set_author("I usually don't like punching people, but since you asked so nicely~")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{interaction.user.display_name} punched {user.display_name}, how strong was it..?")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # poke
    @app_commands.command(name='poke', description='Pokes another user, if you want to')
    async def poke(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'poke'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text='Is it annoying to keep poking people?')

        if user == interaction.user:
            GenericEmbed.embed.set_author("Yume likes poking others, come here!!!")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{interaction.user.display_name} is poking {user.display_name}. I want to poke them too!")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # cuddle
    @app_commands.command(name='cuddle', description='Stop being annoying, cuddle with someone instead')
    async def cuddle(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'cuddle'
        GenericEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        GenericEmbed.embed.set_footer(text="That's the sweetest thing i've seen~")

        if user == interaction.user:
            GenericEmbed.embed.set_author("Seems like you are always lonely, huh? Come here, cutie!")
            await interaction.response.send_message(embed=GenericEmbed.embed)

        GenericEmbed.embed.set_author(name=f"{interaction.user.display_name} is cuddling with {user.display_name}, do not interrupt them!")
        await interaction.response.send_message(embed=GenericEmbed.embed)

    # lick

    # stomp

    # boop


# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(RolePlay(yume))
