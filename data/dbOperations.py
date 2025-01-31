import os
from dotenv import load_dotenv

load_dotenv()


class DBOperations:

    def __init__(self):
        self.dbURL = os.getenv('DB_URL')
        self.dbHost = os.getenv('DB_HOST')
        self.dbUser = os.getenv('DB_USERNAME')
        self.dbPassword = os.getenv('DB_PASSWORD')

    def registerUser(self):
        pass

    def removeUser(self):
        pass

    def getUserData(self):
        pass
