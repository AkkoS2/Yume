# bibliotecas
from helpers.envkeys import rapid_api, exrate_api
from mcstatus import JavaServer, BedrockServer
from discord.ext import commands
from discord import app_commands
from helpers import searchers
import requests
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

    # Crypto value
    @app_commands.command(name='crypto', description="I'll show you the current value of the chosen crypto!")
    async def crypto(self, interaction: discord.Interaction, *, crypto: str):

        r = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={crypto.upper()}USDT")
        data = r.json()

        if 'symbol' in data:
            value = data['price'][:-5]
            await interaction.response.send_message(f"{crypto.upper()} is worth **{value} USDT** at the moment!")

        value = data['msg']
        await interaction.response.send_message(f"There's a problem... ({value})")

    # Urban Dictionary
    @app_commands.command(name='dictionary', description="Urban Dictionary will send you the meaning of that!")
    async def urban(self, interaction: discord.Interaction, term: str):

        url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
        querystring = {"term": term}
        headers = {"X-RapidAPI-Key": rapid_api(), "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"}

        r = requests.get(url, headers=headers, params=querystring)
        data = r.json()
        result = data['list'][0]['definition']

        await interaction.response.send_message(f"The meaning of **{term}** is: \n ```{result}```")

    # Currency Converter
    @app_commands.command(name='currency', description="I Will convert a currency to another! ex: USD to GBP")
    async def currency(self, interaction: discord.Interaction, currency1: str, amount: float, currency2: str):

        r = requests.get(f"https://v6.exchangerate-api.com/v6/{exrate_api()}/pair/{currency1}/{currency2}/{amount}")
        data = r.json()
        value = data['conversion_result']

        await interaction.response.send_message(f"Looks like {amount} {currency1.upper()} is worth {value} {currency2.upper()} at the moment!")


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Search(yume))
