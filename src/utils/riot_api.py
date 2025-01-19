import requests
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
api_key = os.getenv("api_key")
# print(api_key)
def get_puuid(username: str, tag_line: str, region: str="americas") -> str:
    
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{username}/{tag_line}"
    headers = {"X-Riot-Token": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("puuid")
    
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    


def get_summoner_id(puuid: str, region: str) -> str:
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/{puuid}"
    headers = {"X-Riot-Token": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json().get("id")
    
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def get_ranked_stats(summoner_id: str, region: str) -> str:
    url = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
    headers = {"X-Riot-Token": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
    

# username = "BELLA CIAOOOOO"
# tag_line = "NA1"
# region = "americas"

# puuid = get_puuid(username, tag_line, region)
# print(puuid)
# summoner_id = get_summoner_id(puuid, "NA1")
# print(summoner_id)
# ranked_stats = get_ranked_stats(summoner_id, "NA1")
# print("Ranked Stats:")
# for queue in ranked_stats:
#     print(f"- Queue: {queue['queueType']}")
#     print(f" Tier: {queue['tier']} {queue['rank']} ({queue['leaguePoints']} LP)")
#     winrate = round(int(queue['wins'])/(int(queue['losses'])+  int(queue['wins'])) * 100, 2)
#     print(f" Winrate: {winrate}%") 