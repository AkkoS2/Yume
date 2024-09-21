# Bibliotecas utilizadas neste arquivo
import discord


class GitEmbed:

    git_embed = discord.Embed(description='You can use the buttons located at the bottom of the embed to choose what '
                                          'you want to see about me~', color=discord.Color.fuchsia())
    git_embed.set_author(name="Yume's GitHub Info.")
    git_embed.set_image(url="https://cdn.discordapp.com/avatars/944414497966264321/20feb089532248f4665cea9b10b61d81."
                        "png?size=4096")
    git_embed.set_footer(text="Yes, it's AI generated, please don't mind it.")


class InfoEmbed:

    icon = "https://cdn.discordapp.com/avatars/944414497966264321/20feb089532248f4665cea9b10b61d81.png?size=1024"

    iembed = discord.Embed(description="Here you can find yume's useful links and other things in the future.", color=discord.Color.fuchsia())
    iembed.set_author(name="Welcome to Yume's Information Page!", icon_url=icon)
    iembed.add_field(name='<:github:1243404130651865098> GitHub Links:',
                     value="<:externallink:1286308168762134569> [Repository](https://github.com/AkkoS2/Yume)\n"
                           "<:externallink:1286308168762134569> [Report Issues](https://github.com/AkkoS2/Yume/issues)\n"
                           "<:externallink:1286308168762134569> [Development Progress](https://github.com/users/AkkoS2/projects/12)", inline=False)

    iembed.add_field(name="<:kofi:1286360498853380159> Ko-Fi:", value="<:externallink:1286308168762134569> [In case you want to support Yume](https://ko-fi.com/ninym)", inline=False)
    iembed.add_field(name="🔗 Support Server:", value="soon™", inline=False)

    iembed.add_field(name="🔗 Invite Link:",
                     value="<:externallink:1286308168762134569> "
                           "[Invite Page](https://discord.com/oauth2/authorize?client_id=944414497966264321&permissions=551903676480&integration_type=0&scope=bot)", inline=False)


class GenericEmbed:

    embed = discord.Embed(color=discord.Color.random())
