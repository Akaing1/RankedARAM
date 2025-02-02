import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('RIOT_API_KEY')


class RiotData:
    def __init__(self):
        self.API_KEY = os.getenv('RIOT_API_KEY')

    def checkRiotIDisValid(self, riotID) -> bool:
        componentID = (riotID[:riotID.index('#')], riotID[riotID.index('#')+1:])
        req = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/%s/%s?api_key=' % componentID
        if requests.get(req + self.API_KEY).status_code == 200:
            return True
        return False
