

def getLPFromDB(user, db) -> int:
    return db.getLP(user)


def getLPFromUser(ctx, db) -> str:
    return f'{ctx.author.mention}, you have {getLPFromDB(str(ctx.author), db)}LP'
