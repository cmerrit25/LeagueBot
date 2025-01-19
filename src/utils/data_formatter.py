def format_ranked_stats(ranked_stats):

    if not ranked_stats:
        print("No ranked stats available")

    formatted_stats = []
    for queue in ranked_stats:
        queue_type = "Solo/Duo" if queue["queueType"] == "RANKED_SOLO_5x5" else "Flex"
        tier = f"{queue['tier']} {queue['rank']} ({queue['leaguePoints']} LP)"
        win_rate = f"{queue['wins']}W / {queue['losses']}L"
        wr_perc = round(int(queue['wins'])/(int(queue['wins']) + int(queue['losses'])), 2) * 100
        win_rate_perc = f'{wr_perc}%'
        formatted_stats.append(f"- {queue_type}: {tier}, {win_rate}, {win_rate_perc}")

    return "\n".join(formatted_stats)