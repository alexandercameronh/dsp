# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    k=0
    m=0
    newlist=[]
    for i in range(0, len(words)):
        if len(words[i]) >= 2:
            newlist.append(words[i])
    for i in range(0,len(newlist)):
        checkword=newlist[i]
        if checkword[0] == checkword[-1]:
            m=m+1
    print(m)
    
match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
match_ends(['', 'x', 'xy', 'xyx', 'xx'])
match_ends(['aaa', 'be', 'abc', 'hello'])  
##############################################################################################

##############################################################################################
def front_x(words):
    xlist=[]
    newlist=[]
    for i in range(0, len(words)):
        checkword=words[i]
        if checkword[0] == 'x':
            xlist.append(words[i])
        else:
            newlist.append(words[i])
    newlist.sort()
    xlist.sort()
    xlist = list(xlist+newlist)
    print(xlist)

    
front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])   
##############################################################################################

##############################################################################################

def remove_adjacent(nums):
    new_nums=[]
    if len(nums) < 1:
        print(nums)
    else:
        new_nums.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                new_nums.append(nums[i])
                print(new_nums)
    
remove_adjacent([1, 2, 2, 3])
remove_adjacent([2, 2, 3, 3, 3])
remove_adjacent([3, 2, 3, 3, 3])   
remove_adjacent([])
##############################################################################################

##############################################################################################

def linear_merge(list1, list2):
    list(list1)
    list(list2)
    list1.extend(list2)
    list(list1)
    list1.sort()
    print(list1)
    
linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
