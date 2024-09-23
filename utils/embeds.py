# Bibliotecas utilizadas neste arquivo
import discord

# TEMP
txtlink = open('./texts/links.txt', 'r').readlines()
txtmoji = open('./texts/external_emojis.txt', 'r').readlines()
icon = txtlink[0]
gitpage = txtlink[1]
gitissue = txtlink[2]
gitidea = txtlink[3]
kofi = txtlink[4]
invlink = txtlink[5]
gitemoji = txtmoji[0].rstrip()
kofimoji = txtmoji[1].rstrip()
extemoji = txtmoji[2].rstrip()


class InfoEmbed:

    iembed = discord.Embed(description="Here you can find yume's useful links and other things in the future.", color=discord.Color.fuchsia())
    iembed.set_author(name="Welcome to Yume's Information Page!", icon_url=icon)

    iembed.add_field(name=f'{gitemoji}GitHub Links:',
                     value=f"{extemoji}[Repository]({gitpage})\n"
                           f"{extemoji}[Report Issues]({gitissue})\n"
                           f"{extemoji}[Development Progress]({gitidea})", inline=False)

    iembed.add_field(name=f"{kofimoji}Ko-Fi:", value=f"{extemoji}[In case you want to support Yume]({kofi})", inline=False)
    iembed.add_field(name="🔗 Support Server:", value="soon™", inline=False)
    iembed.add_field(name="🔗 Invite Link:", value=f"{extemoji}[Invite Page]({invlink})", inline=False)


class GenericEmbed:

    embed = discord.Embed(color=discord.Color.random())
