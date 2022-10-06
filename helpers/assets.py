# bibliotecas
from discord.ui import Button, View
import discord


class Buttons:

    next_button = Button(label='Next', style=discord.ButtonStyle.blurple)
    ok_button = Button(label='OK', style=discord.ButtonStyle.blurple)
    back_button = Button(label='Back', style=discord.ButtonStyle.blurple)
    random_button = Button(label='Random', style=discord.ButtonStyle.blurple)

    view = View()
    view.add_item(back_button)
    view.add_item(ok_button)
    view.add_item(next_button)
    view.add_item(random_button)