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
        
def options():
    print('''
    1. Find songs by artist
    2. Find songs by genre
    3. Find songs by feature
    4. Update a song's informaion
    5. Delete a song
    6. Delete all records with at least 1 NULL attribute
    7. Exit
    ''')
    return helper.get_choice([1,2,3,4,5,6,7])
        