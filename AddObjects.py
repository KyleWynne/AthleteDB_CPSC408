import mysql.connector
from helper import helper
import re
import string
from datetime import date

class AddObjects:

    def __init__(self):

    #connect to mysql
        self.conn = mysql.connector.connect(host="localhost",
                                user="root",
                                password="cpsc408!",
                                auth_plugin='mysql_native_password',
                                database="Athlete")

        self.cur_obj = self.conn.cursor()

    def execute_insert(self, query):
        self.cur_obj.execute(query)
        self.conn.commit()

    def Insert_Athlete(self, name, salary, age, sport, trophies, teamID):
        query = "INSERT INTO players VALUES(NULL,\'"+name+"\', \'"+salary+"\', \'"+age+"\', \'"+sport+"\', \'"+trophies+"\', \'"+teamID+"\');"
        self.execute_insert(query)
    
    def Insert_Team(self, name, leagueID, trophies):
        query = "INSERT INTO teams VALUES(NULL,\'"+name+"\', \'"+leagueID+"\', \'"+trophies+"\');"
        self.execute_insert(query)
    
    def Insert_League(self, name, sport, country):
        query = "INSERT INTO leagues VALUES(NULL,\'"+name+"\', \'"+sport+"\', \'"+country+"\');"
        self.execute_insert(query)
    
    def Insert_Game(self, teamID1, teamID2, team1_score, team2_score, outcome):
        query = "INSERT INTO games VALUES(NULL, \'"+teamID1+"\', \'"+teamID2+"\', \'"+team1_score+"\', \'"+team2_score+"\', \'"+outcome+"\');"
        self.execute_insert(query)
    
    def Insert_Award(self, name, league_id, player_id, teamID, year):
        query = "INSERT INTO trophies VALUES(NULL,\'"+name+"\', \'"+league_id+"\', \'"+year+"\', \'"+player_id+"\', \'"+teamID+"\');"
        self.execute_insert(query)
