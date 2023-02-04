import discord
import re
import string
import os
try:
    from pygelbooru import Gelbooru
except ImportError:
    os.system('pip install pygelbooru')
    from pygelbooru import Gelbooru

from discord.ext import commands

class nsfw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gelbooru(self, ctx, *, tags):
        await ctx.message.delete()
        tagsnew = re.sub('[' + string.punctuation + ']', '', tags).split()
        gelbooru = Gelbooru(
            '&api_key=571aee667df493a3acb132a79fe89642e a7d189a14dd43a07b5538c57731ffea&user_id=904295', '904295')
        res = await gelbooru.random_post(tags=tagsnew)
        if res is None:
            await ctx.send(f"There were no results for '{tags}'", delete_after=5)
        else:
            await ctx.send(str(res))

def setup(bot):
    bot.add_cog(nsfw(bot))
    print("nsfw loaded successfully")