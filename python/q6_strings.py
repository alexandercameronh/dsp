# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count < 10:
        print("Numer of donuts: {}".format(count))
    else:
        print("Number of donuts: many.")
        
donuts(4)    
donuts(9)
donuts(10)
donuts(11)
###################################

###################################
def both_ends(s):
    if len(s) < 2:
        s=''
        print("'{}'".format(s))
    else:
        print("{}{}{}{}".format(s[0],s[1],s[-2],s[-1]))
    

both_ends('spring')
both_ends('Hello')
both_ends('a')
both_ends('xyz')
###################################

###################################
def fix_start(s):
    origLen=len(s)
    s=s+s[0]
    for i in range(1, len(s)-1):
        if s[0] != s[i]:
            s=s+s[i]
        else:
            s=s+'*'
    print(s[origLen::])

fix_start('babble')
fix_start('aardvark')
fix_start('google')
fix_start('donut')
###################################


###################################
def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError
###################################    

###################################
def verbing(s):
    if len(s) < 3:
        print(s)
    else:
        if s[-1] == 'g':
            s=s + 'ly'
            print(s)
        else:
            s=s + 'ing'
            print(s)
            
verbing('hail')
verbing('swiming')
verbing('do')
###################################

###################################
def not_bad(s):
    a=0
    b=0
    a=s.find('not')
    b=s.find('bad')
    if b < a:
        print(s)
    else:
        print(s.replace(s[a:b+3],'good'))

not_bad('this movie is not so bad')
not_bad('This dinner is not that bad!')
not_bad('This tea is not hot')
not_bad("It's bad yet not")
###########################################

###########################################
def front_back(a,b):
    middle1=0
    middle2=0
    if len(a)%2 == 0:
        middle1=int(len(a)/2)
    else:
        middle1=int((len(a)/2)+1)
    if len(b)%2 == 0:
        middle2=int(len(b)/2)
    else:
        middle2=int((len(b)/2)+1)
    print("{}{}{}{}".format(a[:middle1:],b[:middle2:],a[middle1::],b[middle2::]))
    
front_back('abcd', 'xy')
front_back('abcde', 'xyz')
front_back('Kitten','Donut')
