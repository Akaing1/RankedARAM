import requests
import os
from dotenv import load_dotenv
from data.riotData.PlayerData import PlayerData

load_dotenv()


class MatchData:

    def __init__(self):

        self.__FETCH_MATCH_HISTORY_DATA = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/%s/ids?start=0&count=10&api_key='
        self.__FETCH_MATCH_DATA = 'https://americas.api.riotgames.com/lol/match/v5/matches/%s?api_key='

        self.__playerData = PlayerData()

        self.__API_KEY = os.getenv('RIOT_API_KEY')

    def getMatchHistory(self, riotID) -> list:
        puuid = self.__playerData.getPuuid(riotID)
        req = self.__FETCH_MATCH_HISTORY_DATA % puuid
        response = requests.get(req + self.__API_KEY)
        return response.json()

    def getMatchData(self, matchID):
        req = self.__FETCH_MATCH_DATA % matchID
        response = requests.get(req + self.__API_KEY)
        return response.json()

    def checkIfMatchWon(self, response, riotID):
        puuid = self.__playerData.getPuuid(riotID)
        for players in response.get("info").get("participants"):
            if puuid in str(players):
                return players.get("win")
        return False
