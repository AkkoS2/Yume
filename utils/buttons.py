# Bibliotecas utilizadas neste arquivo
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


class ActionButtons:
    smug_button = Button(label="Smug back", style=discord.ButtonStyle.blurple, emoji="")
    stare_button = Button(label="Start staring", style=discord.ButtonStyle.blurple, emoji="")
    party_button = Button(label="Join party", style=discord.ButtonStyle.blurple, emoji="")
    leave_button = Button(label="Leave party", style=discord.ButtonStyle.blurple, emoji="")
    respect_button = Button(label="Pay respects", style=discord.ButtonStyle.blurple, emoji="")
    arrest_button = Button(label="Arrest them", style=discord.ButtonStyle.blurple, emoji="")
    dance_button = Button(label="Dance together", style=discord.ButtonStyle.blurple, emoji="")
    sigh_button = Button(label="Sigh...", style=discord.ButtonStyle.blurple, emoji="")
    laugh_button = Button(label="Laugh back", style=discord.ButtonStyle.blurple, emoji="")
    pout_button = Button(label="Pout too", style=discord.ButtonStyle.blurple, emoji="")
    purr_button = Button(label="Act like a kitty too", style=discord.ButtonStyle.blurple, emoji="")
    shrug_button = Button(label="Shrug back", style=discord.ButtonStyle.blurple, emoji="")
    smile_button = Button(label="Smile too", style=discord.ButtonStyle.blurple, emoji="")
    hmph_button = Button(label="Hmph!!!", style=discord.ButtonStyle.blurple, emoji="")
    hug_button = Button(label="Comfort them", style=discord.ButtonStyle.blurple, emoji="")
    shy_button = Button(label="I'm also blushy...", style=discord.ButtonStyle.blurple, emoji="")
    bribe_button = Button(label="Try giving them a bribe", style=discord.ButtonStyle.blurple, emoji="")
    sad_button = Button(label="So sad...", style=discord.ButtonStyle.blurple, emoji="")
    wave_button = Button(label="Wave to them", style=discord.ButtonStyle.blurple, emoji="")

    view_smug = View()
    view_smug.add_item(smug_button)
    view_smug.add_item(stare_button)

    view_party = View()
    view_party.add_item(party_button)
    view_party.add_item(leave_button)
    view_party.add_item(stare_button)
