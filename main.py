import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
bot = commands.Bot(command_prefix="~", self_bot=True)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    if not os.getenv("BEARER_TOKEN"):
        bot.unload_extension("cogs.trolley")
        print("twitter cog disabled because BEARER_TOKEN is not set")


for cog in os.listdir("./cogs"):
    if cog.endswith(".py"):
        bot.load_extension(f"cogs.{cog[:-3]}")


@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send("pong")


bot.run(os.getenv("TOKEN"))
