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