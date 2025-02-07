import os
import logging

import mysql
import mysql.connector
from dotenv import load_dotenv

from enums import RankEnum

from data.database.dbExceptionsHandler import *
from exceptions.UserDoesNotExistError import UserDoesNotExistError
from exceptions.UserAlreadyExistsError import UserAlreadyExistsError

exceptionHandler = DBExceptionsHandler()
load_dotenv()


class DBOperations:

    def __init__(self):

        self.__RANK = RankEnum.Rank
        self.__INSERT = "INSERT INTO Player (Name, RiotID, LP, UserRank, Division) VALUES (%s, %s, %s, %s, %s)"
        self.__DELETE = "DELETE FROM Player WHERE Name = '%s'"
        self.__UPDATE = "UPDATE Player SET LP = %s WHERE Name = '%s'"
        self.__SELECT = "SELECT * FROM Player WHERE Name = '%s'"
        self.__SELECT_RIOTID = "SELECT RiotID FROM Player WHERE Name = '%s'"

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

        val = (str(interaction.user), riotId, 0, self.__RANK.IRON.value, 4)

        try:
            exceptionHandler.checkIfUserExists(str(interaction.user))
            self.cursor.execute(self.__INSERT, val)
            self.db.commit()
            logger.info('User added successfully')
            return True
        except UserAlreadyExistsError as e:
            logger.error(e)
        return False

    def removeUser(self, interaction) -> bool:

        try:
            exceptionHandler.checkIfUserDoesNotExist(str(interaction.user))
            self.cursor.execute(self.__DELETE % str(interaction.user))
            self.db.commit()
            logger.info(f'{str(interaction.user)} has been removed')
            return True
        except UserDoesNotExistError as e:
            logging.error(e)
        return False

    def getUserData(self, interaction):

        try:
            exceptionHandler.checkIfUserDoesNotExist(str(interaction.user))
            self.cursor.execute(self.__SELECT % str(interaction.user))
            userData = self.cursor.fetchall()
            return userData
        except UserDoesNotExistError as e:
            logging.error(e)
        return 'No data found for user'

    def getRiotIDData(self, interaction):

        try:
            exceptionHandler.checkIfUserDoesNotExist(str(interaction.user))
            self.cursor.execute(self.__SELECT_RIOTID % str(interaction.user))
            userData = self.cursor.fetchall()
            return userData
        except UserDoesNotExistError as e:
            logging.error(e)
        return 'No data found for user'

    def getLP(self, user):
        try:
            exceptionHandler.checkIfUserDoesNotExist(user)
            self.cursor.execute(self.__SELECT % user)
            userData = self.cursor.fetchall()
            return userData[0][2]
        except UserDoesNotExistError as e:
            logging.error(e)
        return 'No data found for user'

    def updateLP(self, user, lp) -> bool:
        try:
            exceptionHandler.checkIfUserDoesNotExist(user)
            self.cursor.execute(self.__UPDATE % (lp, user))
            self.db.commit()
            print('finished updating user lp')
            return True
        except UserDoesNotExistError as e:
            logging.error(e)
        return False


