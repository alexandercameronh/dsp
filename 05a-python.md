# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences of values (of any type). Also, both lists and tuples are indexed by integers. 

>> The main difference between the two is that lists are mutable; tuples are immutable. Tuples would work as keys in dictionaries. This is because of the properties of Dictionaries. Dictionaries within Python were designed using a hashtable and for this reason the keys need to be hashable. This would cause problems with mutable keys (lists). 
---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Sets are unordered, contain unique unduplicated elements, and are not indexed by integers. Lists are ordered values of any type, and indexed by integers.

>> List: a=[1,2,3,3,3,4,5,5, 'apple']

>>Set: b=[1,2,3,4]

>>When trying to find a specific element within a set or list - sets are faster since they do not contain duplicate values.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda fuction is an 'anonymous' (does not have a name) function. It allows the user to create a simple, one-lined function that can quickly be written and executed.

>> One reason why it is used frequently is because of it's efficieny.

>> Example: Imagine I have a small home directory of my friend's their corresponding ages, I can quickly sort this set directory (set of tuples) based on age using lamba expression in the key argument:

>>homeDirectory = [
        ('Jane', 'Doe', '22'),
        ('Alex', 'Hughes', '26'),
        ('Lauren', 'Gehman', '21')]

>>sorted(homeDirectory, key=lambda age:age[2])

>>OUTPUT: [('Lauren', 'Gehman', '21'), ('Jane', 'Doe', '22'), ('Alex', 'Hughes', '26')]



---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>>List comprehensions is the ability transform one list into another list. 

>>

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>>7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





