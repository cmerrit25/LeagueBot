from utils.riot_api import get_puuid, get_summoner_id, get_ranked_stats
from utils.data_formatter import format_ranked_stats
import logging

logger = logging.getLogger(__name__)

async def fetch_player_stats(ctx, bot):
    logging.basicConfig(filename="error.log", level=logging.INFO)

    await ctx.send("Please enter a username:")
    username = (await bot.wait_for("message")).content

    await ctx.send("Please enter a tagline:")
    tag_line = (await bot.wait_for("message")).content

    await ctx.send("Please enter a region:")
    region = (await bot.wait_for("message")).content

    puuid = get_puuid(username, tag_line, region)
    logger.info(puuid)

    if not puuid:
        await ctx.send("Could not retrieve PUUID. Please check the inputs and try again.")
        return
    
    if region == "americas":
        region = "NA1"
    summoner_id = get_summoner_id(puuid, region)
    logger.info(summoner_id)

    if not summoner_id:
        await ctx.send("Could not retrieve Summoner ID. Please check the inputs and try again.")

    ranked_stats = get_ranked_stats(summoner_id, region)
    if not ranked_stats:
        await ctx.send("No ranked stats found. This user may not have played ranked games this season.")
        
    output = format_ranked_stats(ranked_stats)
    
    await ctx.send(f"{username}'s ranked stats:")
    await ctx.message.channel.send(output)