from data.riotData.MatchData import *

matchData = MatchData()


def getLPFromDB(user, db) -> int:
    return db.getLP(user)


def getLPFromUser(interaction, db) -> str:
    return f'{interaction.user.mention}, you have {getLPFromDB(str(interaction.user), db)}LP'


def getWinsSinceLastCheck(riotId) -> int:
    return matchData.getNumberOfWins(riotId)


def updateLPinDB(interaction, db, wins) -> bool:
    return db.updateLP(str(interaction.user), getLPFromDB(interaction.user, db) + 15 * wins)
