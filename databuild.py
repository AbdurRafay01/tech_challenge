import csv
import psycopg2
import os
import glob

# conn = psycopg2.connect("host=127.0.0.1 dbname=covid_data user=abdurrafay password=test123")
# print("connecting to the database")

filename = "owid-covid-data.csv"


tablename = filename.replace("./TestDataLGA\\", "").replace(".csv", "")
print(tablename)
tablename = tablename.replace("-", "_")
print(tablename)
# Open file
fileInput = open(filename, "r")

# Extract first line of file
firstLine = fileInput.readline().strip()

# Split columns into an array [...]
columns = firstLine.split(",")

# Build SQL code to drop table if exists and create table
sqlQueryCreate = 'DROP TABLE IF EXISTS '+ tablename + ";\n"
sqlQueryCreate += 'CREATE TABLE '+ tablename + "("

#some loop or function according to your requiremennt
# Define columns for table
for column in columns:
    sqlQueryCreate += column + " VARCHAR(64),\n"

sqlQueryCreate = sqlQueryCreate[:-2]
sqlQueryCreate += ");"

cur = conn.cursor()
cur.execute(sqlQueryCreate)
conn.commit()
cur.close()