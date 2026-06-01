# bibliotecas
from utils.hembed import HelpEmbed
from discord.ext import commands
from discord import app_commands
import discord


# realiza a criação da classe cog
class Help(commands.Cog):
    def __init__(self, yume: commands.AutoShardedBot):
        self.yume = yume

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help is Ready!!')

    # help
    @app_commands.choices(category=[
        discord.app_commands.Choice(name='Fun', value=1),
        discord.app_commands.Choice(name='Image', value=2),
        discord.app_commands.Choice(name='Moderation', value=3),
        discord.app_commands.Choice(name='NSFW', value=4),
        discord.app_commands.Choice(name='Roleplay', value=5),
        discord.app_commands.Choice(name='Actions', value=6),
        discord.app_commands.Choice(name='Search', value=7),
        discord.app_commands.Choice(name='Utility', value=8),
        discord.app_commands.Choice(name='Mathematics', value=9),
        discord.app_commands.Choice(name='Gambling', value=10),
        discord.app_commands.Choice(name='Economy', value=11),
        ])
    @app_commands.command(name='help', description='Need any help, cutie?')
    async def help(self, interaction: discord.Interaction, category: discord.app_commands.Choice[int], *, dm: bool):

        match category.value:
            case 1:
                if dm is True:
                    await interaction.user.send(embed=HelpEmbed.fun)
                    await interaction.response.send_message('Check your DM, cutie~', ephemeral=True)
                else:
                    await interaction.response.send_message(embed=HelpEmbed.fun, ephemeral=True)

            case 2:
                if dm is True:
                    await interaction.user.send(embed=HelpEmbed.image)
                    await interaction.response.send_message('Check your DM, cutie~', ephemeral=True)
                else:
                    await interaction.response.send_message(embed=HelpEmbed.image, ephemeral=True)

            case 3:
                if dm is True:
                    await interaction.user.send(embed=HelpEmbed.moderation)
                    await interaction.response.send_message('Check your DM, cutie~', ephemeral=True)
                else:
                    await interaction.response.send_message(embed=HelpEmbed.moderation, ephemeral=True)

            case 4:
                if dm is True:
                    await interaction.user.send(embed=HelpEmbed.nsfw)
                    await interaction.response.send_message('Check your DM, cutie~', ephemeral=True)
                else:
                    await interaction.response.send_message(embed=HelpEmbed.nsfw, ephemeral=True)

            case 5:
                if dm is True:
                    await interaction.user.send(embed=HelpEmbed.roleplay)
                    await interaction.response.send_message('Check your DM, cutie~', ephemeral=True)
                else:
                    await interaction.response.send_message(embed=HelpEmbed.roleplay, ephemeral=True)

            case 6:
                if dm is True:
                    await interaction.user.send(embed=HelpEmbed.actions)
                    await interaction.response.send_message('Check your DM, cutie~', ephemeral=True)
                else:
                    await interaction.response.send_message(embed=HelpEmbed.actions, ephemeral=True)

            case 7:
                if dm is True:
                    await interaction.user.send(embed=HelpEmbed.search)
                    await interaction.response.send_message('Check your DM, cutie~', ephemeral=True)
                else:
                    await interaction.response.send_message(embed=HelpEmbed.search, ephemeral=True)

            case 8:
                if dm is True:
                    await interaction.user.send(embed=HelpEmbed.utility)
                    await interaction.response.send_message('Check your DM, cutie~', ephemeral=True)
                else:
                    await interaction.response.send_message(embed=HelpEmbed.utility, ephemeral=True)

            case 9:
                if dm is True:
                    await interaction.user.send(embed=HelpEmbed.mathematics)
                    await interaction.response.send_message('Check your DM, cutie~', ephemeral=True)
                else:
                    await interaction.response.send_message(embed=HelpEmbed.mathematics, ephemeral=True)

            case 10:
                await interaction.response.send_message("There's nothing here, yet...", ephemeral=True)

            case 11:
                await interaction.response.send_message("There's nothing here, yet...", ephemeral=True)


# registra as classes no cog
async def setup(yume: commands.AutoShardedBot) -> None:
    await yume.add_cog(Help(yume))
