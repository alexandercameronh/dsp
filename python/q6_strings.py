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

def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
