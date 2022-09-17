# bibliotecas
from discord.ext.commands import has_permissions
from helpers.envkeys import deepai_key
from discord.ext import commands
import requests
import discord
import random


# inicializa o cog
class Utility(commands.Cog):
    def __init__(self, saturn):
        self.saturn = saturn

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('Utility is Ready!')

    # ping
    @commands.command(aliases=['delay'])
    async def ping(self, ctx):

        ping = round(self.saturn.latency * 1000)

        if ping <= 100:
            await ctx.send(f'**{ping}ms**, não está nada mal!')

        else:
            await ctx.send(f'Eu estou com **{ping}ms**, acho que tem como ficar melhor.')

    # saturn
    @commands.command(aliases=['online'])
    async def saturn(self, ctx):
        await ctx.reply('como posso ajudar?', mention_author=False)

    # avatar
    @commands.command(aliases=['pfp'])
    async def avatar(self, ctx, *, user: discord.Member = None):

        pfp = discord.Embed(color=discord.Colour.random())

        if user is None:
            user = ctx.author
            pfp.set_author(name=f'Este é o seu avatar! Bonitinho, não?')
            pfp.set_image(url=user.avatar_url)
            await ctx.send(embed=pfp)

        else:
            pfp.set_author(name=f'Este é o avatar de {user.name}! O que achou?')
            pfp.set_image(url=user.avatar_url)
            await ctx.send(embed=pfp)

    # waifu2x
    @has_permissions(attach_files=True)
    @commands.command(aliases=['w2x'])
    async def waifu2x(self, ctx):

        attachment = ctx.message.attachments[0]
        image_url = attachment.url

        waifu = discord.Embed(color=discord.Colour.random(), description='**Sua imagem está sendo processada, espere!**')
        waifu2 = discord.Embed(color=discord.Colour.random(), description='**Aqui está a sua imagem!**')
        send = await ctx.reply(embed=waifu, mention_author=False)

        r = requests.post('https://api.deepai.org/api/waifu2x', data={'image': f'{image_url}'},
                          headers={'api-key': f'{deepai_key()}'})
        if r.status_code == 200:
            data = r.json()
            url = data['output_url']

            waifu2.set_image(url=url)
            waifu2.set_footer(text='Vou deletar a imagem em 10 minutos, lembre-se de salvar ela!')
            await send.edit(embed=waifu2, delete_after=600)

        else:
            await ctx.reply('Parece que algo deu errado com a API, desculpa! :c', mention_author=False)
            await self.saturn.delete_message(embed=send)

    # color generator
    @commands.command(aliases=['cor'])
    async def color(self, ctx):

        value_int = random.randint(0, 16777215)
        value_hex = str(hex(value_int))
        value_final = '#' + value_hex[2:]

        await ctx.send(f'Este é o hexadecimal da cor gerada! **{value_final}**')

    # password generator
    @commands.command(aliases=['senha'])
    async def password(self, ctx, *, optional=None):

        lower_case = 'abcdefghijklmnopqrstuvwxyz'
        upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        symbols = '~`!@#$%^&*()_-+={}[]|\/:;.,<>?¨'
        everything = lower_case + upper_case + numbers + symbols

        length = random.randint(8, 16)
        user = ctx.author
        new_password = "".join(random.sample(everything, length))

        if optional is None:
            await ctx.reply(f'Esta é a senha que eu montei para você! **{new_password}**')

        elif optional.lower() == 'dm':
            dm_password = f'Esta é a senha que eu montei para você! **{new_password}**'
            await user.send(dm_password)

    # colorize
    @commands.command(aliases=['colorir'])
    async def colorize(self, ctx):

        attachment = ctx.message.attachments[0]
        image_url = attachment.url

        color = discord.Embed(color=discord.Colour.random(), description='**Sua imagem está sendo processada, espere!**')
        color2 = discord.Embed(color=discord.Colour.random(), description='**Aqui está a sua imagem!**')
        send = await ctx.reply(embed=color, mention_author=False)

        r = requests.post('https://api.deepai.org/api/colorizer', data={'image': f'{image_url}'},
                          headers={'api-key': f'{deepai_key()}'})
        if r.status_code == 200:
            data = r.json()
            url = data['output_url']

            color2.set_image(url=url)
            color2.set_footer(text='Vou deletar a imagem em 10 minutos, lembre-se de salvar ela!')
            await send.edit(embed=color2, delete_after=600)

        else:
            await ctx.reply('Parece que algo deu errado com a API, desculpa! :c', mention_author=False)
            await self.saturn.delete_message(embed=send)

    # user info
    @commands.command(aliases=['uf'])
    async def userinfo(self, ctx, *, user: discord.Member = None):

        if user is None:
            user = ctx.author
        date = '%a, %d %b, %Y %I:%M %p'
        info = discord.Embed(description=user.display_name, color=discord.Colour.random())
        info.set_author(name=str(user), icon_url=user.avatar_url)
        info.set_thumbnail(url=user.avatar_url)
        info.add_field(name='Entrou no servidor: ', value=user.joined_at.strftime(date))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        info.add_field(name='Conta criada: ', value=user.created_at.strftime(date))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            info.add_field(name='Cargos [{}]'.format(len(user.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace('_', ' ').title() for p in user.guild_permissions if p[1]])
        info.add_field(name='Permissões: ', value=str(perm_string), inline=False)
        info.set_footer(text='ID: ' + str(user.id))
        await ctx.send(embed=info)

    @userinfo.error
    async def error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.reply('Erro')
        else:
            raise error


# registra a classe no cogs
def setup(saturn):
    saturn.add_cog(Utility(saturn))
