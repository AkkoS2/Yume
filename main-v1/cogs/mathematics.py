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
            await interaction.response.send_message(f"Looks like this number doesn't have a square root", ephemeral=True)

    # inverse square root
    @app_commands.command(name='inv-square-root', description="Just a Quake thingie, don't mind it~")
    async def invsqrt(self, interaction: discord.Interaction, *, number: float):

        try:
            if number <= 0:
                await interaction.response.send_message(f"Can you use a positive number? please and thank you!", ephemeral=True)

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
    @app_commands.command(name='linear-equation', description="I will calculate it with the values of your choice!")
    async def first_degree(self, interaction: discord.Interaction, *, a: float, b: float):

        if a == 0:
            await interaction.response.send_message(f"The value of A is zero, so it doesn't have a solution, try again!", ephemeral=True)

        x = -b / a
        await interaction.response.send_message(f"The value of X is: {x:.2f}")

    # equação de segundo grau
    @app_commands.command(name='quadratic-equation', description="I will calculate it with the values of your choice!")
    async def second_degree(self, interaction: discord.Interaction, *, a: float, b: float, c: float):

        if a == 0:
            await interaction.response.send_message("The value of A is zero, let's try another value, okay?", ephemeral=True)

        delta = b ** 2 - 4 * a * c

        if delta < 0:
            await interaction.response.send_message("Looks like the Delta value is negative, so it doesn't have a real solution.", ephemeral=True)

        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        await interaction.response.send_message(f"Yume thinks that the result of this equation is: X1: {x1:.2f} and X2: {x2:.2f}")

    # equação de terceiro grau
    @app_commands.command(name='cubic-equation', description="I will calculate it with the values of your choice!")
    async def third_degree(self, interaction: discord.Interaction, *, a: float, b: float, c: float, d: float):

        if a == 0:
            await interaction.response.send_message("Hmm... the value of A is zero, i need another value to do that.", ephemeral=True)

        delta = (b ** 2) - (3 * a * c) + (9 * a * d)
        delta_0 = (2 * b ** 3) - (9 * a * b * c) + (27 * a ** 2 * d)

        if delta < 0 or delta_0 < 0:
            await interaction.response.send_message("Oh no, Delta value is negative, let's try again?", ephemeral=True)

        if delta == 0:
            x = (-b + math.cbrt(delta_0)) / (3 * a)
            await interaction.response.send_message(f"Yume found the root of the equation, and it is: {x:.2f}")

        else:
            x1 = (-b + math.sqrt(delta) + math.cbrt(delta_0)) / (3 * a)
            x2 = (-b - math.sqrt(delta) + math.cbrt(delta_0)) / (3 * a)
            x3 = (-b + math.sqrt(delta) - math.cbrt(delta_0)) / (3 * a)

            await interaction.response.send_message(f"The results of this equation are: X1: {x1:.2f}, X2: {x2:.2f} and X3: {x3:.2f}")


# registra a classe cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Mathematics(yume))
