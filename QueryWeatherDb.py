# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 07:39:51 2022

@author: PACMAN
"""

#Purpose: Query database using SQL
#Name: Miguel Pacudan
#Date: Sep 19, 2022
#   Run BuildWeatherDB.py to build weather database before running this program

import sqlite3
import pandas as pd


#file names for database and output file
dbFile = "weather.db"

#format output
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.expand_frame_repr', False)

#connect to and query weather database 
conn = sqlite3.connect(dbFile)
#Create SQL command

# Order by: timestamp
selectCmd = " SELECT * FROM observations ORDER BY timestamp; "
                
# Order by: Min-to-Max temperature
# selectCmd = " SELECT MIN(temperature), MAX(temperature) FROM observations; "

# Order by: Clear text description
# selectCmd = "SELECT temperature, windspeed, textDescription FROM observations where textDescription = 'Clear'; "

# selectCmd = """ SELECT windspeed, relativeHumidity FROM observations
                # ORDER BY timestamp; """
                
# selectCmd = """ SELECT windChill FROM observations
#                 ORDER BY timestamp; """
#print out the query
result = pd.read_sql_query(selectCmd, conn)
print(result)
