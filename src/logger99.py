import discord      # gee i wonder
import json

from discord.ext import commands

    # JSON: Parse bot.json to Load Authorization Keys

    # JSON: Parse Data.json to load Organization Rules

    # JSON: Parse registry.json to load Users

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

    # Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Started Bot :3')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world!")

    # Start the bot using your bot token
bot.run(JSON_BOT_APIKEY)