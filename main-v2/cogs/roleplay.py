# bibliotecas
from utils.embeds import RpEmbed
from utils import helpers, buttons
from discord.ext import commands
from discord import app_commands
import discord


# Realiza a definição da classe cog
class RolePlay(commands.GroupCog, name='rp'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # Avisa quando a classe cog iniciar
    @commands.Cog.listener()
    async def on_ready(self):
        print('Roleplay is Ready!')

    # hug
    @app_commands.command(name='hug', description='Give a hug to someone!')
    async def hug(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'hug'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text='Squishy squashy hugs, yay!')

        if user == interaction.user:
            RpEmbed.embed.set_footer(text="Snuggie snuggie snuggie :3")
            RpEmbed.embed.set_author(name="Aww... come here, Yume is gonna hug you~ ❤") # Does this convert emoji text or is it limited to direct Unicode input? --flushedpancake
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{interaction.user.display_name} just hugged {user.display_name}! ❤️❤️❤️")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # slap
    @app_commands.command(name='slap', description='Slaps someone.')
    async def slap(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'slap'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text='I wonder what happened between them?')

        if user == interaction.user:
            RpEmbed.embed.set_footer(text="I didn't want to hurt you...")
            RpEmbed.embed.set_author(name="If you insist... I'm so, so sorry...")
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{interaction.user.display_name} slapped {user.display_name}! Ouch!")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # kiss
    @app_commands.command(name='kiss', description='Kisses someone.')
    async def kiss(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'kiss'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text='So romantic... This is making Yume\'s heart flutter <3')

        if user == interaction.user:
            RpEmbed.embed.set_footer(text="This... feels like more... than... a dream could wish...")
            RpEmbed.embed.set_author(name="Aww... Come here, Yume is gonna give you a kiss!")
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{interaction.user.display_name} just kissed {user.display_name}! ❤️❤️❤️")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # pat
    @app_commands.command(name='pat', description='Give someone a pat')
    async def pat(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'pat'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text='Everybody deserves a little pat!')

        if user == interaction.user:
            RpEmbed.embed.set_footer(text="Aww, you're like a cute puppy.")
            RpEmbed.embed.set_author(name="You want Yume's patpats? Sure!! hehe~")
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{interaction.user.display_name} is patting {user.display_name}! ❤️")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # bite
    @app_commands.command(name='bite', description='Bites someone.')
    async def bite(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'bite'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text='I hope that didn\'t hurt too much...')

        if user == interaction.user:
            RpEmbed.embed.set_footer(text="Was that meant to be a love bite?")
            RpEmbed.embed.set_author(name="You want me to bite you? Um, okay...")
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{interaction.user.display_name} is biting {user.display_name}...")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # stare
    @app_commands.command(name='stare', description='Just... stare at someone for no reason.')
    async def stare(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'stare'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text='Don\'t trigger the sixth sense by staring too long...')

        if user == interaction.user:
            RpEmbed.embed.set_footer(text="Are you enjoying the staring contest?")
            RpEmbed.embed.set_author(name="I'm gonna stare at you then... please don't look away!")
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{interaction.user.display_name} is staring at {user.display_name}...")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # shoot
    @app_commands.command(name='shoot', description='Shoots a user.')
    async def shoot(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'shoot'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text="Oh my God, are you okay? I'm calling an ambulance, stay strong, please!")

        if user == interaction.user:
            RpEmbed.embed.set_footer(text="Was listening to the user command the right thing to do here...?")
            RpEmbed.embed.set_author(name="Suuuree.... hehe~")
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{user.display_name} just got shot by {interaction.user.display_name}!")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # punch
    @app_commands.command(name='punch', description='Punches someone!')
    async def punch(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'punch'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text='Ow... that actually might have been painful...')

        if user == interaction.user:
            RpEmbed.embed.set_footer(text="Where did that energy even come from?")
            RpEmbed.embed.set_author(name="I usually don't like punching people, but since you asked so nicely...")
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{interaction.user.display_name} punched {user.display_name}, how strong was it..?")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # poke
    @app_commands.command(name='poke', description='Pokes another user.')
    async def poke(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'poke'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text='POKE 53280, PEEK(53281)') # I am so fucking sorry -- flushedpancake

        if user == interaction.user:
            RpEmbed.embed.set_author(name="Yume likes poking others, come here!!!")
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{interaction.user.display_name} is poking {user.display_name}. I want to poke them too!")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # cuddle
    @app_commands.command(name='cuddle', description='Cuddle with someone!')
    async def cuddle(self, interaction: discord.Interaction, *, user: discord.Member):

        helpers.nekos_gif = 'cuddle'
        view = buttons.PingButton()
        buttons.pinged_one = user.mention

        RpEmbed.embed.set_image(url=str(await helpers.nekos_best()))
        RpEmbed.embed.set_footer(text="A warm cuddle makes everything better!")

        if user == interaction.user:
            RpEmbed.embed.set_author(name="You want Yume cuddles?! Come here, cutie!")
            await interaction.response.send_message(embed=RpEmbed.embed)

        RpEmbed.embed.set_author(name=f"{interaction.user.display_name} is cuddling with {user.display_name}, do not interrupt them!")
        await interaction.response.send_message(embed=RpEmbed.embed, view=view)

    # lick
    @app_commands.command(name='lick', description="----")

    # stomp
    @app_commands.command(name='stomp', description="----")


    # boop
    @app_commands.command(name='boop', description="----")



# Realiza o registro da classe nos cogs
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(RolePlay(yume))
