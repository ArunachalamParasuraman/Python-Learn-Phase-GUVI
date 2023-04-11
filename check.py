# Write a code to get 2 integers A and N. Print the integer A, N times in separate line.
a =10
n =5
while(n>0):
    print(a)
    n =n-1
# IN THIS CASE IF '10' IT WILL AFFECT
a ='5'
b =4
c =a*b
for i in c:
    print(i)
# WITH USER INPUT
userInput = input()
split=userInput.split(' ')
a=int(split[0])
n=int(split[1])
while(n>0):
    print(a)
    n =n-1

#check whether its odd or even. In case of a decimal, Round off to nearest integer and then find the output. Incase the input is zero, print "Zero".
A =round(int(input()))
if A%2==0 and A!=0:
    print('Even')
elif A%2==1:
    print('Odd')
elif A==0:
    print('Zero')
#You are given A = Length of a rectangle & B = breadth of a rectangle. Find its area “C”.
A =int(input())
B =int(input())
print(A*B)
# to round off a value and according to their places
a =32.345
print(round(a))
print(round(a,1))
print(round(a,2))
A =5
B =5.234
C =A+B
print(round(C,1))
#You are given Two Numbers, A and B. If C = A + B. Find C,Round off the output to a single decimal place.
A =int(input())
B =int(input())
C =A+B
print(round(C,1))
#You will be provided with a number. Print the number of days in the month corresponding to that number
#Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".
a = int(input()) #2
if a in (1,3,5,7,8,10,12):
    print('31')
elif a in (4,6,9,11):
    print('30')
elif a==2:
    print('28')
else:
    print('Error')
#You are given three numbers A, B & C. Print the largest amongst these three numbers.
a =3 #int(input())
b =9
c =6
print(max(a,b,c))
#You are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.
#Print the output up to two decimal places (Round-off if necessary).(S.I. = P*T*R/100)
A = input()
split=A.split(' ')              #INPUT--- 1000 2 5
P =int(split[0])
R =float(split[1])
T =int(split[2])
print(round((P*(R/100)*T),2))
#Print the First 3 multiples of the given number "N". (N is a positive integer)
#print the characters with a single space between them.
a=3
n=2
list=[]
for i in range(1,a+1):
    list.append(i*n)
print(*list)
a =[1,4,5,6]
print(*a)
# write a program to print the table of 9 till N in the format as follows:
N =0
a =9
list =[]
for i in range(1,N+1):
    list.append(i*a)
print(*list)
if N==0:
    print('NULL')
#You are provided with two numbers. Find and print the smaller number.
a =5
b =9
if a<b:
    print(a)
elif b<a:
    print(b)
# Write a code to get the input and print it 5 times.
n =int(input())
a =5
while (a>0):
    print(n)
    a =a-1
# You are given with a number "N", find its cube.
N =(int(input()))**3
print(N)
# You are provided with a number, "N". Find its factorial.
N =5
for i in range(1,N):
    N =N*i
print(N)
# You are provided with the radius of a circle "A". Find the length of its circumference.
A =float(input())
if A>0 :
    print(round((2*(22/7)*A),2))
elif A<0:
    print('Error')
# You are provided with a number "N", Find the Nth term of the series: 1, 4, 9, 16, 25, 36, 49, 64, 81, .......
# (Print "Error" if N = negative value and 0 if N = 0).
N =4
if N>0:
    print(N*N)
elif N<0:
    print('Error')
elif N==0:
    print('0')
# You are given with a number A i.e. the temperature in Celcius. Write a program to convert this into Fahrenheit. 
# Note: In case of decimal values, round-off to two decimal places.
A =12
print(round((12*1.8+32),2))
# Write a code to get an integer N and print the values from N to 1.
N =10
while(N>=1):
    print(N)
    N =N-1
# Write a code to get an integer N and Print the digits of the integer in a single line separated by space.
N ='345'
print(' '.join(N))
#The area of an equilateral triangle is ¼(√3a2) where "a" represents a side of the triangle. You are provided with the side "a"
a =20
print(round(0.25*(3**0.5*a**2),2))
# Write a code to get an integer N and print the sum of  values from 1 to N.
N =10
from functools import reduce
def custom(a,b):
    return a+b
print(reduce(custom,range(1,N+1)))
# You are given a number A in Kilometers. Convert this into B: Meters and C: Centi-Metres.
A =2
B =print(A*1000)
C =print(A*100000)
# Write a program to get a string as input and reverse the string without using temporary variable.
a ='arun'
print(a[-1::-1])
# Let "A" be a year, write a program to check whether this year is a leap year or not.
A =2002
if A%4==0 and A%100!=0 or A%400==0:
    print('Y')
