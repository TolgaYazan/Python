# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:26:25 2020

@author: Murat
"""

class A:
    def __init__(self,a=10, b=20):
        self.a = a
        self.b= b
        
    def sumA(self):
        return self.a + self.b
    
    def totalA(self, a, b):
        return self.a + self.b + a + b
    
    def average (self, a , b, c):
        return (a + b + c)/c
    
    def mix(self, a, b):
        return self.sumA() + self.totalA(a,b)

class B:
    def __init__(self, c,d):
        self.a = c
        self.b = d
    
    def mulB(self):
        return self.a * self.b
    
    def sumAB(self,a,b):
        return self.mulB()+ A.totalA(self, a, b)
    
class C:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
     
    def hello(self):
        print("Hello CMPE 261 ")
    
    def info(self):
        print (" IN the class C,data are: A = " + str(self.a)+ " B is "+ str(self.b)+ " C is: " + str(self.c) )


#multiple inheritance

class D (A,B,C):
    def __init__(self,a,b,c,name):
        A.__init__(self,a,b)
        B.__init__(self,a,b)
        C.__init__(self,a,b,c)
        self.name = name
        
    def myName(self):
        print("My name is:" +self.name)
    

    
    
    
    
a = A(10,30)
print(a.sumA())
print(a.mix(2,3))


a1 = A()
print(a1.sumA())
print(a1.mix(2,3))

print ("B class")
b = B(10,20)


print(b.mulB())
print(b.sumAB(1,2))
print("C class")
c = C(1,2,3)
c.info()

print(" Test class D")
d = D(1,2,3, " Bilgi")
d.myName()
d.info()
print(d.sumAB(20,30))
print(d.average(10,20,30))
