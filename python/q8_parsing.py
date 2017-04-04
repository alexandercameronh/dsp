# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 11:13:57 2017

@author: alexanderhughes
"""

import csv



with open('/Users/alexanderhughes/football.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

print(type(readCSV))


goals_made=[]
goals_allowed=[]
newList=[]
teams=[]

f =open('/Users/alexanderhughes/football.csv')
csv_f=csv.reader(f)

for row in csv_f:
    goals_made.append(row[5])
    goals_allowed.append(row[6])
    teams.append(row[0])
    
del goals_made[0]
del goals_allowed[0]
del teams[0]


goals_made=list(map(int, goals_made))
goals_allowed=list(map(int, goals_allowed))
for i in range(0, len(goals_made)):
    diff=goals_made[i]-goals_allowed[i]
    newList.append(diff)

newList=list(map(abs, newList))

min(newList)
correspondIndex=newList.index(min(newList))

print("The team with the smallest difference in Goals Scored vs Goals Allowed is: {}".format(teams[correspondIndex]))




