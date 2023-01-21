import discord

from discord.ext import commands

class utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge(self, ctx, amount):
        await ctx.message.delete()
        await ctx.channel.purge(limit=int(amount))
        await ctx.send(f"Deleted {amount} messages", delete_after=5)

    @commands.command()
    async def clean(self,ctx, amount):
        print("NOT IMPLEMENTED YET :D")

def setup(bot):
    bot.add_cog(utils(bot))
    print("utils loaded successfully")