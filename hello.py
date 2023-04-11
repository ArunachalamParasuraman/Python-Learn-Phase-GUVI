# strings
# indexing - left to r8

a = 'i love india'
print(a[7])            # o/p -- i

# type

a = 'i love india'
print(type(a))
print(type(a[-1]))

# r8 to left

a = 'i love india'
print(a[-2])

# length

a = 'i love india'
print(len(a))

# indexing with len

a = 'i love india this is my country'
print(a[len(a)-7])

# slicing

a = 'i love india'
print(a[0:6]) # by default skip = 1

# if skip = 2
a = 'i love india'
print(a[0:6:2])

# reverse slicing

a = 'i love india'
print(a[-5:])   

# prob for test
a=2                                        # P E D M A S
b=3
c=5
d=a+b*c/b+c+(c//a%b)//(a**(b**b)%c)
print(d)
print(type(d))

# in-built functions for strings
#upper
a = 'arun'
print(a.upper())

# lower
a = 'ARUN'
print(a.lower())

# count
a = 'i am arunachalam am am'
print(a.count('a'))
print(a.count('am'))

# capitalize
a = 'i Am Arunachalam Am Am'
print(a.capitalize())

# index
a = 'i am arunachalam am am'
print(a.index('a'))              # if i/p is not there it shows value error
print(a.index('am'))
# index and find with indexing to find index number without counting manually
a = 'i love india this the is my country'
print(a[a.index('the')])
print(a[a.find('the')])
print(a[18])

# find
a = 'i am arunachalam am am'
print(a.find('a'))                # if i/p is not there it shows -1
print(a.find('am'))

# isalpha
a = 'iamarunachalam'             # o/p will be in true or false
print(a.isalpha())

# isalnum
a ='iamarunach0123alam'         # o/p will be in true or false
print(a.isalnum())

# strip
a ='   arunachalam   '
print(a.strip())

# rstrip
a ='   arunachalam   '
print(a.rstrip())

# lstrip
a ='   arunachalam   '
print(a.lstrip())

# startswith
a ='i am aru'                    # o/p will be in true or false
print(a.startswith('i'))

# endswith
a ='i am aru'                    # o/p will be in true or false
print(a.endswith('u'))

# join
a ='aruna'
print('the'.join(a))             # syntax : 'sub string'.join(variable) always o/p will be string

# replace
a ='asonachalam'
print(a.replace('son','run'))

# split
a ='i love eagles'
print(a.split('e'))              # ['i lov', ' ', 'agl', 's']
a ='In loINve Ingel India'
print(a.split('In'))             # ['', ' loINve ', 'gel ', 'dia']

# partition
a ='i love india ya'
print(a.partition('e'))          # ('i lov', 'e', ' india ya')
a ='It is raining'
print(a.partition('i'))          # ('It ', 'i', 's raining')

# LIST
# indexing 
a =[1,2,3,4,5,'hii','aru','hello',[6,7,8,9]]
print(a[5]) 
# indexing within a nested loop
a =[1,2,3,4,5,'hii','aru','hello',[6,7,8,9]]
print(a[8][3])
a =[1,2,3,4,[11,12,14,15,[['aru','jas','rose'],45,63],95,4,1]]
print(a[4][4][0][2])

# slicing
a =[1,2,3,4,5,'hii','aru','hello',[6,7,8,9]]
print(a[5:8])

# in-built functions for list
# max
a =[1,2,60,5.5,6.7,88.9,88]
print(max(a))
a =['a','B','c','1','5','10']
print(max(a))

# min
a =[1,2,60,5.5,6.7,88.9,88]
print(min(a))
a =['a','B','c','1','5','10']
print(min(a))

# append
a =[1,2,3,'aru','hii']           # it will change only in source
a.append('hello')            
a.append([5,6,7])
print(a)                         # o/p ---[1, 2, 3, 'aru', 'hii', 'hello', [5, 6, 7]]

# extend
a =[1,2,3,'aru','hii']            # it will change only in source
a.extend('hello')
a.extend([5,6,7])                 # o/p --[1, 2, 3, 'aru', 'hii', 'h', 'e', 'l', 'l', 'o', 5, 6, 7]
print(a)

# pop
a =['aru',1,2,3,'data']
b =a.pop()
print(b)                        # o/p---data
print(a)                        # o/p---['aru', 1, 2, 3]
# pop with index no
a =['aru',1,5,3,'data']
b =a.copy()
c =b.pop(2)
print(a)                        # o/p--['aru', 1, 5, 3, 'data']
print(b)                        # o/p--['aru', 1, 3, 'data']
print(c)                        # o/p--5

# insert
a =['aru',1,2,5,4]
b =a.copy()
b.insert(3,'love')
print(b)                        # o/p--['aru', 1, 2, 'love', 5, 4]

# join for list
a =['1','2','3','4','5']
print('aru'.join(a))            # o/p--1aru2aru3aru4aru5

# sort - it will affect the source
a =[1,5,9,7,8,55,61,23]
a.sort()
print(a)
# to perform sort in decending order
a =[1,5,9,7,8,55,61,23]
a.sort(reverse=True)
print(a)

# sorted - it will not affect the source
a =[5,6,55,98,45,12,32,77]
print(sorted(a))
# to perform sort in decending order
a =[5,6,55,98,45,12,32,77]
print(sorted(a,reverse=True))

# reverse
a =[50,40,30,20,10,1]
a.reverse()
print(a)

# reversed
a =[50,40,30,20,10,1]
print(reversed(a))            # o/p----<list_reverseiterator object at 0x000001B44E50D6A0>
print(list(reversed(a)))      # o/p----[1, 10, 20, 30, 40, 50]

# sum
a =[2,4,6,8,10,12]
print(sum(a))

# item assignment
a =[1,2,3,4,5]
a[3]='aru'
print(a)

# concatnation
# in string
print('arun'+'aru')
print('aru'*3)
# in list
print([1,2,3]+[4,5,6])
print([1,2,3]*3)

# set                                        # it will take only unique elements
a ={1,2,1,2,5,3,4,6,8,8,9,7,6,4,2,5,3,1}     
print(a)                                     # o/p---{1, 2, 3, 4, 5, 6, 7, 8, 9}

# in-built functions in set
# add
a ={1,2,3,'aru',(4,5,6)}
a.add((7,8,9))
print(a)

# union
a ={1,2,3,4,5,6}
b ={5,6,7,8}
print(a.union(b))

# update
a ={1,2,3,4}
b =(5,8,9,10)
a.update([4,5,6,7],b)
print(a)

# intersection
a ={1,2,3,4,5}
b ={4,5,6,7,8}
print(a.intersection(b))

# difference
a ={1,2,3,4,5}
b ={4,5,6,7,8}
print(a.difference(b))
print(b.difference(a))

# symmetric difference
a ={1,2,3,4,5}
b ={4,5,6,7,8}
print(a.symmetric_difference(b))

# remove----if the element not there it shows error
a ={1,5,6,4,8,7}
a.remove(4)                 # o/p-----{1, 2, 3, 6, 7, 8}
# a.remove(9) ------ key error
print(a)

# discard----if the element not there it shows orginal set
a ={1,5,6,4,8,7}
a.discard(4)                 # o/p-----{1, 2, 3, 6, 7, 8}
# a.discard(9) ---------- o/p - {1, 4, 5, 6, 7, 8}
print(a)

# conditions
# if else
a =55
b =41
if a>b:
    print('aru')
else:
    print('hello')
# 0,empty data type,false,none the condition is false
#a = 0 / [] / 5<1
if a:
    print('ar')
else:
    print('ua')

#elif
a =50
b =60
if a!=b:
    print('aru')
elif a<=b:
    print('run')
else:
    print('son')

a =3
b =2
if a>b:
    print(1)
if ['']:
    print(2)
if a>5:
    print(3)
elif a>4:
    print(4)                
elif b>a:
    print(5)
else:
    print(6)

# and
a =5
b =6
if a<b and a!=b:
    print('aru')
else:
    print('son')

# or
a =5
b =6
if a>b and a==b or a<b:
    print('aru')
else:
    print('son')

# in
a ='123456'
if '5' in a:
    print('true')
else:
    print('false')

# not
a =6
if not a>7:
    print('aru')
else:
    print('no')

#not in
a ='123456'
if '5' not in a:
    print('true')
else:
    print('false')

# range
print(range(5))         # o/p---range(0, 5)
print(list(range(5)))   # o/p---[0, 1, 2, 3, 4]
# indexing in range
print(range(5)[3])      # o/p----3
print(range(100,110))
print(list(range(100,110)))    # o/p---[100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
# skip in range
print(list(range(100,110,2)))   # o/p----[100, 102, 104, 106, 108]

# for loop
a ='arun'
for i in a:
    print(i.upper())
a =[1,2,'arun']
for i in a:
    print(i*2)
# take only even no and odd no
a =[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2==0:
        print(i)
a =[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if not i%2==0:        # if i%2==1:
        print(i)
a ='12345678910'
for i in a:
    if int(i)%2==0:
        print(i)  
# for with range and length
a =[1,2,3,4,6,7]
b =[5,6,7,8,9,3]
for i in range(len(a)):
    print(a[i]*b[i]) 

# while loop
# print 7 times aru
a =7
while(a>0):
    print('aru')
    a =a-1
# print 1 to 20
a =1
n =20
while(a<=n):          # a<21
    print(a)
    a =a+1

# print right angle triangle with * upto 5
n =5
a =1
while(a<=n):
    print('*'*a)
    a =a+1
# print left angle triangle with * upto 7
n =7
a =1
while(n>0):
    print((' '*(n-1))+'*'*a)
    n =n-1
    a =a+1
# print equilateral triangle with * upto 7
n =7
a =1
while(n>0):
    print((' '*(n-1))+('*'*a)+(' '*(n-1)))
    n =n-1
    a =a+1      # not yet completed

# dictionary
a ={'aru':45,'arun':43,'aru':55}
print(a['aru'])
# add or update key value pair
a ={'king':'queen',46:'rossi','true':'yes'}
a['aru'] = 'dev'
print(a)                                          # o/p ---{'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'dev'}
a ={'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'dev'}
a['aru'] = 'QA'
print(a)                                          # o/p ---{'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'QA'}

# in built functions in dictionary
# keys
a ={'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'dev'}
print(a.keys())                                                  # o/p ---dict_keys(['king', 46, 'true', 'aru'])

# values
a ={'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'dev'}
print(a.values())                                                # o/p ---dict_values(['queen', 'rossi', 'yes', 'dev'])
# for loop in dict -- will always take keys
a ={'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'dev'}
for i in a:
    print(i)
# to take values with for loop
a ={'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'dev'}
for i in a:
    print(i,a[i])

# items
a ={'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'dev'}
print(a.items())                                # o/p --dict_items([('king', 'queen'), (46, 'rossi'), ('true', 'yes'), ('aru', 'dev')])
# for loop in items
a ={'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'dev'}
for i in a.items():
    print(i)
a ={'king': 'queen', 46: 'rossi', 'true': 'yes', 'aru': 'dev'}
for k,v in a.items():
    print(k,v)
a =[('keys1',1,5),('keys2',10,45),('keys3',5,8)]  # we can manipulate if len of the elements are same
for a,b,c in a:
    print(a,b*c)

# function
def custom_add (a):
    c =0
    for i in a:
        c =c+i
    print(c)
a =[9,5,7,8,6,4,3,2,12]
custom_add([9,5,7,8,6,4,3,2,12])  # or custom_add(a)
a =[2,5,6,7]
custom_add(a)
# function with return
def hi_hello(a):              # if a fun has returned a value it will not return any other value and fun gets terminated instantly
    for i in a:
        return(i)
print(hi_hello([5,6,4,9]))      # o/p--5
# to add in strings
def cum_add (a):
    c =0
    for i in a:
        c =c+int(i)
    print(c)
    return(c)
a ='123456897'
cum_add(a)+5
# to add only no in string
def num_add (a):
    c =0
    for i in a:
        if not i.isalpha():
            c =c+int(i)
    print(c)
    return(c)
a ='679adf897gh253khl649uio32'
print(num_add(a)+20)

# yield--generator
def yi_gen (a):
    for i in a:
        yield (i)
a = yi_gen([1,2,3,4])
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a)) --- stop iteration error
print(list(a))
# if we perform any iteration in generator it will be empty list
def yi_gen (a):
    for i in a:
        yield (i)
a = yi_gen([1,2,3,4])
for i in a:
    print(i)
print(list(a))

# iterator
a =[1,2,3,4,5]
b =iter(a)
print(next(b))
print(next(b))
print(list(b))
# if we perform any iteration in iterator it will be empty list
a =[1,2,3,4,5]
b =iter(a)
for i in b:
    print(i)
print(list(b))

# pass --- it will just pass the condition or close the loop
for i in [1,2,3]:
    pass
for i in [4,5,6]:
    print(i)

# continue---whenever continue gets triggered that iteration will get skipped
a =[1,2,3,4,5,6,7,8,9,10]  # take only odd no
for i in a:
    if i%2==0:
        continue
    print(i)
a ='654sdfa65adfsd4156' # to add only no in string
c =0
for i in a:
    if i.isalpha():
        continue
    c =c+int(i)
print(c)

# break--- whenever break gets triggered that iteration will be terminated
# break inside a generator
def br_gen(a):
    for i in a:
        yield(i)
b =br_gen([5,3,4,8])
for i in b:
    if i==4:
        break
print(list(b))   # o/p---[8]
# break in loop
a =[1,2,3,4,5]
for i in a:
    if i==4:
        break
    print(i)

# lambda function
fun1 = lambda a,b,c : a+b*c/b+c+(c//a%b)//(a**(b**b)%c)
print(fun1(2,3,5))
# MRF
# map with lambda fun
v =[2,4,6,8,10,12]
print(list(map(lambda a:a*2,v)))
# map with def fun
v =[2,4,6,8,10,12]
def custom_mul(v):
    return v*2
print(list(map(custom_mul,v)))

# filter with lambda fun
v =[2,4,6,8]
print(list(filter(lambda a:a>=4,v)))  #o/p--[4, 6, 8]
# filter with def fun
v =[2,4,6,8]
def cum_fil(a):
    return a>45
print(list(filter(cum_fil,v)))    #o/p---[]
# find leap year
a =[1100,1550,1220,1440,2200,2000,2014,2016,2012,2022,2020]
print(list(filter(lambda a:a%4==0 and a%100!=0 or a%400==0,a)))
# reduce
from functools import reduce
def Red(a,b):
    return a+b
print(reduce(Red,[2,4,6,8],5))   #o/p---25

# exception handling
a =45
b =[0,1,2,0,3,0]
for i in b:
    try:
        print(a/i)
    except:
        pass
    print(i)
# if continue
a =45
b =[0,1,2,0,3,0]
for i in b:
    try:
        print(a/i)
    except:
        continue
    else:
        print(i)
    finally:
        print(i)
# to specifically know what kind of error in try block
a =45
b =[0]
for i in b:
    try:
        print(a/i)
    except Exception as aru:
        print(aru)              # o/p---division by zero

# oops---object oriented programming language
# class with inheritance
class Calcu_lation:
    def __init__(self,salary,age):
        self.salary =salary
        self.age =age
    def Increment(self,b):
        self.salary =self.salary*b
        self.age =self.age+1
        return self.salary,self.age
class Principal(Calcu_lation):
    def __init__(self, *args):
        super().__init__(*args)
class Teacher(Calcu_lation):
    def __init__(self, *args):
        super().__init__(*args)

p1 =Principal(50000,45)
print(p1.__dict__)
print(p1.Increment(2))
print(p1.__dict__)
t1 =Teacher(20000,25)
print(t1.__dict__)
print(t1.Increment(2))
print(t1.__dict__)
print(t1.salary)
print(type(t1.salary))

# operator overloading
class Changing_operator:
    def __init__(self,a):
        self.a=a
    def __add__(self,b):
        return (self.a*b.a)*2
#v1 = Changing_operator(3)
#v2 = Changing_operator(5)
print(Changing_operator(3)+Changing_operator(5))
#print(v1.a)
#print(v2.a)





        




    

    










        
             


