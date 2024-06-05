# Bibliotecas Utilizadas
import discord


class GitEmbed:

    git_embed = discord.Embed(description='You can use the buttons located at the bottom of the embed to choose what '
                                          'you want to see about me~', color=discord.Color.fuchsia())
    git_embed.set_author(name="Yume's GitHub Info.")
    git_embed.set_image(url="https://cdn.discordapp.com/avatars/944414497966264321/20feb089532248f4665cea9b10b61d81."
                        "png?size=4096")
    git_embed.set_footer(text="Yes, it's AI generated, please don't mind it.")


class GenericEmbed:

    embed = discord.Embed(color=discord.Color.random())

