# bibliotecas
from discord.ext import commands
from discord import app_commands
import discord
import struct
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
    async def add(self, interaction: discord.Interaction, *, number: float, number2: float):

        result = number + number2
        await interaction.response.send_message(f'I think the result is: {result:.2f}')

    # subtração
    @app_commands.command(name='subtraction', description='Do some basic subtraction math')
    async def sub(self, interaction: discord.Interaction, *, number: float, number2: float):

        result = number - number2
        await interaction.response.send_message(f'I think the result is: {result:.2f}')

    # divisão
    @app_commands.command(name='division', description='Do some basic division math')
    async def div(self, interaction: discord.Interaction, *, number: float, number2: float):

        result = number / number2
        await interaction.response.send_message(f'I think the result is: {result:.2f}')

    # multiplicação
    @app_commands.command(name='multiplication', description='Do some basic multiplication math')
    async def multi(self, interaction: discord.Interaction, *, number: float, number2: float):

        result = number * number2
        await interaction.response.send_message(f'I think the result is: {result:.2f}')

    # fatorial
    @app_commands.command(name='factorial', description='I will find the factorial of your chosen number')
    async def factorial(self, interaction: discord.Interaction, *, number: int):

        if number < 0 or number > 100:
            await interaction.response.send_message(f"Let's try a different number, okay...?", ephemeral=True)

        result = math.factorial(number)
        await interaction.response.send_message(f"I've done the maths and, the result is: {result}")

    # square root
    @app_commands.command(name='square-root', description='Gets you the square root of a real number!')
    async def root(self, interaction: discord.Interaction, *, number: float):

        try:
            if number < 0 or number > 100:
                await interaction.response.send_message(f"I'm only doing this with a positive number, okay?", ephemeral=True)

            result = math.sqrt(number)
            await interaction.response.send_message(f"I've done with the maths and the result is: {result:.2f}, i think?")

        except ValueError:
            await interaction.response.send_message(f"Looks like this number doesn't have a square root")

    # inverse square root
    @app_commands.command(name='inv-square-root', description='An inverse square root... why not??')
    async def invsqrt(self, interaction: discord.Interaction, *, number: float):

        try:
            if number <= 0:
                await interaction.response.send_message(f"Can you use a positive number? please and thank you!")

            three_halfs = 1.5
            x2 = number * 0.5
            y = number

            y_packed = struct.pack('f', y)
            i = struct.unpack('i', y_packed)[0]
            i = 0x5f3759df - (i >> 1)

            i_packed = struct.pack('i', i)
            y = struct.unpack('f', i_packed)[0]
            y = y * (three_halfs - (x2 * y * y))

            result = y
            await interaction.response.send_message(f"The inverse square root of {number} is: {result:.2f}! Yume is smart, hehe~")

        except ValueError:
            await interaction.response.send_message(f"Something went wrong, I'm so sorry :c")

    # equação primeiro grau
    @app_commands.command(name='first-degree-equation', description="I will calculate it with the values of your choice!")
    async def first_degree(self, interaction: discord.Interaction, *, a: float, b: float):

        try:
            x = -b / a
            await interaction.response.send_message(f'The solution for this is: x = {x:.2f}')

        except ValueError:
            await interaction.response.send_message(f"Someting went wrong.... sorry.")

    # equação de segundo grau
    @app_commands.command(name='second-degree-equation', description="I will calculate it with the values of your choice!")
    async def second_degree(self, interaction: discord.Interaction, *, a: float, b: float, c: float):

        try:
            x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
            await interaction.response.send_message(f"The solution is: x1 = {x1:.2f} and x2 = {x2:.2f}")

        except ValueError:
            await interaction.response.send_message(f"Someting went wrong.... sorry.")


# registra a classe cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Mathematics(yume))
