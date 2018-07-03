#!/usr/bin/python3
import mysql.connector as hi
conn = hi.connect(user='root',password='ubuntu',database='Sanjay',host='localhost')
sql_lang=conn.cursor()
sql_lang.execute("show databases;")
print(sql_lang.fetchall())
