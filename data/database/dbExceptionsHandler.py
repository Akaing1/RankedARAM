import os
import logging

import mysql
import mysql.connector
from dotenv import load_dotenv

from exceptions.UserDoesNotExistError import UserDoesNotExistError
from exceptions.UserAlreadyExistsError import UserAlreadyExistsError

load_dotenv()
logger = logging.getLogger()


class DBExceptionsHandler:

    def __init__(self):

        self.__SELECT_NAME_EXISTS = "SELECT COUNT(1) FROM Player WHERE Name = '%s'"

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

    def checkIfUserExists(self, name):
        self.cursor.execute(self.__SELECT_NAME_EXISTS % name)
        flag = self.cursor.fetchall()
        if flag[0][0]:
            raise UserAlreadyExistsError(name)
        else:
            logger.info(f'User \'{name}\' does not exist in db')

    def checkIfUserDoesNotExist(self, name):
        self.cursor.execute(self.__SELECT_NAME_EXISTS % name)
        flag = self.cursor.fetchall()
        if not flag[0][0]:
            raise UserDoesNotExistError(name)
        else:
            logger.info(f'User \'{name}\' exists in db')
