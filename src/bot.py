from commands.stats import fetch_player_stats
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

description = """This is a LOL stats bot. 

Commands span from fetching and displaying player stats to displaying a server leaderboard."""

command_prefix = "?"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix, description=description, intents=intents)


#need to place commands for stats into stats.py file for better readability and modularity
#after making bot functional in server branch off to add functionality and merge back once finished with each command

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name="greet")
async def on_message(ctx):
    await ctx.send('Hello!')

#currently dealing with a minor bug that causes the stats command to not work the first time
@bot.command(name="stats")
async def stats(ctx):
    await fetch_player_stats(ctx, bot)

bot.run(DISCORD_TOKEN)
