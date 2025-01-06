from config import api_key, api_url

import requests # import requests module

response = requests.get(api_url, headers={"X-Riot-Token": api_key}) # get request to api_url with api_key
player_info = (response.json())
player_accountID = player_info['accountId'] # get accountID from player_info

print(player_info) # prints ID, accountID, puuid, name, profileIconId, revisionDate, summonerLevel
print(player_accountID) # prints accountID