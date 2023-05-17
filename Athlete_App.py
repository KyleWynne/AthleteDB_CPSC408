#this code does not run when using the app this code was made solely for development and debugging features of the app
import mysql.connector
from helper import helper
import re
import string
from datetime import date
import csv

#connect to mysql
conn = mysql.connector.connect(host="localhost",
                               user="root",
                               password="cpsc408",
                               auth_plugin='mysql_native_password',
                               database="Athlete")

cur_obj = conn.cursor()

#execute DQL query, no changes made to DB but returns the total output
def execute_query(query):
    cur_obj.execute(query)
    return cur_obj.fetchall()

def bulk_insert(query,records):
    cur_obj.executemany(query,records)
    conn.commit()

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
        teamID INT,
        FOREIGN KEY (teamID) REFERENCES teams(teamID)
        );"""
    execute_insert(query2)
    query3 = """
    CREATE TABLE IF NOT EXISTS games (
        gameID INT AUTO_INCREMENT PRIMARY KEY,
        team1ID INT ,
        team2ID INT ,
        FOREIGN KEY (team1ID) REFERENCES teams(teamID),
        FOREIGN KEY (team2ID) REFERENCES teams(teamID),
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
        leagueID INT NOT NULL,
        FOREIGN KEY (leagueID) REFERENCES leagues(leagueID),
        year YEAR,
        player_winner_id  INT,
        FOREIGN KEY (player_winner_id) REFERENCES players(playerID),
        team_winner_id INT,
        FOREIGN KEY (team_winner_id) REFERENCES teams(teamID));"""
    execute_insert(query5)
    query6 = """
    CREATE INDEX team_index ON teams(teamID);
    CREATE INDEX player_index ON players(playerID);"""
    #execute_insert(query6)

    query7 = """
        CREATE VIEW allPlayers AS
        SELECT players.teamID AS TID, players.player_name, players.salary, players.age, players.sport, players.trophies, teams.teamID, teams.team_name
        FROM players
        INNER JOIN teams
        ON players.teamID = teams.teamID;
    """
    #execute_insert(query7)


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
    #enforces joins accross at least 3 tables(teams, leauges, games)

    query = """
    SELECT games.gameID, games.team1_score, games.team2_score, games.outcome, l.league_name
    FROM games
    JOIN teams t ON t.teamID = games.team1ID
    JOIN games g ON t.teamID = g.team1ID AND t.teamID = g.team2ID
    JOIN leagues l on t.leagueID = l.leagueID;
    """
    cur_obj.execute(query)
    return cur_obj.fetchall()

    query1 = """
    CREATE VIEW team_view AS
    SELECT games.team1_score, games.team2_score, games.outcome
    FROM games
    WHERE games.team1_score = games.team2_score
    """
    cur_obj.execute(query1)

    query2 = """
    SELECT * FROM team_view
    """
    cur_obj.execute(query2)

def generate_csv(): #export the players table after it is created
    query = """
    SELECT *
    FROM players
    """
    cur_obj.execute(query)
    rows = cur_obj.fetchall()
    with open('players.csv','w',newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def query_data(): # queries data with parameters/filters
    #uses a subquery and aggregation
    action = int(input("Enter 1 to query MAX salary by player, 2 to query games won by team, 3 to query gameID's, 4 to query all league_name's, 5 to query by trophy_names: "))
    if action == 1:
        player_id = input("Enter playerID: ")
        query = """
        SELECT MAX(salary)
        FROM players
        WHERE playerID = """ + player_id + ";"
        cur_obj.execute(query)
        return cur_obj.fetchall()
    if action == 2:
        team_name = input("Enter team name: ")
        #subquery to count how many games the team won
        query = """
        SELECT teams.team_name,
            (SELECT COUNT(*) FROM games WHERE games.outcome = teams.id) AS games_won
        FROM teams
        WHERE teams.team_name = %s;
        """
        cur_obj.execute(query, (team_name,))
        return cur_obj.fetchall()
    if action == 3:
        game = input("Enter gameID: ")
        query = """
        SELECT *
        FROM games
        WHERE gameID = """ + game + " GROUP BY gameID;"
        cur_obj.execute(query)
        return cur_obj.fetchall()
    if action == 4:
        league_id = input("Enter leagueID: ")
        query = """
        SELECT *
        FROM leagues
        WHERE leagueID = """ + league_id + "GROUP BY league_name;"
        cur_obj.execute(query)
        return cur_obj.fetchall()
    if action == 5:
        trophy = input("Enter trophy name: ")
        query = """
        SELECT *
        FROM trophies
        WHERE trophy_name = """ + trophy + "GROUP BY trophy_name;"
        cur_obj.execute(query)
        return cur_obj.fetchall()


def delete_records(): # deletes record(s)
    tablename = input("Give me the table name: ")
    column = input("From what column do u want to remove from: ")
    data = input("What exacly do u want to delete: ")
    query = '''
    DELETE FROM '{tablename}'
    WHERE '{column}' LIKE '{data}';
    '''
    cur_obj.execute(query)
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
    while True:
        try:
            if num == 1:
                query = """
                SELECT playerID
                FROM players
                WHERE player_name =  '""" + name + "';"
            if num == 2:
                query = """
                SELECT teamID
                FROM teams
                WHERE team_name = '""" + name + "';"
            if num == 3:
                print("DNE")
            if num == 4:
                query = """
                SELECT trophyID
                FROM trophies
                WHERE trophy_name = '""" + name + "';"
            if num == 5:
                query = """
                SELECT leagueID
                FROM leagues
                WHERE league_name = '""" + name + "';"
            return query_returnOne(query)
        except TypeError:
                print("Value does not Exist")
                num = input("Enter name again: ")


