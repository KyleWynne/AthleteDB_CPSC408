import mysql.connector
from helper import helper
import re
import string
from datetime import date

#connect to mysql
conn = mysql.connector.connect(host="localhost",
                               user="root",
                               password="cpsc408",
                               auth_plugin='mysql_native_password',
                               database="RideShare")

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
    6. Exit
    ''')
    return helper.get_choice([1,2,3,4,5,6])

def view_all_records(): # prints all records in a table
    pass

def query_data(): # queries data with parameters/filters
    pass

def delete_records(): # deletes record(s)
    pass

def update_records(): # updates record(s)
    pass

def insert_records(): # inserts record(s)
    pass
