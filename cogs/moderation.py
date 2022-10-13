# bibliotecas
from discord.ext import commands
from discord import app_commands
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
    @app_commands.command(name='clear', description='deletes a couple of messages')
    async def clear(self, interaction: discord.Interaction, *, amount: int):

        if amount == 0 or amount < 0 or amount >= 101:
            await interaction.response.send_message("You need to choose something between 1 and 100, cutie", ephemeral=True)

        if amount == 1:
            await interaction.channel.purge(limit=amount,)
            await interaction.response.send_message(f"I've just deleted **{amount}** message.")

        await interaction.response.send_message(f"I'm going to delete {amount} messages, as you asked")
        await interaction.channel.purge(limit=amount + 1)

    # nuke
    @app_commands.checks.has_permissions(manage_messages=True, manage_channels=True)
    @app_commands.command(name='nuke', description='after the nuke, the specified channel will be brand new with 0 messages')
    async def nuke(self, interaction: discord.Interaction, *, channel: discord.TextChannel):

        channel_new = await channel.clone(reason=f'{interaction.user} has nuked the old channel')
        await channel.delete()

        await interaction.response.send_message(f'Yume have finished nuking the channel!')

    # clone
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.command(name='clone', description='create a copy of the specified channel')
    async def clone(self, interaction: discord.Interaction, *, channel: discord.TextChannel):

        await channel.clone(reason=f'{interaction.user} has cloned this channel.')
        await interaction.response.send_message(f"I've clone the channel just as you asked!")


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Moderation(yume))
