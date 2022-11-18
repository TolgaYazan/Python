# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:00:57 2020

@author: Murat
"""

class Person:
    
    number = 100;
    
    def __init__(self,name = "Bilgi", age = 20):
        self.name = name
        self.age = age
    
    def info(self):
        #print("Name is:" +self.name +" age is:" +str(self.age))
        return "Name is:" +self.name +" age is:" +str(self.age)
        
    def hello(self):
        print("Hello OOP in python")
    
    def sum(self, a, b):
        return a + b + self.number # we don't write the "self" 
    
  
class Student(Person):
    def __init__(self, name, age, dept):
        Person.__init__(self,name,age)
        self.dept = dept
        
    def  info(self):
        person = Person.info(self)
        
        #print("dept is: "+self.dept)
        return person + "dept is: "+self.dept



# test this class
        
p = Person("Ali", 34)
p.info()
p.hello()
#print(p.sum(1,2))

p2= Person()
#p2.info()

p3= Person("Ankara")
#p3.info()

s = Student("Fatma", 18, " CMPE")
#s.info()
print(s.info())







