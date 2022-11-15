# bibliotecas
from helpers.envkeys import deepai_key
from discord.ext import commands
from discord import app_commands
from PIL import Image
import requests
import discord
import random


# realiza a criação da classe cog
class Utility(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Utility (Main) is Ready!!')

    # ping
    @app_commands.command(name='ping', description='You can use this to verify my ping')
    async def ping(self, interaction: discord.Interaction):

        ping = round(self.yume.latency * 1000)
        await interaction.response.send_message(f'I think it is **{ping}ms**, maybe?')

    # yume
    @app_commands.command(name='yume', description='Check if everything is fine')
    async def yume(self, interaction: discord.Interaction):

        await interaction.response.send_message(f'Everything looks fine here, no problems!', ephemeral=True)

    # avatar
    @app_commands.command(name='avatar', description="Sends a embed with the user's avatar")
    async def avatar(self, interaction: discord.Interaction, user: discord.Member = None):

        avatar = discord.Embed(color=discord.Colour.random())
        avatar.set_author(name=f"This is your avatar! Cute isn't it?")
        avatar.set_image(url=interaction.user.avatar)

        if user is not None:
            avatar.set_image(url=user.avatar)
            avatar.set_author(name=f"This is {user.name}'s avatar! Cute isn't it?")

        await interaction.response.send_message(embed=avatar)

    # waifu2x
    @app_commands.checks.has_permissions(attach_files=True)
    @app_commands.command(name='waifu2x', description="Utilizes AI to reduce image noise and improve quality")
    async def waifu2x(self, interaction: discord.Interaction, *, image: discord.Attachment):

        w2x_wait = discord.Embed(color=discord.Colour.random(), description='**Your image is being generated, please wait a moment.**')
        w2x_done = discord.Embed(color=discord.Colour.random(), description='**Here is your image!**')
        await interaction.response.send_message(embed=w2x_wait)

        r = requests.post('https://api.deepai.org/api/waifu2x', data={'image': f'{image.url}'}, headers={'api-key': f'{deepai_key()}'})

        if r.status_code == 200:
            data = r.json()
            url = data['output_url']

            w2x_done.set_image(url=url)
            w2x_done.set_footer(text="Remember to save the image, the link might broke after some minutes")
            await interaction.edit_original_response(embed=w2x_done)

        else:
            await interaction.response.send_message('Looks like something happened with the API, sorry...', ephemeral=True)
            await interaction.delete_original_response()

    # colorize
    @app_commands.checks.has_permissions(attach_files=True)
    @app_commands.command(name='colorize', description="Utilizes AI to colorize a black and white image")
    async def colorize(self, interaction: discord.Interaction, *, image: discord.Attachment):

        colorize_wait = discord.Embed(color=discord.Colour.random(), description='**Your image is being generated...**')
        colorize_done = discord.Embed(color=discord.Colour.random(), description="**here's your image, hope you liked it!**")
        await interaction.response.send_message(embed=colorize_wait)

        r = requests.post('https://api.deepai.org/api/colorizer', data={'image': f'{image.url}'}, headers={'api-key': f'{deepai_key()}'})

        if r.status_code == 200:
            data = r.json()
            url = data['output_url']

            colorize_done.set_image(url=url)
            colorize_done.set_footer(text="Remember to save the image, the link might broke after some minutes")
            await interaction.edit_original_response(embed=colorize_done)

        else:
            await interaction.response.send_message('Looks like something happened with the API, sorry...', ephemeral=True)
            await interaction.delete_original_response()


# realiza a criação da classe cog
class Info(commands.GroupCog, name='info'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Utility (Info) is Ready!!')

    # user information
    @app_commands.command(name='user', description='Show you some information about the a specific user')
    async def user(self, interaction: discord.Interaction, member: discord.Member = None):

        if member is None:
            member = interaction.user

        date = '%a, %d %b, %Y, %I:%M:%S %p'

        info = discord.Embed(description=member.display_name, color=discord.Colour.random())
        info.add_field(name='Server member since: ', value=member.joined_at.strftime(date))
        info.add_field(name='Account created in: ', value=member.created_at.strftime(date))
        info.set_author(name=str(member), icon_url=member.avatar.url)
        info.set_thumbnail(url=member.avatar.url)

        if len(member.roles) > 1:
            role_str = ', '.join([r.mention for r in member.roles][1:])
            info.add_field(name='Roles: [{}]'.format(len(member.roles) - 1), value=role_str, inline=False)

        perm_str = ', '.join([str(p[0]).replace('_', ' ').title() for p in member.guild_permissions if p[1]])
        info.add_field(name='Permissions: ', value=str(perm_str), inline=False)
        info.set_footer(text='User ID: ' + str(member.id))

        await interaction.response.send_message(embed=info)

    # server information
    @app_commands.command(name='server', description='Shows you some information about the current server')
    async def server(self, interaction: discord.Interaction):

        date = '%a, %d %b, %Y, %I:%M:%S %p'

        info = discord.Embed(description=f"{interaction.guild.name}'s Info", color=discord.Colour.random())
        info.set_author(name=str(interaction.guild.name), icon_url=interaction.guild.icon.url)
        info.set_thumbnail(url=interaction.guild.icon.url)
        info.add_field(name=f'Voice Channels: ', value=f'{len(interaction.guild.voice_channels)} channels.', inline=True)
        info.add_field(name=f'Text Channels: ', value=f'{len(interaction.guild.text_channels)} channels.', inline=True)
        info.add_field(name=f'Member Count: ', value=f'{interaction.guild.member_count} users.', inline=True)
        info.add_field(name=f'Created in: ', value=interaction.guild.created_at.strftime(date), inline=True)
        info.add_field(name=f'Server Owner: ', value=f'{interaction.guild.owner}', inline=False)
        info.set_footer(text='Server ID: ' + str(interaction.guild_id))

        await interaction.response.send_message(embed=info)


# realiza a criação da classe cog
class Generate(commands.GroupCog, name="generate"):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Utility (Generate) is Ready!!')

    # password generator
    @app_commands.command(name='password', description='Sends you a random generated password')
    async def password(self, interaction: discord.Interaction):

        lower = 'abcdefghijklmnopqrstuvwxyz'
        upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '`!@#$%^&*()_-+={[}]|\:;"<,>.?/'
        everything = lower + upper + numbers + symbols

        length = random.randint(8, 16)
        new_password = "".join(random.sample(everything, length))

        await interaction.response.send_message(f"Here's your brand new password: **{new_password}**", ephemeral=True)

    # color generator
    @app_commands.command(name='color', description='Generates a random color for you!')
    async def color(self, interaction: discord.Interaction):

        value_int = random.randint(0, 16777215)
        value_hex = str(hex(value_int))
        value_done = '#' + value_hex[2:]

        im = Image.new("RGB", (200, 150), value_done)
        im.save("./media/color.png")
        img = discord.File('./media/color.png', filename='color.png')

        color_embed = discord.Embed(description="This is the color that i've generated!", color=discord.Colour.random())
        color_embed.set_image(url='attachment://color.png')
        color_embed.set_footer(text=f'HEX: {value_done.upper()}')

        await interaction.response.send_message(embed=color_embed, file=img)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Utility(yume))
    await yume.add_cog(Generate(yume))
    await yume.add_cog(Info(yume))
