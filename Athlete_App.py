import mysql.connector
from helper import helper
import re
import string
from datetime import date

#connect to mysql
conn = mysql.connector.connect(host="localhost",
                               user="root",
                               password="database",
                               auth_plugin='mysql_native_password',
                               database="Athlete")

cur_obj = conn.cursor()

#execute DQL query, no changes made to DB but returns the total output
def execute_query(query):
    cur_obj.execute(query)
    return cur_obj.fetchall()

#Execute DQL query, no changes made to DB but returns only the first list item in the output
def query_returnOne(query):
    cur_obj.execute(query)
    return cur_obj.fetchone()[0]

#Execute DML query, commits changes to DB does not return anything
def execute_insert(query):
    cur_obj.execute(query)
    conn.commit()
    
def name_placeholder_query(self,query,dictionary): # executes a single query given a dictionary of variables
        self.cursor.execute(query,dictionary)
        results = self.cursor.fetchall()
        results = [i[0] for i in results]
        return results
    
def insert_variables(self,query, variables): # executes a single query only
        cur_obj.execute(query, variables)
        conn.commit()
        print("query executed")
        
def create_all_tables():
    query = """
    CREATE TABLE IF NOT EXISTS teams (
        teamID INT AUTO_INCREMENT PRIMARY KEY,
        team_name VARCHAR(30) NOT NULL,
        leagueID INT NOT NULL,
        trophies INT);"""
    execute_insert(query)
    query2 = """
    CREATE TABLE IF NOT EXISTS players (
        playerID INT AUTO_INCREMENT PRIMARY KEY,
        player_name VARCHAR(30) NOT NULL,
        salary INT,
        age INT,
        sport VARCHAR(30) NOT NULL,
        trophies INT,
        teamID INT NOT NULL FOREIGN KEY);"""
    execute_insert(query2)
    query3 = """
    CREATE TABLE IF NOT EXISTS games (
        gameID INT AUTO_INCREMENT PRIMARY KEY,
        team1ID INT NOT NULL FOREIGN KEY,
        team2ID INT NOT NULL FOREIGN KEY,
        team1_score INT NOT NULL,
        team2_score INT NOT NULL,
        outcome VARCHAR(30) NOT NULL);"""
    execute_insert(query3)  
    query4 = """
    CREATE TABLE IF NOT EXISTS leagues (
        leagueID INT AUTO_INCREMENT PRIMARY KEY,
        league_name VARCHAR(30) NOT NULL,
        sport VARCHAR(30) NOT NULL, 
        country VARCHAR(30));"""
    execute_insert(query4)
    query5 = """
    CREATE TABLE IF NOT EXISTS trophies (
        trophyID INT AUTO_INCREMENT PRIMARY KEY,
        trophy_name VARCHAR(30) NOT NULL,
        leagueID INT NOT NULL FOREIGN KEY,
        sport VARCHAR(30) NOT NULL,
        year YEAR,
        player_winner_id  INT NOT NULL FOREIGN KEY,
        team_winner_id INT NOT NULL FOREIGN KEY);"""
    execute_insert(query5)
        
def destructor(self): #commit changes and close connection
        self.connection.close()
        
def options(): # prints options for user to choose from
    print('''
    1. View all records in a table(teams, players, games, leagues, trophies)
    2. Query data with parameters/filters
    3. Delete record(s)
    4. Update record(s)
    5. Insert record(s)
    6. Generate a csv report
    7. Exit
    ''')
    return helper.get_choice([1,2,3,4,5,6,7])

def view_all_records(): # prints all records in a table
    #enforces joins accross at least 3 tables(player, trophy, team)
    query = """
    SELECT player.playerID, player.player_name, player.salary, player.age, player.sport, player.trophies, team.team_name, team.leagueID, team.trophies, game.gameID, game.team1ID, game.team2ID, game.team1_score, game.team2_score, game.outcome, league.leagueID, league.league_name, league.sport, league.country, trophy.trophyID, trophy.trophy_name, trophy.leagueID, trophy.sport, trophy.year, trophy.player_winner_id, trophy.team_winner_id
    FROM players player team team, games game, leagues league, trophies trophy
    INNER JOIN players ON player.teamID = team.teamID
    INNER JOIN trophies ON trophy.leagueID = league.leagueID;
    """
    cur_obj.execute(query)
    return cur_obj.fetchall()

def query_data(): # queries data with parameters/filters
    #use a subquery
    #use an aggregation/group by
    action = int(input("Enter 1 to query by player, 2 to query by team, 3 to query by game, 4 to query by league, 5 to query by trophy: "))
    if action == 1:
        player = input("Enter player name: ")
        query = """
        SELECT *
        FROM players
        WHERE player_name = """ + player + ";"
            
    if action == 2: 
        team = input("Enter team name: ")
        query = """
        SELECT * 
        FROM teams
        WHERE team_name = """ + team + ";"
    if action == 3: 
        game = input("Enter game ID: ")
        query = """
        SELECT *
        FROM games
        WHERE gameID = """ + game + ";"
    if action == 4: 
        league = input("Enter league name: ")
        query = """
        SELECT *
        FROM leagues
        WHERE league_name = """ + league + ";"
    if action == 5:
        trophy = input("Enter trophy name: ")
        query = """
        SELECT *
        FROM trophies
        WHERE trophy_name = """ + trophy + ";"
    cur_obj.execute(query)
    return cur_obj.fetchall()     

