# bibliotecas
from mcstatus import JavaServer, BedrockServer
from discord.ext import commands
from discord import app_commands
from helpers import searchers
import discord


# realiza a criação da classe cog
class Search(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Search is Ready!!')

    # Minecraft Server Status
    @app_commands.choices(version=[
        discord.app_commands.Choice(name='Java', value=1),
        discord.app_commands.Choice(name='Bedrock', value=2)
    ])
    @app_commands.command(name='mcserver', description="I'll show you the details about a minecraft server!")
    async def mcserver(self, interaction: discord.Interaction, *, version: discord.app_commands.Choice[int], ip: str):

        if version.value == 1:
            server = JavaServer.lookup(f'{ip}')
            status = server.status()

            java = discord.Embed(colour=discord.Colour.random())
            java.add_field(name='Server IP:', value=ip, inline=False)
            java.add_field(name='Player Count:', value=f'{status.players_online}**/**{status.players.max}', inline=False)

            await interaction.response.send_message(embed=java)

        else:
            server = BedrockServer.lookup(f'{ip}')
            status = server.status()

            bedrock = discord.Embed(colour=discord.Colour.random())
            bedrock.add_field(name='Server IP:', value=ip, inline=False)
            bedrock.add_field(name='Player Count:', value=f'{status.players_online}', inline=False)

            await interaction.response.send_message(embed=bedrock)

    # Spotify
    @app_commands.choices(kind=[
        discord.app_commands.Choice(name='Artist', value=0),
        discord.app_commands.Choice(name='Album', value=1),
        discord.app_commands.Choice(name='Song', value=2)
    ])
    @app_commands.command(name='spotify', description='Search something in spotify')
    async def spotfy(self, interaction: discord.Interaction, *, kind: discord.app_commands.Choice[int], search: str):

        searchers.spotify = search
        result = searchers.spotify_search()

        if kind.value == 0:
            await interaction.response.send_message(result[0])
        if kind.value == 1:
            await interaction.response.send_message(result[1])
        else:
            await interaction.response.send_message(result[2])


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Search(yume))
