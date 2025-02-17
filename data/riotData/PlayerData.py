import requests
import os
from dotenv import load_dotenv

load_dotenv()


class PlayerData:

    def __init__(self):

        self.__ACCOUNT_DATA_V1_BY_IGN = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/%s/%s?api_key='

        self.__API_KEY = os.getenv('RIOT_API_KEY')

    def checkRiotIDisValid(self, riotID) -> bool:
        componentID = (riotID[:riotID.index('#')], riotID[riotID.index('#') + 1:])
        req = self.__ACCOUNT_DATA_V1_BY_IGN % componentID
        if requests.get(req + self.__API_KEY).status_code == 200:
            return True
        return False

    def getPuuid(self, riotID) -> str:
        componentID = (riotID[:riotID.index('#')], riotID[riotID.index('#') + 1:])
        req = self.__ACCOUNT_DATA_V1_BY_IGN % componentID
        response = requests.get(req + self.__API_KEY)
        return response.json().get('puuid')
