# bibliotecas
from discord.ext import commands
from helpers import searchers
import discord


# inicializa o cog
class RolePlay(commands.Cog):
    def __init__(self, saturn):
        self.saturn = saturn

    # avisa se a classe iniciou
    @commands.Cog.listener()
    async def on_ready(self):
        print('RolePlay is Ready!')

    # kiss
    @commands.command()
    async def kiss(self, ctx, user: discord.Member = None):

        searchers.gif = 'kiss'

        if user is None or user == ctx.author:
            await ctx.reply(f'Não tente fazer isso, beije outra pessoa!', mention_author=False)

        else:
            kiss = discord.Embed(color=discord.Colour.random(), description=f'**{ctx.author.mention} beijou {user.mention}!**')
            kiss.set_image(url=str(searchers.rp_search()))
            kiss.set_footer(text='Que bonitinho! 💕')
            await ctx.send(embed=kiss)

    # slap
    @commands.command()
    async def slap(self, ctx, user: discord.Member = None):

        searchers.gif = 'slap'

        if user is None:
            await ctx.reply('Onde você está tentando bater?', mention_author=False)

        elif user == ctx.author:
            slap = discord.Embed(color=discord.Colour.random(), description=f'**{ctx.author.mention} bateu em si mesmo!**')
            slap.set_image(url=str(searchers.rp_search()))
            slap.set_footer(text='Eu recomendo seriamente que procure um psicólogo.')
            await ctx.send(embed=slap)

        else:
            slap = discord.Embed(color=discord.Colour.random(), description=f'**{ctx.author.mention} bateu em {user.mention}!**')
            slap.set_image(url=str(searchers.rp_search()))
            slap.set_footer(text='Parece que doeu, você está bem?')
            await ctx.send(embed=slap)

    # arrest
    @commands.command()
    async def arrest(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime arrest'

        arrest = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=arrest)

    # hug
    @commands.command()
    async def hug(self, ctx, user: discord.Member = None):

        searchers.gif = 'hug'

        if user is None or user == ctx.author:
            await ctx.reply('Não faça isso, abrace outra pessoa!', mention_author=False)

        else:
            hug = discord.Embed(color=discord.Colour.random(), description=f'**{ctx.author.mention} abraçou {user.mention}!**')
            hug.set_image(url=str(searchers.rp_search()))
            hug.set_footer(text='Que fofinho! 💞')
            await ctx.send(embed=hug)

    # cuddle
    @commands.command()
    async def cuddle(self, ctx, user: discord.Member = None):

        searchers.gif = 'cuddle'

        if user is None or user == ctx.author:
            await ctx.reply('é vergonhoso ver você tentando fazer isso sozinho, por favor, pare.', mention_author=False)

        else:
            cuddle = discord.Embed(color=discord.Colour.random(), description=f'**{ctx.author.mention} {user.mention}!**')
            cuddle.set_image(url=str(searchers.rp_search()))
            cuddle.set_footer(text='adorável!')
            await ctx.send(embed=cuddle)

    # smug
    @commands.command()
    async def smug(self, ctx, user: discord.Member = None):

        searchers.gif = 'smug'

        smug = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=smug)

    # party
    @commands.command()
    async def party(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime party'

        party = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=party)

    # pat
    @commands.command()
    async def pat(self, ctx, user: discord.Member = None):

        searchers.gif = 'pat'

        if user is None or user == ctx.author:
            await ctx.reply('Dê carinho para outra pessoa ao invés de fazer isso.', mention_author=False)
        else:

            pat = discord.Embed(color=discord.Colour.random(), description=f'**{ctx.author.mention} fez carinho em {user.mention}!**')
            pat.set_image(url=str(searchers.rp_search()))
            pat.set_footer(text='Todo mundo gosta de ganhar carinho, não? 💞')
            await ctx.send(embed=pat)

    # ship
    @commands.command()
    async def ship(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        ship = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=ship)

    # kill license
    @commands.command()
    async def klicense(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        klicense = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=klicense)

    # marry
    @commands.command()
    async def marry(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        marry = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=marry)

    # divorce
    @commands.command()
    async def divorce(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        divorce = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=divorce)

    # bite
    @commands.command()
    async def bite(self, ctx, user: discord.Member = None):

        searchers.gif = 'bite'

        bite = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=bite)

    # clap
    @commands.command()
    async def clap(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime clap'

        clap = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=clap)

    # cry
    @commands.command()
    async def cry(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime cry'

        cry = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=cry)

    # dance
    @commands.command()
    async def dance(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime dance'

        dance = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=dance)

    # cringe
    @commands.command()
    async def cringe(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        cringe = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=cringe)

    # facepalm
    @commands.command()
    async def facepalm(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime facepalm'

        facepalm = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=facepalm)

    # glare
    @commands.command()
    async def glare(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime glare'

        glare = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=glare)

    # greet
    @commands.command()
    async def greet(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime greet'

        greet = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=greet)

    # high five
    @commands.command()
    async def hifi(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime high five'

        hifi = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=hifi)

    # laugh
    @commands.command()
    async def laugh(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime laugh'

        laugh = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=laugh)

    # lick
    @commands.command()
    async def lick(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime neck lick'

        if user is None or user == ctx.author:
            await ctx.reply('Tente lamber alguma pessoa!')

        else:
            lick = discord.Embed(color=discord.Colour.random(), description=f'**{ctx.author.mention} acabou de lamber {user.mention}**')
            lick.set_image(url=str(searchers.rp_search()))
            lick.set_footer(text='Será que ele gostou disso?')
            await ctx.send(embed=lick)

    # poke
    @commands.command()
    async def poke(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime poke'

        poke = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=poke)

    # pout
    @commands.command()
    async def pout(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime pout'

        pout = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=pout)

    # punch
    @commands.command()
    async def punch(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime punch'

        punch = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=punch)

    # cheer
    @commands.command()
    async def cheer(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime cheer'

        cheer = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=cheer)

    # purr
    @commands.command()
    async def purr(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        purr = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=purr)

    # run
    @commands.command()
    async def run(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime run'

        run = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=run)

    # sad
    @commands.command()
    async def sad(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime sad'

        sad = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=sad)

    # shoot
    @commands.command()
    async def shoot(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime shoot'

        shoot = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=shoot)

    # shrug
    @commands.command()
    async def shrug(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime shrug'

        shrug = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=shrug)

    # shy
    @commands.command()
    async def shy(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime shy'

        shy = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=shy)

    # smile
    @commands.command()
    async def smile(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime smile'

        smile = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=smile)

    # stare
    @commands.command()
    async def stare(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime stare'

        stare = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=stare)

    # stomp
    @commands.command()
    async def stomp(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime stomp'

        stomp = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=stomp)

    # die
    @commands.command()
    async def die(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime die'

        die = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=die)

    # wiggle
    @commands.command()
    async def wiggle(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        wiggle = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=wiggle)

    # wag
    @commands.command()
    async def wag(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        wag = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=wag)

    # marriage
    @commands.command()
    async def marriage(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        marriage = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=marriage)

    # accept marriage
    @commands.command()
    async def accept(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        accept = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=accept)

    # decline marriage
    @commands.command()
    async def decline(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        decline = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=decline)

    # inspire
    @commands.command()
    async def inspire(self, ctx, user: discord.Member = None):

        searchers.gif = ''

        inspire = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=inspire)

    # spank
    @commands.command()
    async def spank(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime spank'

        spank = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=spank)

    # boop
    @commands.command()
    async def boop(self, ctx, user: discord.Member = None):

        searchers.gif = 'anime boop'

        boop = discord.Embed(color=discord.Colour.random())
        await ctx.send(embed=boop)


# registra a classe no cogs
def setup(saturn):
    saturn.add_cog(RolePlay(saturn))
