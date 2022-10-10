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
    @commands.has_permissions(manage_messages=True)
    @app_commands.command(name='clear', description='deletes a couple of messages')
    async def clear(self, interaction: discord.Interaction, *, amount: int):

        if amount == 0 or amount < 0 or amount >= 101:
            await interaction.response.send_message("You need to choose something between 1 and 100, cutie", ephemeral=True)

        if amount == 1:
            await interaction.channel.purge(limit=amount)
            await interaction.response.send_message(f"I've just deleted **{amount}** message.")

        await interaction.channel.purge(limit=amount)
        await interaction.response.send_message(f"I've deleted **{amount}** messages just as you asked!")


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Moderation(yume))
