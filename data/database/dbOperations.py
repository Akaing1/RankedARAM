import os

import mysql
import mysql.connector
from dotenv import load_dotenv

from enums import RankEnum
from exceptions.UserAlreadyExistsException import UserAlreadyExistsException

load_dotenv()


class DBOperations:
    RANK = RankEnum.Rank
    INSERT = "INSERT INTO Player (Name, RiotID, LP, UserRank) VALUES (%s, %s, %s, %s)"
    DELETE = "DELETE FROM Player WHERE Name = '%s'"
    SELECT = "SELECT * FROM Player WHERE Name = '%s'"

    def __init__(self):
        self.dbURL = os.getenv('DB_URL')
        self.dbHost = os.getenv('DB_HOST')
        self.dbUser = os.getenv('DB_USER')
        self.dbPassword = os.getenv('DB_PASSWORD')
        self.db = mysql.connector.connect(
            database=self.dbURL,
            host=self.dbHost,
            user=self.dbUser,
            password=self.dbPassword
        )
        self.cursor = self.db.cursor()

    def registerUser(self, interaction, riotId) -> bool:

        val = (str(interaction.user), riotId, 0, self.RANK.IRON.value)
        try:
            self.cursor.execute(self.INSERT, val)
            self.db.commit()
            return True
        except UserAlreadyExistsException:
            print('User already exists')
        return False

    def removeUser(self, interaction) -> bool:

        try:
            self.cursor.execute(self.DELETE % str(interaction.user))
            self.db.commit()
            return True
        except UserAlreadyExistsException:
            print('User does not exist')
        return False

    def getUserData(self, interaction):

        try:
            self.cursor.execute(self.SELECT % str(interaction.user))
            userData = self.cursor.fetchall()
            return userData
        except UserAlreadyExistsException:
            print('User does not exist')
        return 'No data found for user'

    def getLP(self, user):
        try:
            self.cursor.execute(self.SELECT % user)
            userData = self.cursor.fetchall()
            return userData[0][2]
        except UserAlreadyExistsException:
            print('User does not exist')
        return 'No data found for user'