else:
    print('N')
# Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.
a ='30 42'
b =a.split(' ')
x =int(b[0])
y =int(b[1])
def custom_HCF(x,y):
    if x>y:
        smaller =y
    else:
        smaller =x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            HCF =i
    return HCF
print(custom_HCF(x,y))
# Write a code get an integer number as input and print the odd and even digits of the number separately.and o/p to be sorted
a =list('456213789')
b =sorted(a)
print(*list(filter(lambda b:int(b)%2==0,b)))
print(*list(filter(lambda b:int(b)%2,b)))
# Let "A"  be a string. Remove all the whitespaces and find it's length. 
a ='aruna chalam'
print(len(a.replace(' ','')))
# Write a code to get an integer N and print the even values from 1 till N in a separate line.
N =6
for i in range(1,N+1):
    if i%2==0:
        print(i)
# Given a range of 2 numbers (i.e) L and R count the number of prime numbers in the range
a ='2,5'
a =a.split(',')
L =int(a[0])
R =int(a[1])
for num in range(L,R+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)  
# Given base(B) and height(H) of a triangle find its area.
INPUT ='2 4'
a =INPUT.split(' ')
B =int(a[0])
H =int(a[1])
N =0.5*B*H
print(N)    
# Given 2 numbers N,M. Print 'yes' if their product is a perfect square else print 'no'.
x ='5 5'
a =x.split(' ')
N =int(a[0])
M =int(a[1])
if N == M:
    print('yes')
else:
    print('no')  
# Given a number N, print 'yes' if it is composite else print 'no'.
N =123
factor =0
for i in range(1,N):
    if N%i==0:
        factor =i
if factor>1:
    print('yes')
else:
    print('no')
# Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1
N,M = map(int,'10 5'.split())
if N>M:
    smaller =M
else:
    smaller =N
for i in range(1,smaller+1):
    if (N%i==0) and (M%i==0):
        GCD =i
if GCD>1:
    print(GCD)
else:
    print(-1)
# Let P represent Paper, R represent Rock and S represent Scissors. Given 2 out of the 3 determine which one wins. If its a draw print 'D'.
a =input()
if 'RP' and 'PR'in a:
    print('P')
elif 'RS'and 'SR'in a:
    print('R')
elif 'PS'and 'SP'in a:
    print('S')
else:
    print('D')
# Given a string 'S' swap the even and odd characters starting from index 1(Assume the index starts from 0).
s='codekata'
t=list(s)
t[::2],t[1::2]=t[1::2],t[::2]
c=''.join(t)
print(c)
# or
str = 'CloudiKnow'
output = ''
i = 0
while i < len(str):
        if i + 1 < len(str):
                output = output + str[i + 1]
                output = output + str[i]
        i = i + 2
print ('Given   String: ' + str)
print ('Swapped String: ' + output)

# Write a code to get a integer n as input and calculate the smallest perfect power of 2 greater than n.
n =48
for i in range(1,n):
    if (2**i)>n:
        break
print(2**i)
#You are provided with a string ‘s’. Your task is to reverse the string using stack Data Structure.
a ='i am jsb'
b =a.split()
c= b[::-1]
print(*c)
#or
a ='i am jsb'
b =a.split()
b.reverse()
print(*b)
#Given a roman numeral N, convert it into integer
def romanToInt(s):
		translations = {
			"I": 1,
			"V": 5,
			"X": 10,
			"L": 50,
			"C": 100,
			"D": 500,
			"M": 1000
		}
		number = 0
		s = s.replace("IV", "IIII").replace("IX", "VIIII")
		s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
		s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
		for char in s:
			number += translations[char]
		print(number)
        		
romanToInt('IV')

n =5
k=10
a ={10,10,20, 30, 76}
if k in a:
    a.discard(k)
    print(a)
#elif a.discard(k)=={}:
#   print('empty')
a =[1,0,3,2]
b =[4,6,5]
c =[7,9,8]
d =a+b+c
d.sort()
print(*d)

a =3
b=2
c=-1
x1 = ((-b)+((b**2)-(4*a*c))**(1/2))/2*a
print(round(x1,1))
x2 = ((-b)-((b**2)-(4*a*c))**(1/2))/2*a
print(round(x2,1))

S = 'codekata'
for i in S:
    if i in '[a,e,i,o,u]':
        print('yes')
        break
else:
    print('no')

s = 'aab'
if len(s)==3 and s[0]!=s[int(len(s)/2)]!=s[-1]:
    print(1)
else:
    print(0)

# testing exception handling

a = 45
b = 0
try:
    print(a/b)
except ZeroDivisionError:
    print(a/(b+1))








    
    

        




    


    