def update_records(): # updates record(s)
    while True:
        opt = update_options()
        if opt != 5:
            tuple = find_table_tuple(opt)
            id = str(tuple[0][0])
            print(id)
        if opt == 1:
            print("What would you like to change")
            print('''
            1. player Name
            2. yearly salary
            3. age in years
            4. sport
            5. number of trophies
            6. Team
            ''')
            num = int(input())
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
                print(value)
            query = '''
            UPDATE players
            SET ''' + att + " = '" + str(value) + ''''
            WHERE playerID = ''' + str(id) + ";"
        if opt == 2:
            print("What would you like to change")
            print('''
            1. Team Name
            2. number of trophies
            ''')
            num = int(input())
            value = input("Enter new value: ")
            if num == 1:
                att = "team_name"
            if num == 2:
                att = "trophies"
            query = """
            UPDATE teams
            SET """ + att + " = '" + str(value) + """'
            WHERE teamID = """ + str(id) + ";"
        if opt == 3:
            print("What would you like to change")
            print('''
            1. Team1 score
            2. Team2 score
            3. outcome
            ''')
            num = int(input())
            value = input("Enter new value: ")
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
            print("What would you like to change")
            print('''
            1. Most recent player winner
            2. Most recent team winner
            ''')
            num = int(input())
            value = input("Enter new value: ")
            if num == 1:
                att = "player_winner_id"
                value = findID(1,value)
                query1 = '''
                UPDATE trophies
                SET ''' + att + " = '" + str(value) + """'
                WHERE trophyID = """ + str(id) + ";"

                query2 = """UPDATE players
                SET trophies = trophies + 1
                WHERE playerID = """ + str(value) + """;"""
            if num == 2:
                att = "team_winner_id"
                value = findID(2,value)
                query1 = '''
                UPDATE trophies
                SET ''' + att + " = " + str(value) + '''
                WHERE trophyID = ''' + str(id) + ";"

                query2 = """UPDATE teams
                SET trophies = trophies + 1
                WHERE teamID = """ + str(value) + """;"""
        if opt == 5:
            print("Changes Done")
            break
        execute_insert("START TRANSACTION;")
        execute_insert(query1)
        execute_insert(query2)
        execute_insert("COMMIT;")



def insert_records(): # inserts record(s)
    #made it single input for testing purpose
    tablename = input("Give me table name: ")
    columnname1 = input("Give me the columnname: ")
    value1 = input("Give me the values you want to input: ")
    query = '''
    INSERT INTO ''' + tablename + "(" + columnname1 + ")"'''
    VALUES (%s)''', (value1) + ''';'''
    cur_obj.execute(query)
    pass

def insert_sample_data(): # inserts sample data
    query5 = "INSERT INTO leagues (league_name, sport, country) VALUES(%s, %s,%s)"
    data5 = [
        ("Ghost", "nothing", "Nothing"),
        ("NBA", "Basketball", "USA"),
        ("Serie A", "Soccer", "Italy"),
        ("La Liga", "Soccer", "Spain"),
        ("ATP", "Tennis", "World")
    ]
    #bulk_insert(query5, data5)
    query2 = "INSERT INTO teams (team_name, leagueID, trophies) VALUES(%s, %s, %s)"
    data2 = [
        ("Ghost", 1, 0),
        ("Lakers", 2, 17),
        ("Juventus", 3, 36),
        ("Barcelona", 3, 26),
        ("Switzerland", 4, 0)
    ]
    #bulk_insert(query2, data2)
    query = "INSERT INTO players (player_name, salary, age, sport, trophies, teamID) VALUES(%s, %s, %s, %s,%s,%s)"
    data = [
        ("Ghost", 0, 0, "ghost", 0, 1),
        ("Lebron James", 37436858, 35, "Basketball", 4, 2),
        ("Cristiano Ronaldo", 67800000, 35, "Soccer", 5,3),
        ("Lionel Messi", 61000000, 32, "Soccer", 6,4),
        ("Roger Federer", 7700000, 38, "Tennis", 20,5)
    ]
    #bulk_insert(query, data)
    query3 = "INSERT INTO games (team1_score, team2_score, outcome, team1ID, team2ID) VALUES(%s, %s, %s,%s, %s)"
    data3 = [
        (100, 98, "W", 2, 3),
        (2, 1, "W", 4, 5),
        (2, 3, "L", 3, 4),
        (0, 1, "L", 5, 4)
    ]
    #bulk_insert(query3, data3)
    query4 = "INSERT INTO trophies (trophy_name,leagueID, team_winner_id, player_winner_id) VALUES(%s,%s,%s,%s)"
    data4 = [
        ('NBA Championship', 2, 1, 1),
        ('Serie A', 3, 1, 1),
        ('La Liga', 4,  1, 1),
        ('Wimbledon', 5, 1, 1)
    ]
    #bulk_insert(query4, data4)
def startscreen():
    print("Welcome the the Athlete Database!")
    create_all_tables()
    insert_sample_data()
    while True:
        num = options()
        if num == 1:
            print("Not yet completed")
        if num == 2:
            print("Not yet completed")
        if num == 3:
            print("Not yet completed")
        if num == 4:
            print("You chose to update a record")
            update_records()
        if num == 5:
            print("Not yet completed")
        if num == 6:
            print("You chose to generate a csv report")
            generate_csv()
        if num == 7:
            break

#main program
startscreen()
#insert_records()
