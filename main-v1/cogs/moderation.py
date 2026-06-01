# bibliotecas
from discord.ext import commands
from discord import app_commands
import asyncio
import discord


# realiza a criação da classe cog
class Moderation(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation is Ready!!')

    # clear
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.command(name='clear', description='Deletes a couple of messages')
    async def clear(self, interaction: discord.Interaction, *, amount: int):

        if amount == 0 or amount < 0 or amount >= 101:
            await interaction.response.send_message("You need to choose something between 1 and 100, cutie", ephemeral=True)

        if amount == 1:
            await interaction.channel.purge(limit=amount)
            await interaction.response.send_message(f"I've just deleted **{amount}** message.", ephemeral=True)

        await interaction.response.defer(ephemeral=True)
        await interaction.channel.purge(limit=amount + 1)
        await asyncio.sleep(3)
        await interaction.followup.send(f"I've deleted **{amount}** messages, just as you asked!")

    # nuke
    @app_commands.checks.has_permissions(manage_messages=True, manage_channels=True)
    @app_commands.command(name='nuke', description='After the nuke, the specified channel will be brand new with 0 messages')
    async def nuke(self, interaction: discord.Interaction, *, channel: discord.TextChannel):

        await channel.clone(reason=f'{interaction.user} has nuked the old channel')
        await channel.delete()

        await interaction.response.send_message(f'Yume have finished nuking the channel!')

    # clone
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name='clone', description='Create a copy of the specified channel')
    async def clone(self, interaction: discord.Interaction, *, channel: discord.TextChannel):

        await channel.clone(reason=f'{interaction.user} has cloned this channel.')
        await interaction.response.send_message(f"I've clone the channel just as you asked!")


# realiza a criação da classe cog
class Create(commands.GroupCog, name='create'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation (Create) is Ready!!')

    # text
    @app_commands.checks.has_permissions(manage_channels=True, manage_guild=True)
    @app_commands.command(name='text-channel', description='Creates a new text channel with the chosen name')
    async def text(self, interaction: discord.Interaction, *, name: str, nsfw: bool):

        await interaction.guild.create_text_channel(name=name, nsfw=nsfw)
        await interaction.response.send_message("I've created the text channel just like you wanted!")

    # voice
    @app_commands.checks.has_permissions(manage_channels=True, manage_guild=True)
    @app_commands.command(name='voice-channel', description='Creates a new voice channel with the chosen name')
    async def voice(self, interaction: discord.Interaction, *, name: str):

        await interaction.guild.create_voice_channel(name=name)
        await interaction.response.send_message("And it's created! Hope you like it~")

    # category
    @app_commands.checks.has_permissions(manage_channels=True, manage_guild=True)
    @app_commands.command(name='category', description='Creates a new category with the chosen name')
    async def category(self, interaction: discord.Interaction, *, name: str, position: int):

        await interaction.guild.create_category(name=name, position=position)
        await interaction.response.send_message("Done! I Hope you like it, hehe~")


# realiza a criação da classe cog
class Delete(commands.GroupCog, name='delete'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation (Delete) is Ready!!')

    # text
    @app_commands.checks.has_permissions(manage_channels=True, manage_guild=True)
    @app_commands.command(name='text-channel', description="I will the delete the specified text channel, be careful")
    async def text(self, interaction: discord.Interaction, *, channel: discord.TextChannel):

        await channel.delete()
        await interaction.response.send_message("And done! That text channel doesn't exist anymore")

    # voice
    @app_commands.checks.has_permissions(manage_channels=True, manage_guild=True)
    @app_commands.command(name='voice-channel', description='The specified voice channel will be gone forever...')
    async def voice(self, interaction: discord.Interaction, *, channel: discord.VoiceChannel):

        await channel.delete()
        await interaction.response.send_message("The voice channel you have chosen is now gone forever!")

    # category
    @app_commands.checks.has_permissions(manage_channels=True, manage_guild=True)
    @app_commands.command(name='category', description='This will delete the specified category, use carefully!')
    async def category(self, interaction: discord.Interaction, *, name: discord.CategoryChannel):

        await name.delete()
        await interaction.response.send_message("The category doesn't exist anymore, hehe~")


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Moderation(yume))
    await yume.add_cog(Create(yume))
    await yume.add_cog(Delete(yume))
