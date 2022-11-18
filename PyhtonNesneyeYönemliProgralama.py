# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:21:11 2020

@author: tolga
"""
#class 
#object

class Person:
    
    adress  = "no information"
    def  __init__(self, name , year):# selfin anlamı this demek
     self.name=name    #constructor object  oluşturulunca oluşur
     self.year = year
     print("init metodu çalıştı.")
   
    
    def info(self):
         print("name is" + str(self.name) + "year is " + str(self.year))
    # pass # classın hata vermesini engeller
    # accesing object attributes
  
p1=Person("tolga", 1990) ## p1 objectisi üzerinde methodlara ve attributelara ulaşmasını sağlar   
p1.name="ahmet"   # set metodu
p1.adress="kocali"
p2=Person(name = "yağmur",year =1995)
p2.info()
print(f"p1 name :  {p1.name} year : {p1.year} adress : {p1.adress}") ## bu direk methodsuz çalıştırır
print(f"p2 name :  {p2.name} year : {p2.year} adress : {p2.adress}")
print(type(p1)) #ë veri tipini türünü gösteriyor
print(type(p2))

#METHOD----------------------------------------
class Student:
    adress = "no information"
    def __init__(self,name,year):
        self.name=name
        self.year=name
    
    #instance methods
    def intro(self):
        print("hello there " + self.name)
        
    # def calculate(self) :
    #     return 2019-self.year

s1=Student("ahmet",1995)
s1.intro()
#print(f"my name is : {s1.name } and my age is :str{s1.calculate()}")


class Circle:
    #"class object attribute
    pi = 3.14
    def __init__(self, radius =1): # yarıçap göndermezsek  raiduse equals 1
        self.radius=radius
    
    #methods
    def calculateperimeter(self):
        return 2*self.pi * self.radius
    
    def CalculateArea(self):
        return self.pi*(self.radius**2)
    
    
c1 = Circle()# yarıçap 1 e eşitlenir   eğer yarıçap göndermezsek
c2 = Circle(5)
print(f"c1 : alan = {c1.CalculateArea()} perimeter ={c1.calculateperimeter()}")
print(f"c2 : alan = {c2.CalculateArea()} perimeter ={c2.calculateperimeter()}")

#Kalıtım (ınheritance)---------------------------

class Person:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname =lastname
        print ("person created")
        
    def who_am_i (self):
        print("ı am person")
        
    def eat   (self ):
        print ("ı am eating")

class Student(Person): # (person) help to extends person class
    def __init__ (self,firstname,lastname,number): # burayaa eklemeliyiz . javada olduğu gibi
        Person.__init__(self,firstname,lastname) # personu ezmeyi engeller
        self.number=number
        print("student created") 
        
    def who_am_i(self): # override personda ki metdou ezdik
        print("ı am student")
     
    def sayHello(self):
        print("hello ı am a student")
        
        
class Teacher(Person):
  def __int__(self,firstname,lastname,branch):
         Person.__init__(self, firstname, lastname)
         self.branch=branch
         
  def who_am_i(self):
     print(f"ı am a {self.branch} teacher")

             
#p1 = Person()
p1=Person("ali", "yılmaz")
s1=Student("çınar","turan",1256)
print(p1.firstname + " "+ p1.lastname)
print(s1.firstname + " "+ s1.lastname+ " " + str(s1.number)) # str içine almayı unutma

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()# bunu  yalnıca student üzerinden çağırabilirsin
#t1=Teacher("ahmet","mehmet","Math")
#t1.who_am_i()

#Özel Metodlar------------------------------------------------------------------

myList= [1,2,3]
myString = "my string"
print (len(myString))
print(len(myList))
print(type(myString))
print(type(myList))


class Movie():
    def __init__(self, title, director,duration):
        self.title=title
        self.director=director
        self.duration = duration
        print("movie objesi oluşturuldu")
    def __str__(self):
        return f"{self.title} by {self.director}" 
    def __len__(self):
        return self.duration
    def __del__(self): # del ile obje silinir ama bu metod çalışarak uyarı verir
        print ("movie silindi") # eğer obje kullanılmazsa del metodu olmazsa bile siler
        
m=Movie("film adı","yönetmen",120)
# print(myList)
# print(type(m))

print(m) # adresi verir def str oldu print str metodunu çalıştırdı

#print(len(m))

#del m # del ojeyi silmeye yarıyor

#print(m)



















