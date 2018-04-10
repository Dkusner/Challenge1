# Alooma SE Challenge Response

## 1.	Introduction
This document addresses the Alooma SE challenge.  It provides a holistic view of the steps and results yielded as an outcome of the exercise.

## 2.	Software
This assignment was built using the following OS and SW tools:
* Python 3.6.3 64bits 
* MySQL 6.3.10 64bits
*	IOS – High Sierra 10.13.4
*	Date from hubspot  -“Engagements overview”

## 3.	Extracting Data:

### 3.1	Pulling Data from Hubspot. 
The file 'getEngagements.py' combines the API and a Python script to extract the engagement data from the url.
The libraries imported are:
* urllib
* urllib.request
* json
* csv
* time
* os	

## 3.2	Algorithm

a)	'getEngagements.py' retrieves the engagement data from the url,

b)	 It translates it into a Json file, where a data analysis is conducted.

c)	The relevant fields are organized and sorted in a sequential order.

d)	The script the groups the data and outputs a CSV file which contains a readable table.

e)	Within the in python console, run command: runfile('~getEngagements.py'). 

d)  Output: Once the command  is executed, a csv file "getEngagements_output.csv"  is created in the home directory.


## 4.	Reading Data

*	A SQL Query (filename)   pulls the Engagements per Day broken and groups them by type. The count of each type per day is displayed .
*	Schema is filenamexxxxxx
*	The SQL query yields the results shown in file xxxxx.

