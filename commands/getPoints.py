
def getLPfromDB(user) -> int:
    print(user)
    return 0


def getLPFromUser(ctx, db) -> str:
    return f'{ctx.author.mention}, you have {getLPfromDB(ctx.author)}LP'