def delete_records(): # deletes record(s)
    pass

def update_options():
    print('''
    1. Update a player's information
    2. Update a Team's information
    3. Update a game's information
    4. Update a trophies information
    5. Exit
    ''')
    return helper.get_choice([1,2,3,4,5])

def find_table_tuple(num):
    num = num
    if num == 1:
        id = input("Enter player ID: ")
        query = '''
        SELECT *
        FROM players
        Where PlayerID = ''' + id + ";"
    if num == 2:
        id = input("Enter Team ID: ")
        query = '''
        SELECT *
        FROM teams
        Where teamID = ''' + id + ";"
    if num == 3:
        id = input("Enter game ID: ")
        query = '''
        SELECT *
        FROM games
        Where gameID = ''' + id + ";"
    if num == 4:
        id = input("Enter trophy ID: ")
        query = '''
        SELECT *
        FROM trophies
        Where trophyID = ''' + id + ";"           
    if num == 5:
        id = input("Enter League ID: ")
        query = '''
        SELECT *
        FROM leagues
        Where leagueID = ''' + id + ";"       
    cur_obj.execute(query)
    return cur_obj.fetchall()

def findID(a, curr_name):
    name = curr_name
    num = a
    if num == 1:
        query = '''
        SELECT playerID
        FROM players 
        WHERE player_name = ''' + name + ";"
    if num == 2:
        query = '''
        SELECT teamID
        FROM teams 
        WHERE team_name = ''' + name + ";"
    if num == 3:
        print("DNE")
    if num == 4:
        query = '''
        SELECT trophyID
        FROM trophies 
        WHERE trophy_name = ''' + name + ";"
    if num == 5:
        query = '''
        SELECT leagueID
        FROM leagues 
        WHERE league_name = ''' + name + ";"
#add try catch block??? how to account for input errors
    return query_returnOne(query)

def update_records(): # updates record(s)
    opt = update_options()
    tuple = find_table_tuple(opt)
    id = tuple[0]
    while True:
        if opt == 1:
            print("What would you like to change\n")
            print('''
            1. player Name
            2. yearly salary
            3. age in years
            4. sport
            5. number of trophies
            6. Team 
            ''')
            num = helper.get_choice[(1,2,3,4,5,6)]
            value = input("Enter new value: ")
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
                value = findID(2,value)
            query = '''
            UPDATE TABLE players 
            SET ''' + att + " = " + value + '''
            WHERE playerID = ''' + id + ";"
        if opt == 2:
            print("What would you like to change\n")
            print('''
            1. Team Name
            2. League
            3. number of trophies
            ''')
            num = helper.get_choice[(1,2,3,4,5,6)]
            value = input("Enter new value: ")
            if num == 1:
                att = "team_name"
            if num == 2:
                att = "leagueID"
                value = findID(5,value)
            if num == 3:
                att = "trophies"
            query = '''
            UPDATE TABLE teams 
            SET ''' + att + " = " + value + '''
            WHERE teamID = ''' + id + ";"
        if opt == 3:
            print("What would you like to change\n")
            print('''
            1. Team1 score
            2. Team2 score
            3. outcome
            ''')
            if num == 1:
                att = "team1_score"
            if num == 2:
                att = "team2_score"
            if num == 3:
                att = "ourcome"
            query = '''
            UPDATE TABLE games 
            SET ''' + att + " = " + value + '''
            WHERE gameID = ''' + id + ";"
        if opt == 4:
            print("What would you like to change\n")
            print('''
            1. Most recent player winner
            2. Most recent team winner
            ''')
            num = helper.get_choice([1,2])
            value = input("Enter new value: ")
            if num == 1:
                att = "player_winner_id"
                value = findID(1,value)
            if num == 2:
                att = "team_winner_id"
                value = findID(2,value)
            query = '''
            UPDATE TABLE trophies 
            SET ''' + att + " = " + value + '''
            WHERE trophyID = ''' + id + ";"
        if opt == 5:
            print("Changes Done")
            break
    
    

def insert_records(): # inserts record(s)
    pass

def startscreen():
    print("Welcome")
    create_all_tables()
    num = options()
    while True:
        if num == 1:
            print("Not yet completed")
        if num == 2:
            print("Not yet completed")
        if num == 3:
            print("Not yet completed")
        if num == 4:
            print("You chose to update a record")
        if num == 5:
            print("Not yet completed")
        if num == 6:
            print("Not yet completed")
        if num == 7:
            break

#main program
startscreen()