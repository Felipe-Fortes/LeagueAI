from dotenv import load_dotenv
import os
import requests

load_dotenv()

gameName = input("Enter the game name: ")
tagLine = input("Enter the tag line(Without the #): ")
api_key = os.getenv("api_key")
if not api_key:
    raise ValueError("API key not found. Please set the 'api_key' in your .env file.")
api_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/%s/%s" % (gameName, tagLine)
api_url = api_url + "?api_key=" + api_key

request = requests.get(api_url)
puuid = request.json().get("puuid")


# Função pra obter o summoner
def get_summoner():
    if request.status_code == 200:
        print("Request was successful!")
        summoner_url = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/%s" % puuid
        summoner_url = summoner_url + "?api_key=" + api_key
        summoner_request = requests.get(summoner_url)
        data = summoner_request.json()
        print(data)
    else:
        print(f"Request failed with status code: {request.status_code}")
        print("Response content:", request.text)

def get_summoner_matches():
    if request.status_code == 200:
        print("Request was successful!")
        match_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/%s/ids" % puuid
        match_url = match_url + "?start=0&count=20&api_key=" + api_key
        match_request = requests.get(match_url)
        data = match_request.json()
        print(data)
    else:
        print(f"Request failed with status code: {request.status_code}")
        print("Response content:", request.text)


def get_last_match():
    if request.status_code == 200:
        print("Request was successful!")
        match_url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/%s/ids" % puuid
        match_url = match_url + "?start=0&count=1&api_key=" + api_key
        match_request = requests.get(match_url)
        data = match_request.json()
        print(data)
    else:
        print(f"Request failed with status code: {request.status_code}")
        print("Response content:", request.text)

def get_last_match_players():
    if request.status_code == 200:
        print("Request was successful!")
        match_url = "https://americas.api.riotgames.com/lol/match/v5/matches/BR1_3108236037"
        match_url = match_url + "?api_key=" + api_key
        match_request = requests.get(match_url)
        data = match_request.json().get("info", {}).get("participants", [])
        for player in data:
            print(f"Summoner Name: {player.get('summonerName')}, Champion: {player.get('championName')}, Kills: {player.get('kills')}, Deaths: {player.get('deaths')}, Assists: {player.get('assists')}")
    else:
        print(f"Request failed with status code: {request.status_code}")
        print("Response content:", request.text)

get_last_match_players()