# bibliotecas
from discord.ext import commands
from discord import app_commands
import discord
import math


# realiza a criação da classe cog
class Mathematics(commands.GroupCog, name='math'):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume
        super().__init__()

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Mathematics is Ready!!')

    # adição
    @app_commands.command(name='addition', description='Do some basic addition math')
    async def add(self, interaction: discord.Interaction, *, number: int, number2: int):

        result = number + number2
        await interaction.response.send_message(f'I think the result is: {round(result)}')

    # subtração
    @app_commands.command(name='subtraction', description='Do some basic subtraction math')
    async def sub(self, interaction: discord.Interaction, *, number: int, number2: int):

        result = number - number2
        await interaction.response.send_message(f'I think the result is: {round(result)}')

    # divisão
    @app_commands.command(name='division', description='Do some basic division math')
    async def div(self, interaction: discord.Interaction, *, number: int, number2: int):

        result = number / number2
        await interaction.response.send_message(f'I think the result is: {round(result)}')

    # multiplicação
    @app_commands.command(name='multiplication', description='Do some basic multiplication math')
    async def multi(self, interaction: discord.Interaction, *, number: int, number2: int):

        result = number * number2
        await interaction.response.send_message(f'I think the result is: {round(result)}')

    # fatorial
    @app_commands.command(name='factorial', description='I will find the factorial of your chosen number')
    async def factorial(self, interaction: discord.Interaction, *, number: int):

        if number < 0:
            await interaction.response.send_message(f"I won't let you do this, use a positive number! :c", ephemeral=True)

        result = math.factorial(number)
        await interaction.response.send_message(f"I've done the maths and, the result is: {result}")

    # square root
    @app_commands.command(name='root', description='Gets you the square root of a real number!')
    async def root(self, interaction: discord.Interaction, *, number: int):

        try:
            if number < 0:
                await interaction.response.send_message(f"I'm only doing this with a positive number, okay?", ephemeral=True)

            result = math.sqrt(number)
            await interaction.response.send_message(f"I've done with the maths and the result is: {result}, i think?")

        except ValueError:
            await interaction.response.send_message(f"Looks like this number doesn't have a square root")


# registra a classe cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Mathematics(yume))
