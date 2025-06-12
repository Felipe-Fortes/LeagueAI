import requests

gameName = input("Enter the game name: ")
tagLine = input("Enter the tag line(Without the #): ")
api_key = "RGAPI-137c5a19-6e44-4f0a-b46f-cb7184327f7f"
api_url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/%s/%s" % (gameName, tagLine)
api_url = api_url + "?api_key=" + api_key


request = requests.get(api_url)
if request.status_code == 200:
    print("Request was successful!")
    data = request.json()
    print(data)
else:
    print(f"Request failed with status code: {request.status_code}")
    print("Response content:", request.text)