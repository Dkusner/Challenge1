# Alooma SE Challenge Response

## 1.	Introduction
This document addresses the Alooma SE challenge.  It provides a holistic view of the steps and results yielded as an outcome of the exercise.

## 2.	Software
This assignment was built using the following OS and SW tools:
* Python 3.6.3 64bits 
* MySQL 6.3.10 64bits
*	IOS – High Sierra 10.13.4
*	Date from hubspot  -“Engagements overview”  https://developers.hubspot.com/docs/methods/engagements/engagements-overview


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

*	The Data Import Wizard in MySQL Workbench was used to import the data from 'getEngatements_output.csv' (python output file).  All defaults are used during the import).
* The import wizard produced the following schema:
* Once the file was created, it contained the following schema:
* A SQL query 'typeDailyCount.sql' pulls the Engagements per Day and groups them by type. The count of each type per day is displayed.
*	The SQL query results are shown in the output file: https://github.com/Dkusner/Challenge1/blob/master/output/type_daily_count.csv

