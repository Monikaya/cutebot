import discord

from discord.ext import commands


class admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def purge(self, ctx, amount):
        await ctx.message.delete()
        await ctx.channel.purge(limit=int(amount))
        try:
            await ctx.send(f"Deleted {amount} messages", delete_after=5)
        except Exception:
            pass

    @commands.command()
    async def clean(self, ctx, amount):
        await ctx.message.delete()
        await ctx.channel.purge(
            limit=int(amount), check=lambda m: m.author == self.bot.user
        )
        try:
            await ctx.send(f"Deleted {amount} messages", delete_after=5)
        except Exception:
            pass

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.kick(reason=reason)
        await ctx.send(f"{member} has been kicked", delete_after=5)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.message.delete()
        await member.ban(reason=reason)
        await ctx.send(f"{member} has been banned", delete_after=5)

    @commands.command()
    async def unban(self, ctx, *, member):
        await ctx.message.delete()
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} has been unbanned", delete_after=5)
                return


def setup(bot):
    bot.add_cog(admin(bot))
    print("utils loaded successfully")
