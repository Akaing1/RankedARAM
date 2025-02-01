import mysql.connector
from Enums import RankEnum
import os
from dotenv import load_dotenv

load_dotenv()

db = mysql.connector.connect(
    database=os.getenv('DB_URL'),
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD')
)

mycursor = db.cursor()

# sql = '''CREATE TABLE Player (
#                   Name varchar(100) NOT NULL,
#                   RiotID varchar(200) NOT NULL,
#                   LP smallint,
#                   UserRank varchar(50) NOT NULL,
#                   PRIMARY KEY (RiotID)
#                   )'''

insert = "INSERT INTO Player (Name, RiotID, LP, UserRank) VALUES (%s, %s, %s, %s)"
val = ("steohany", "steohany#ant", 50, RankEnum.Rank.DIAMOND.value)
delete = "DELETE FROM Player WHERE Name = 'steohany'"

# mycursor.execute(delete)
# db.commit()

# tables = mycursor.fetchall()
# print(tables)

mycursor.execute("SELECT * FROM Player")
myresult = mycursor.fetchall()
# print(myresult[1][2])
for x in myresult:
    print(x)
