

def getLPFromDB(user, db) -> int:
    return db.getLP(user)


def getLPFromUser(interaction, db) -> str:
    return f'{interaction.user.mention}, you have {getLPFromDB(str(interaction.user), db)}LP'
