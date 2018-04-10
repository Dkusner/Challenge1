# Alooma SE Challenge Response

## 1.	Introduction
This document addresses the Alooma SE challenge.  It provides a holistic view of the steps and results yielded as an outcome of the exercise.

## 2.	Software
This assignment was built using the following OS and SW tools:
* Python 3.6.3 64bits 
* MySQL 6.3.10 64bits
*	IOS – High Sierra 10.13.4
*	Data from hubspot  -“Engagements Overview”  
Link to Engagements Overview:  https://developers.hubspot.com/docs/methods/engagements/engagements-overview


## 3.	Extracting Data:

### 3.1	Pulling Data from Hubspot. 
The file 'getEngagements.py' combines the API call and a Python script to extract the engagement data and convert to csv output.
The libraries imported are:
* urllib
* urllib.request
* json
* csv
* time
* os	
Link to getEngagements.py:  https://github.com/Dkusner/Challenge1/blob/master/source/getEngagements.py

### 3.2	Python Algorithm to Retrieve Data

* 'getEngagements.py' retrieves the engagement data from the url via API call.
* Response from API call is translated into Json file so that analysis can be conducted.
* The script extracts the relevant fields and outputs a CSV file for use to import into MySQL.
* To run the python code, run command: runfile('~getEngagements.py') from python console.
* Output: Once the command is executed, a csv file "getEngagements_output.csv"  is created in the home directory.
Link to getEngagements_output.csv:  https://github.com/Dkusner/Challenge1/blob/master/output/getEngagements_output.csv

## 4.	Importing and Reading the Data in MySQL

*	The Data Import Wizard in MySQL Workbench was used to import the data from 'getEngatements_output.csv' (the output file from python script).  All defaults were used during the import.
* The import wizard produced the following schema:
  * id (int)
  * portalId (int)
  * createdAt (text)
  * type (text)
* Indexes were created on the following fields in order to ensure optimal performance during the specified SQL query:
  * createdAt
  * type
* SQL query 'typeDailyCount.sql' pulls the Engagements per Day and groups them by type.
Link to SQL query typeDailyCount.sql:  https://github.com/Dkusner/Challenge1/blob/master/source/typeDailyCount.sql
* THe output from the SQL query shows the count of each type per day.
Link to output from SQL query:  https://github.com/Dkusner/Challenge1/blob/master/output/type_daily_count.csv
