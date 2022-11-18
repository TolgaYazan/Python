
print (" Hello CMPE 261")
# This is a comment line
"""
"""
# data types
data = 12
name = " Ali"
flag =True
price = 3.5
 
age = 34
 
print(type(age))
# operators
# +, - , *, / ,%, > >=i < .<=, == , !=
sum = data + age
print (" The result is: ", sum)

total = age + price

print (total)

# typecastiong 

x = int(3.5)
print(x)
d2 = "2.3"

print(d2*4)


x2 = float(d2)
print(x2*4)


x3 = 1000

x4 = str(x3)
print(x4*5," the result","  ")

print (2+3, " result", " bilgi", " ")


# boolean

y=100
z=34
p = 20

if (z > y):
    print("z is greater than y")
elif (z > p):
    print ("z is greater than p")
# pyhthon has and, or, not logic eperators... see your self
    
# loops---for loop
for t in range(5,11,2):
    print(t)


# in java: for(int i=0;i<10;i+++){ssss println(i)}
# print numbers beween 5 and 10


# decresing numbers
for n in range(20,0,-3):
    print(n)
    
# range function has 3 parameters...

print (" This is while loop")
    
w = 0
while (w < 10):
    print(w)
    w = w +3
# you can use "break", "continue" same as java, C++

# nested loops
"""
*
**
***
****
*****
"""

for i in range(5):
    for j in range(i+1):
        print("*", end = " ")
    print()
    
#  in python style...
print (" with python style")
for i in range (6):
    print(i*"*")

# arrays...list

myData = []
yourData = [10,20,30,40,50,60,70,80,90]

print(yourData)

for i in yourData:
    print(i)

print("print with index")
for i in range(len(yourData)):
    print(yourData[i])
    
yourData.append(1000)
print(yourData) 
yourData.extend([-1,-2,-3])
print(yourData)
c = [-10,-20,-30]

k = yourData + c
print(k)  

k= k+ [100,200,300,400] 

print(k)
print(len(k))

print (k[-1])

#two dimensional arary
table = [[1,2,3], [4,5,6],[7,8,9]]
print (table)

for i in table:
    print (i)


print ("print in a table shape")
for i in table:
    for j in i:
        print(j, end =" ")
    print()

print("print table with index")

for i in range(len(table)):
    for j in range(len(table[0])):
        print (table [i][j], end = " ")
    print()

## functions....
def add(a, b):
    return a + b


sum = add(2,3)
print(sum)

print (" sum of two numbers are:", add(10,30))

def hi():
    print ("hi")
    
hi()


# write a function gives us sum of array data

def sumArray(data):
    sum = 0
    for i in data:
        sum = sum + i
    return sum

print(sumArray(yourData))

#zzzz=1000;#

#print(sumArray(zzzz))

# sum of odd numbers of a table
def sumTable(myData):
    sum = 0
    for i in myData:
        for j in i:
            if (j % 2 == 1):
                sum = sum + j
    
    return sum



print(sumTable(table))





