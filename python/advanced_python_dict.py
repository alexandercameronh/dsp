     #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:22:02 2017

@author: alexanderhughes
"""


import csv
import collections
import itertools


f =open('/Users/alexanderhughes/faculty.csv')
csv_f=csv.reader(f)

csv_f=list(csv_f)

degreeList=[]
titleList=[]
emailList=[]
domainList=[]
secondDomainList=[]
person=[]
newDegreeList=[]
finalDegreeList=[]
degreeSubset=[]
currentList=[]
partsList=[]
finalDegreeList2=[]
emailList2=[]
emailListFinal=[]
nameList=[]

for i in range(0, len(csv_f)):
    degreeList.append(csv_f[i][1])
    titleList.append(csv_f[i][2])
    emailList.append(csv_f[i][3])
    nameList.append(csv_f[i][0])
    
del titleList[0]
del emailList[0]
del degreeList[0]




  ###########################################################Part III

nameList2=[]
firstNames=[]
lastNames=[]
fullNameFirst=[]
fullNameLast=[]
del nameList[0]

for i in range(0, len(nameList)):
    parts=nameList[i].split(' ')
    nameList2.append(parts)

for i in range(0, len(nameList2)):
    firstNames.append(nameList2[i][0])
    lastNames.append(nameList2[i][-1])
    


lastNames=tuple(lastNames)

values=list(zip(degreeList,titleList,emailList))


dictionary=dict(zip(lastNames, values))

print(dictionary)

faculty=list(zip(lastNames,values))

faculty

print(dictionary['Bellamy'])
print(dictionary['Bilker'])
print(dictionary['Bryan'])
#################################### Q7 



fullNameFirst=list(zip(firstNames,lastNames))
professor_dict=dict(zip(fullNameFirst,values))
print(list(professor_dict.items())[:3])



################################### Q8




fullNameLast=list(zip(lastNames,firstNames))
#print(fullNameLast)
professor_dict2=collections.OrderedDict(zip(fullNameLast,values))

print(list(professor_dict2.items())[:3])


    

