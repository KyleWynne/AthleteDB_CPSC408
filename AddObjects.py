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

    def __del__(self):
        del self.cur_obj
        self.conn.close()

    def execute_insert(self, query):
        self.cur_obj.execute(query)
        self.conn.commit()
    
    def query_returnOne(self, query):
        self.cur_obj.execute(query)
        return self.cur_obj.fetchone()[0]

    def Insert_Athlete(self, name, salary, age, sport, trophies, teamID):
        if teamID != "1":
            teamID = self.findID(2, teamID)

        if teamID == "invalid input":
            return teamID
        else:
            teamID = str(teamID)
            query = "INSERT INTO players VALUES(NULL,\'"+name+"\', \'"+salary+"\', \'"+age+"\', \'"+sport+"\', \'"+trophies+"\', \'"+teamID+"\');"
            self.execute_insert(query)
    
    def Insert_Team(self, name, leagueID, trophies):
        leagueID = self.findID(5, leagueID)
        if leagueID == "invalid input":
            return leagueID
        else:
            leagueID = str(leagueID)
            query = "INSERT INTO teams VALUES(NULL,\'"+name+"\', \'"+leagueID+"\', \'"+trophies+"\');"
            self.execute_insert(query)
    
    def Insert_League(self, name, sport, country):
        query = "INSERT INTO leagues VALUES(NULL,\'"+name+"\', \'"+sport+"\', \'"+country+"\');"
        self.execute_insert(query)
    
    def Insert_Game(self, teamID1, teamID2, team1_score, team2_score, outcome):
        teamID1 = self.findID(2, teamID1)
        teamID2 = self.findID(2, teamID2)
        if teamID1 == "invalid input":
            return teamID1
        elif teamID2 == "invalid input":
            return teamID2
        else:
            teamID1 = str(teamID1)
            teamID2 = str(teamID2)
            query = "INSERT INTO games VALUES(NULL, \'"+teamID1+"\', \'"+teamID2+"\', \'"+team1_score+"\', \'"+team2_score+"\', \'"+outcome+"\');"
            self.execute_insert(query)
        
    def Insert_Award(self, name, league_id, player_id, teamID, year):
        if league_id != "1":
            league_id = self.findID(5, league_id)
        if player_id != "1":
            player_id = self.findID(1, player_id)
        if teamID != "1":
            teamID = self.findID(2, teamID)
        
        if league_id == "invalid input":
            return league_id
        elif player_id == "invalid input":
            return player_id
        elif teamID == "invalid input":
            return teamID
        else:
            league_id = str(league_id)
            teamID == str(teamID)
            player_id = str(player_id)
            query = "INSERT INTO trophies VALUES(NULL,\'"+name+"\', \'"+league_id+"\', \'"+year+"\', \'"+player_id+"\', \'"+teamID+"\');"
            self.execute_insert(query)
    
    def delete_tuple(self, table, id, id2):
        num = int(table)
        try:
            if num == 1:
                id = self.findID(1, id)
                if id == "invalid input":
                    return "invalid input"

                else: 
                    query = """
                    DELETE FROM players
                    WHERE playerID = """ + str(id) + ";"

                    self.execute_insert(query)

            if num == 2:
                id = self.findID(2, id)
                if id == "invalid input":
                    return "invalid input"

                else:
                    query = """
                    UPDATE players
                    SET teamID = 1
                    WHERE teamID = """ + str(id) + ";"
                    
                    query2 = """ DELETE FROM teams
                    WHERE teamID = """ + str(id) + ";"
                    
                    self.execute_insert("START TRANSACTION;")
                    self.execute_insert(query)
                    self.execute_insert(query2)
                    self.execute_insert("COMMIT;")

            if num == 3:
                id = self.findID(2, id)
                id2 = self.findID(2, id2)
                if id == "invalid input":
                    return "invalid input"
                elif id2 == "invalid input":
                    return "invalid input"

                else:
                    query = """
                    DELETE FROM games
                    WHERE gameID = """ + str(id) + ";"

                    self.execute_insert(query)
            if num == 4:
                id = self.findID(4, id)
                if id == "invalid input":
                    return "invalid input"
                else:
                    query = """
                    DELETE FROM trophies
                    WHERE trophyID = """ + str(id) + ";"

                    self.execute_insert(query)

        except TypeError:
            pass

    def findID(self, a, curr_name):
        name = curr_name
        num = a
        while True:
            
            try:
                if num == 1:
                    query = """
                    SELECT playerID
                    FROM players 
                    WHERE player_name =  '""" + name + "'""""
                    LIMIT 1;"""
                if num == 2:
                    query = """
                    SELECT teamID
                    FROM teams 
                    WHERE team_name = \'""" + name + "\'""""
                    LIMIT 1;"""
                if num == 3:
                    print("DNE")
                if num == 4:
                    query = """
                    SELECT trophyID
                    FROM trophies 
                    WHERE trophy_name = '""" + name + "'""""
                    LIMIT 1;"""
                if num == 5:
                    query = """
                    SELECT leagueID
                    FROM leagues 
                    WHERE league_name = '""" + name + "'""""
                    LIMIT 1;"""
                tester = self.query_returnOne(query)
                tester = str(tester)
                return tester

            except TypeError:
                return "invalid input"
    
    def update_records(self, opt, num, value, old, old2): # updates record(s)

        tuple = self.find_table_tuple(opt, old, old2)
        id = str(tuple[0][0])
        if opt == 1:
            if num == 1:
                att = "player_name"
            if num == 2:
                att = "salary"
            if num == 3:
                att = "age"
            if num == 4:
                att = "sport"
            if num == 5:
                att = "trophies"
            if num == 6:
                att = "teamID"
                value = self.findID(2,value)

            query = '''
            UPDATE players 
            SET ''' + att + " = '" + str(value) + ''''
            WHERE playerID = ''' + str(id) + ";"
        if opt == 2:
            if num == 1:
                att = "team_name"
            if num == 2:
                att = "trophies"
            query = """
            UPDATE teams 
            SET """ + att + " = '" + str(value) + """'
            WHERE teamID = """ + str(id) + ";"
        if opt == 3:
            if num == 1:
                att = "team1_score"
            if num == 2:
                att = "team2_score"
            if num == 3:
                att = "outcome"
            query = '''
            UPDATE games 
            SET ''' + att + " = '" + str(value) + """'
            WHERE gameID = """ + str(id) + ";"
        if opt == 4:
            if num == 1:
                att = "player_winner_id"
                value = self.findID(1,value)
                query1 = '''
                UPDATE trophies 
                SET ''' + att + " = '" + str(value) + """'
                WHERE trophyID = """ + str(id) + ";"

                query2 = """UPDATE players
                SET trophies = trophies + 1
                WHERE playerID = """ + str(value) + """;"""
            if num == 2:
                att = "team_winner_id"
                value = self.findID(2,value)
                query1 = '''
                UPDATE trophies 
                SET ''' + att + " = " + str(value) + '''
                WHERE trophyID = ''' + str(id) + ";"

                query2 = """UPDATE teams
                SET trophies = trophies + 1
                WHERE teamID = """ + str(value) + """;"""
        
            self.execute_insert("START TRANSACTION;")
            self.execute_insert(query1)
            self.execute_insert(query2)
            self.execute_insert("COMMIT;")

        else:

            self.execute_insert(query)

    def find_table_tuple(self, num, name, name2):
        num = num
        if num == 1:
            id = self.findID(1, name)
            id = str(id)
            query = '''
            SELECT *
            FROM players
            Where PlayerID = ''' + id + ";"
        if num == 2:
            id = self.findID(2, name)
            id = str(id)
            query = '''
            SELECT *
            FROM teams
            Where teamID = ''' + id + ";"
        if num == 3:
            id = self.FindGameID(name, name2)
            id = str(id)
            query = '''
            SELECT *
            FROM games
            Where gameID = ''' + id + ";"
        if num == 4:
            id = self.findID(4, name)
            id = str(id)
            query = '''
            SELECT *
            FROM trophies
            Where trophyID = ''' + id + ";"           
        if num == 5:
            id = self.findID(5, name)
            id = str(id)
            query = '''
            SELECT *
            FROM leagues
            Where leagueID = ''' + id + ";"       
        self.cur_obj.execute(query)
        return self.cur_obj.fetchall()
    
    def FindGameID(self, Teamname1, Teamname2):
        teamID1 = self.findID(2, Teamname1)
        teamID2 = self.findID(2, Teamname2)
        if teamID1 == "invalid input":
            return teamID1
        elif teamID2 == "invalid input":
            return teamID2
        else:
            teamID1 = str(teamID1)
            teamID2 = str(teamID2)
            query = ''' 
            SELECT gameID
            FROM games
            WHERE ('''+teamID1+''' OR '''+teamID2+''' = 4)
            AND ('''+teamID1+''' OR '''+teamID2+''' = 3);'''
            return self.query_returnOne(query)