

def getLPFromDB(user, db) -> int:
    return db.getLP(user)


def getLPFromUser(interaction, db) -> str:
    return f'{interaction.user.mention}, you have {getLPFromDB(str(interaction.user), db)}LP'


def updateLPinDB(interaction, db, wins) -> bool:
    return db.updateLP(str(interaction.user), 15*wins)
