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
        self.cursor.execute(query, variables)
        self.connection.commit()
        print("query executed")
        
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
