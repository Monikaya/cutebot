import discord
import tweepy
import os
import asyncio
import random

import urllib.request

from discord.ext import commands
from dotenv import load_dotenv


async def get_client():
    client = tweepy.Client(os.getenv("BEARER_TOKEN"), wait_on_rate_limit=True)
    return client


async def get_pages(client, tweets_per_page):
    pages = []

    for response in tweepy.Paginator(
        client.get_liked_tweets,
        id=os.getenv("USER_ID"),
        max_results=tweets_per_page,
        expansions="attachments.media_keys",
        media_fields="url",
    ):
        print(response)
        try:
            pages.append(response.includes["media"])
        except KeyError:
            continue
    return pages


async def format_pages(page):
    urls = []
    for tweet in page:
        urls.append(tweet.url)
    return urls


async def download_images(page):
    urls = await format_pages(page)

    os.makedirs("data/images", exist_ok=True)
    for url in urls:
        try:
            filename = url.split("/")[-1]
            filepath = os.path.join("data/images", filename)
            if os.path.exists(filepath):
                print(f"Skipping {filename} because it already exists")
                continue
            print(f"Downloading {filename}...")
            urllib.request.urlretrieve(url, filepath)
            print(f"Downloaded {filename}!")
        except Exception:
            print(f"Failed to download a file! Skipping...")
            continue


class trolley(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def updateimages(self, ctx):
        await ctx.message.delete()
        load_dotenv()
        tweets_per_page = 50
        client = await get_client()
        pages = await get_pages(client, tweets_per_page)
        tasks = [asyncio.create_task(download_images(page)) for page in pages]
        for task in tasks:
            await task
        await ctx.send("Successfully downloaded all images!")

    @commands.command()
    async def trolley(self, ctx):
        await ctx.message.delete()
        os.makedirs("data/images", exist_ok=True)
        try:
            image = random.choice(os.listdir("data/images"))
            await ctx.send(file=discord.File(os.path.join("data/images", image)))
        except IndexError:
            await ctx.send(
                "No images found! Please run updateimages or manually fill the image directory first."
            )
            return
        


def setup(bot):
    bot.add_cog(trolley(bot))
    print("trolley cog loaded")
