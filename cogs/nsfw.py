import discord
import re
import string
import os
import requests

from discord.ext import commands
from pygelbooru import Gelbooru

async def get_post(tags):
    print(tags)
    gelbooru = Gelbooru(
            '&api_key=571aee667df493a3acb132a79fe89642e a7d189a14dd43a07b5538c57731ffea&user_id=904295', '904295')
    res = await gelbooru.random_post(tags=tags)
    print(res)
    return res

class nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gelbooru(self, ctx, *, tags):
        await ctx.message.delete()
        tagsnew = re.sub('[' + string.punctuation + ']', '', tags).split()
        res = await get_post(tagsnew)
        if res is None:
            await ctx.send(f"There were no results for '{tags}'", delete_after=5)
        else:
            await ctx.send(str(res))

    @commands.command()
    async def booba(self, ctx):
        await ctx.message.delete()
        res = await get_post(['breasts'])
        await ctx.send(str(res))

def setup(bot):
    bot.add_cog(nsfw(bot))
    print("nsfw loaded successfully")