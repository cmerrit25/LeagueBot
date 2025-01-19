# This example requires the 'message_content' intent.
from utils.riot_api import get_puuid, get_summoner_id, get_ranked_stats
#from discord.ext import commands
from utils.data_formatter import format_ranked_stats
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logger = logging.getLogger(__name__)

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

description = """This is a LOL stats bot. 

Commands span from fetching and displaying player stats to displaying a server leaderboard."""

command_prefix = "?"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix, description=description, intents=intents)

#reference https://github.com/Rapptz/discord.py/blob/v2.4.0/examples/basic_bot.py for commands extension library implementation
#need to place commands for stats into stats.py file for better readability and modularity
#after making bot functional in server branch off to add functionality and merge back once finished with each command

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name="greet")
async def on_message(ctx):

    await ctx.send('Hello!')

#need to update to client.command
@bot.command(name="stats")
async def fetch_player_stats(ctx):
    logging.basicConfig(filename="error.log", level=logging.INFO)

    await ctx.send("Please enter a username:")
    username = (await bot.wait_for("message")).content

    await ctx.send("Please enter a tagline:")
    tag_line = (await bot.wait_for("message")).content

    await ctx.send("Please enter a region:")
    region = (await bot.wait_for("message")).content

    puuid = get_puuid(username, tag_line, region)
    logger.info(puuid)
    if region == "americas":
        region = "NA1"
    summoner_id = get_summoner_id(puuid, region)
    logger.info(summoner_id)
    ranked_stats = get_ranked_stats(summoner_id, region)
    output = format_ranked_stats(ranked_stats)
    
    await ctx.send(f"{username}'s ranked stats:")
    await ctx.message.channel.send(output)

bot.run(DISCORD_TOKEN)
