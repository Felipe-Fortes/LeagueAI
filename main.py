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
if request.status_code == 200:
    print("Request was successful!")
    puuid = request.json().get("puuid")
    summoner_url = "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/%s" % puuid
    summoner_url = summoner_url + "?api_key=" + api_key
    summoner_request = requests.get(summoner_url)
    data = summoner_request.json()
    print(data)
else:
    print(f"Request failed with status code: {request.status_code}")
    print("Response content:", request.text)