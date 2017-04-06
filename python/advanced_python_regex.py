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

for i in range(0, len(csv_f)):
    degreeList.append(csv_f[i][1])
    titleList.append(csv_f[i][2])
    emailList.append(csv_f[i][3])
    
del titleList[0]
del emailList[0]
del degreeList[0]



#####Question 1#############################################################

for i in degreeList:
    j=i.replace('.', '')
    newDegreeList.append(j)


for i in range(0, len(newDegreeList)):
    if len(newDegreeList[i]) < 5 and newDegreeList[i] != '0':
        finalDegreeList.append(newDegreeList[i])
    else:
        degreeSubset.append(newDegreeList[i])
    
degreeSubset.pop(4)


for i in degreeSubset:
    j=i.replace(' ', ',')
    currentList.append(j)

for i in range(0, len(currentList)):
    parts=currentList[i].split(',')
    partsList.append(parts)

chain=itertools.chain(*partsList)
list3=list(chain)

list3.remove('')
del list3[3]
del list3[6]
del list3[11]

for i in range(0, len(list3)):
    finalDegreeList.append(list3[i])
    
for i in finalDegreeList:
    j=i.replace(' ','')
    finalDegreeList2.append(j)
    
print("There are {} different degrees\n".format(len(set(finalDegreeList2))))
counter2=collections.Counter(finalDegreeList2)
print(counter2)



#####Question 2#############################################################

titleList[24]='Assistant Professor of Biostatistics'
newTitleList=list(set(titleList))


print("\n\nThere are {} different titles".format(len(newTitleList)))
counter=collections.Counter(titleList)
print(counter)


#####Question 3#############################################################
print("\n\n")
print(emailList)



#####Question 4#############################################################


for i in range(0,len(emailList)):
   parts=emailList[i].split('@')
   emailList2.append(parts)
   
for i in range(0, len(emailList2)):
    emailListFinal.append(emailList2[i][1])

print("\n\nThere are {} different email domains".format(len(set(emailListFinal))))
