# Bibliotecas Utilizadas
from discord.ui import Button, View
import discord


class GitButtons:
    repo_button = Button(label="Repository", url='https://github.com/AkkoS2/Yume',
                         style=discord.ButtonStyle.link, emoji='<:github:1243404130651865098>')

    issue_button = Button(label="Open Issue", url='https://github.com/AkkoS2/Yume/issues',
                          style=discord.ButtonStyle.link, emoji='<:github:1243404130651865098>')

    commands_button = Button(label="Planned Commands", url='https://github.com/users/AkkoS2/projects/12',
                             style=discord.ButtonStyle.link, emoji='<:github:1243404130651865098>')

    view = View()
    view.add_item(repo_button)
    view.add_item(issue_button)
    view.add_item(commands_button)
