import discord
import requests

from discord.ext import commands

class cute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='hugs someone :D')
    async def hug(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()
        await ctx.send(res['url'])

    @commands.command(brief='pokes someone')
    async def poke(self, ctx, member: commands.MemberConverter):
        r = requests.get("https://nekos.life/api/v2/img/poke")
        res = r.json()
        await ctx.send(res['url'])

    @commands.command(brief='cuddle')
    async def cuddle(self, ctx, member: commands.MemberConverter):
        r = requests.get("https://nekos.life/api/v2/img/cuddle")
        res = r.json()
        await ctx.send(res['url'])

    @commands.command(brief='*pat*')
    async def pat(self, ctx, member: commands.MemberConverter):
        r = requests.get("https://nekos.life/api/v2/img/pat")
        res = r.json()
        await ctx.send(res['url'])

def setup(bot):
    bot.add_cog(cute(bot))
    print("cute loaded successfully")


