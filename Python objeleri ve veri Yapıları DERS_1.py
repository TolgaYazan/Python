# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 00:52:03 2020

@author: tolga
"""
# y=input("1. sayı:")
# print(type(y)) # string
# print(y)

# r= input("give radius:")
# r = float(r) # input dan string gelir her zaman

# pi=3.14

# area = pi *(r**2)
# perimeter = 2*pi*r
# print("dairenin alanı:" , area)
# print( "dairenin çevresi " , perimeter)

# print("dairenin alanı:" +  str(area))   same with obeve lines
# print( "dairenin çevresi " + str(perimeter))

# name = "selçuk"
# surname = "tolga"
# age = 30
#age = "30"

# print ("My name is " + name + " " + surname + " and \nI am " + str(age) + " years old")
# print(name[0]) # s string ifadenin her bir ifadesi index olarak tanımlanmıştır
# print(len(name)) # name karakterini kaç tane indexden oluştuğunu gösterir 
# #note that " (çift tınakda karakter olarak tanımlanır)
# print (name[-1]) # sondan başlayarak yazar
# print (name[2:5]) # 2 dne başlayarak 5 . indexe kadar yazdırır
# print(name[3:])
# print(name[:15])
# print(name[1:6:2]) # 1 den başlaraya 5 . indexe kadar 2 index atlayarak alır

# String formatlama------------


# name = "Çınar"
# surname = "Turan"
# print ("my name is {}".format(name)) #  format süslü parantezin yerine atar ve direk yazdırır
# print ("my name is {1} {0}".format(name, surname) ) # name ve surname yerlerini değişterebilirsin
# print("my name is {n} {s} and I am {k} years old".format(n=name, s = surname , k = 36)) # yukardakiyle aynı
# # result = 200/700
# # print("the result is {r:1.4}".format(r=result)) #1 tam kısım kaç karakter yazdırmak için 4 ise ondalık kısım için kaç karakterli kısım yazdırmasını söyler

# # print(f"my name is {name}{surname}and I am {age} years old" )
# # # başına f koyup direk yazabiliriz

# # Karakter dizileri ------

# website = "http://www.sadikTuran.com"
# course = "phton kursu: baştan sona progralam rehberiniz(40 saa)"
# #1
# print (len(website))
# print (website[7:10])
# print (website[:15])
# print(course[-15:])# son başlaası için -1 yapılır ama biz -15 den başlatıyoz
# print(len(course))
# print(course[::-1]) # sağdan olsa yazdırma
# # [::] ifadesi tüm stringi al demek
# s= "12345" *5  # 12345123451234512345 output
# print(s[::5]) # :: yan yana iki nokta tüm ifadeyi almayı sağlar 5 ise  5 karakterde bir al demek

# #yukarıda verilen deşikenleri ekradan aşağıdaki ifadeyi yazdırın.
# # benim adım bora ylmaz , yaşıma 32 ve mesleiğim mühendis

# name,surname,age,job = "Bora", "yılmaz", 32 , "mühendis"
# print(f"benim adım {name} {surname}, yaşım {age}, my job is {job}") # veya asağıdaki yollar yazabilirsin
# print("benim adım {} {} , yaşıma {} ve mesleiğim {}".format(name, surname ,age,job) # süslü paratezlerini içine rakamlar yazarak yer değiştrebiliriz
# )
# print("benim adım " + name + " " + surname + ", Yaşım " + str(age) + " ve mesleğim" + job)
# # "hello word" ifadesindki w harfini "w" ile değiştirin
# k="W"
# print ("hello {}ord".format(k))
# # another way
# s = "Hello World"
# s= s[0:6 ] + "W" + s[-4:]
# print(s)
# #another way
# s.replace("w", "W") # karakter alır ve yerini değiştir
# print(s)
# #abc ifadesini yan yanayan 3 defa yazdırın

# string = "abc"
# print(string*3)

# #String methodları------------------------------------------------------------------------------------------------------------------
# message = "Hello there . My name is Sadık Turan"

# message = message.upper() # bütün karaketleri büyük harfe çevirir
# message = message.lower() # bütün karakterleri küçük yapar
# message = message.title() # her  kelimin baş harfi büyük harf olur
# message = message.capitalize() # sadece ilk harf büyük harf olur

# message = message.strip() # kulanıcan gelen mesajı ele alır başında boşluk varsa onu siler
#message = message.split() # kullanıcın boşluk karakterlerinden böler kelimeler ayrı ayrı gelir
# message = message.split(".") # karakter veriyoz ve o karaktere göre böler ve array içine koyar
#message= "* ".join(message) # ayırılmıi elamanları birleştirip ve * koyar

#index =message.find("Sadık") # verilen kelimeyi strin içinde arar 
# ve bulduğu kelimenin index numarını yadırır
#index =message.find("Sadıkk") # eğer kelim yoksa -1 veir buda kelimenin cümle içinde olmadığını söyler
#print(index)

#isFound = message.startswith("H") # string verilen karakter ile mi başlıyor onu test eder doğru ise true verir
# cevap yanlışsa false verir
# isFound = message.endswith("N") # hangi karakter ile bittiğine bakar verilen karakter doğru ise true verir
# print(isFound) 
# # print(message)
# #print(message[0]) # split dizinin elamanlarını bulmamıza yardım eder , hello gelcek

# # #message = message.replace("Sadık" , "Çınar") # replave kelimeyi arar ve verilen 2. argüment ile yerlerini değiştirir
# # message = message.replace("Sadık" , "Çınar").replace(" ", "*").replace("T","b")

# # message = message.center(100,"*") # 100 karakterlerik bir alan oluşuturup onu ortalar sağ ve soldan böler
# # yanına karakter koyup boş yerlere karakter koyabiliriz
# # print(message)

# #String methodları Uygulama----------------------------------------------------------------------------------------------

# website ="http://www.sadikturan.com"
# course= "Python Kursu : Baştan Sona Python Progralama Rehberiniz(40 saat)"

# #"Hello World" karakter dizisinin baş ve sondaki boşluk karaterlerini silin.
 
# word= "  Hello world  "
# word1=word.strip()
# print(word1)

# #"www.sadikturan.com" içindeki saidkturan bilgisi haricindeki her karakteri silin

# result=website.lstrip(":/htp")
# print(result)

# #"couser" karakter disinin tüm karaktelrini küçük harf yapın
# course= course.lower()
# print(course)

# #"website içinde kaç tane a karakteri vardır

# result1=website.count("a") # counse verilen karakterleri sayar
# #result1 = website.count("www",0,10) wwww kelimesini 0 ile 10. index arasında bulu ve sayar
# print(result1)

# #"website" "www" ile başlayıp com ile bitiyor mu?
# #isFound=website.startswith("http://")

# # isFound=website.endswith(".com")
# # print(isFound)

# #"website içinde ".com ifadedi var mı


# isFound = website.find(".com")
# # isFound = website.find(".com",0,10) # . com ifadesini 0 ile 10 . index arasında bulur varsa başladığı indexi verir yoksa -1  verir
# isFound = course.rfind("python") # rfind sağdan başlayarak araar ve bulur 
# isFound = website.index(".com") # find ile aynı
# isFound = website.rindex(".com") #sağdan başlayarak yazdırır eğer kelime yok ise hata verir find olduğu gibi -1 vermez!!1
# print(isFound)

# #"course içindeki karakterlerin hepsi alfabetik mi?(isAlptha, isdigit)

# isFound = course.isalpha() # false verir çünkü hepsi albatik karakter değil
# isFound = "Hello".isalpha() # true verir çünkü hepsi char
# isFound = course.isdigit() # false verir çünkü alfavetik değerler var içinde
# isFound = "123".isdigit() #) true verir çünkü hepsi doğru
# # note that if you use isdigit or isalpha "all characters" have to be digit or char otheerwise it gives false
# print(isFound)

# #"contens ifadisi satırda 50 karakter içine yerleştirpi sağ ve solunda * ekleyiniz

# value = "contents"

# print(value.center(50,"*")) # bu sağdan ve soldan yer açar
# print(value.ljust(50,"*")) # yalnızca sağ tarafa 50 satırlık yer açar ve yıldız ekler
# print(value.rjust(50,"*"))# yalnızca sağ tarafdan yer açar ve yıldız ekler
# #"course karakter dizinin tüm boşluk karakterlerini "-" ile değiştirin

# result = course.replace(" ", "-")

# # "heelo world" disinin "world ifadesibkie "there olarak değiştirin

# word = "Hello World"
# result = word.replace("World", "there")
# #print(result)

# # "course karakter dizisinin boşluk karaktelrinden ayırın
# result = course.split()
# result=result[0] # python
# print(result)

#Python Listeler---------------------------------------------------------------------------------------------------------------

message = "Hello There.My name is Sadık Turan".split()
# print(message[0])


# my_List = [1,2,3] #Array list
# my_List = ["bir",2,True,5.6]
# print(my_List)

list1 = ["one","two","three"]
list2 = ["four","five","six"]
numbers = list1 + list2 # list leri topladık
print(numbers) 
print(len(numbers))  # 6 verir
print(message[0]) # hello verir
print(numbers[2])

userA = ["sadık ",32]
userB = ["çınar",2]

users = [userA , userB] # listeleri yeni liste gibi kullanmımıza sağlar

print(userA)
print(userB)
print(users) # liste içinde yeni bir liste oldu
print(users[1]) # ["çınar",2] verir
a = users[1]
print(a[0]) # çınar verir 
#another way
print(users[1][0]) # yine çınar verir

#Uygulama -Python Listeler---------------------------------------------------------- -----------------------------
#-1- "bmw mercedes opel mazda" elamnalarına sahip bir liste oluşturunuz

cars= ["bmw", "mercedes", "opel","mazda"]
print(len(cars))
print(cars[0] +" " + cars[3]) # veya cars[-1](mazda) cars[-4](bmw)

#-2- Mazda değerini Toyota ile değitirin
cars[3] = "toyota" # veya cars[-1] ="toyota
print(cars)

#"mercedes listenin bir elamınmıdır
isFound = cars.index("toyota") # indexi verir veya 
isFound = "mercedes" in cars # true verir yanlış olursa false verir
print(isFound)

#listenin -2 indeksindeki değer nedir
print(cars[-2])

# listenin ilk 3 ifadesini alınr
result = cars[0:3] # stringdeki gibi
result= cars[:3]
print(result)

#-8- lisetinin son 2 elamını yerine "toyota" ve "renault" değerlerini ekleyin

# cars[-1] = "toyota"
# cars[-2] = "renault"
#another way
cars[-2:] = ["toyota", "Renault"]
print(cars)

#-9- listenin üzerine "audi ve "nissan değerlerin ekleyin
# cars1= ["audi" , "nissan"]
# cars = cars1+cars
# another way

cars = cars + ["audi ","nissan"]
print(cars)

#-10- listenin son elamanın silin
del cars[-1]
print(cars)

#-11- liste elamanlarını reverse yazdır

print(cars[::-1])

#-12-Aşağıdaki verileri bir liste içinde saklayınız.

stdA = ["yiğit", "bilgi",2010 , [70,60,70]]
stdB = ["Serna" , "turan", 1999, [80,80,70]]
stdC = ["ahmet","turan" ,1998, [80,70,90]]

result = stdA + stdB + stdC # listeleri ekleyip beraber yazdırır

result= stdA[0] #yiğit verir
result = stdC[3][1] # 70 verir

result = f"{stdA[0]} {stdA[1]} {2020-stdA[2]} yaşında ve not ortalaması {(stdA[3][0] + stdA[3][1] + stdA[3][2])/3}"
# yiğiy bilgi 9 10 yaşında ve not ortalaması 66.666 çıkar


print(result)

#Liste metodları--------------------------------------------------------------------------------------

numbers = [1,10,5,16,4,9,10]
# letters = ["a","b ", "s", "b","y","a","s"]

# val = min(numbers) # numbers içinde minimum değeri verir
# val = max (numbers) # numbers içinde max değeri verir
# val = max(letters) # alfabtik sıraya bakar ve "y" ifadesini verir
# val = min(letters) # alfabetik olara bakar ve "a" ifadesini verir
# val = numbers[3:6] # 16, 4 ,9 verir
# val =  numbers[:3] # 0 dan başlayara 3. indexe kadar yazdırır  "1,10,5"
# val = numbers [4:] # 4.indexden başlar ve sona kadar gider
# numbers[4] = 40 # 4. indexi değiştirdik
# numbers.append(50) # sonunda 50 rakamı eklenir
# numbers.insert(5, 78) # insert metodu indexe göre rakam eklmemizi sağalr 5 .indexe 78 ekledik
# numbers.insert(-1, 80) # -1 ile en sona rakam ekleyebilirz
# numbers.pop()# elamanları bununla sileriz
# numbers.pop(4) # 4.indexdeki rakamı siler
# numbers.remove(1) # bunda karakter vererek sildiriyoruz

# numbers.sort() # liste sayısal olarak sıralanır
# letters.sort() # alfabetik olara sıralanır
# numbers.reverse() # ters çevirir
# letters.reverse()#ters çevirir


# print(numbers)
# print(letters)
# print(len(numbers)) # 7 verir
# print(numbers.count(10)) # 2 verir count metodu listeni içinde verilen elamanı sayar
# numbers.clear() # liste içinde bütün elamanları siler
# print(numbers)

#Uygulamaa Python Liste metodları-----------------------------------------------------------

names = ["ali","yağmur","hakan","deniz"]
years = [1998,2000,1998,1987]

#-1- "cenk" ismini listenin sonuna ekleyinz

names.append("cenk")

#-2- "sena değerini listenin başına ekleyiniz

names.insert(0,"sena")

#-3- "deniz ismini listeden siliniz

# names.remove("deniz")

#-4- deniz ismini indexi nedir

result=names.index("deniz")

print(result)
#-5- "ali listenin bir elamanı mıdır?

# result = "ali" in names
# result = names.index("ali") # ali listenin bir elamnı değil ise hata verir
# print(result)

# #-6-liste elamnalrı terse çeviriniz
# names.reverse()

# #-7- liste elamanarlı alfabetik olarak sıralayınız
# names.sort()
# #-8- years listesindeki rakamsal büyüklük olarak sıralıyınız
# years.sort() 

# #-9- str="Chevrolet,Dacia" karakter dizini listeye çevirin

# str = "Chevroler , Dacia"
# list = [str]


# print(names)
# print(years)
# print(list)
# #10- years dizisinin en büyük ve en küçük elamnı nedir?

# val = min(years)
# val = max(years)
# print(val)

# #11- years dizisinde kaç tane 1998 değeri vardır?

# result = years.count(1995)
# print(result) # eğer elamnı yoksa 0 verir

# #12- years dizisinin tüm elamanları silin

# # years.clear()
# print(years)

#13-kullanıcın alacağınız 3 tane marka bilgisini bir listede saklayınız

# markalar = []

# marka= input("marka: ")
# markalar.append(marka)

# marka= input("marka: ")
# markalar.append(marka)

# marka= input("marka: ")
# markalar.append(marka)

# print(markalar)

#input alma

#Python da Tuple--------------------------------------------------------------------------------------

list = [1,2,3]

tuple = (1, "iki", 3)

# print(type(list))
# print(type(tuple)) 

# print(list[2])
# print(tuple[2])

# print(len(tuple))
# print(len(list))

list = ["ali","veli"] # bu önceki içeriği siler ve farklı bir içerik yükler

tuple = ("damla","ayşe","ayşe")

names = ("demet ", "tolga","mehmet" ) + tuple # eklemeye yapabiliyoz

print(names)
list[0] = "ahmet" # ali ahmet diye değişir
# tuple[0] = "deniz" # hata verir çünkü tuple listesine bir obje atamayız


result=tuple.count("damla")
result = tuple.index("ayşe") # ayşe ilk nerde index verir
print(result)
print(tuple)
print(list)


#!!!!! tuple ile liste aynı ama tuple da index verip elaman güncellemesi yapamıyoruz

#Pythonda Dictinary----------------------------------------------------------------------------

# dictinory bir liste türü

#key -value

#41 = > kocaeli 34 = > istanbul

# sehirler = ["kocaeli", "istanbul"]
# plakalar = [41,34]

# print(plakalar [sehirler.index("kocaeli")]) # 41 verir

# print(plakalar[sehirler.index("istanbul")])

# #print(plakalar["istanbul]) = >41
# #print(plakaler ["kocaeli"]) = >34

# plakalar = {"kocaeli" : 41, "istanbul":34} # sülü parantez kullandık istabulu 34 e kocaleini 41 e atadık
#             #key# value ilişkisi
# print(plakalar["istanbul"]) # 34 verir
# print(plakalar["kocaeli"]) # 41 verir çünkü yukarda atadık

# plakalar ["ankara" ] = 6
# print(plakalar) # ankara : 6 verir ve yeni değer olarak atar üstüne ekler

# plakalar["kocaeli"] = "new value" # güncelleme yapabiliyoz
# print (plakalar) # kocaelini values isni "new value" yaptık


users =  {
    "sadikturan" : {
        "age " : 36,
        "roles" : ["user"],
        "email ": "sadik@gmail.com",
        "adress " : "kocaeli",
        "phone" : "12345"
        
        }, # burdaki virgülü unutma
    "çınarturan" : {
        "age" : 21,
        "role" : ["admin","user"],
        "email": "sadikbebek@gmail.com",
        "adress" : "istanbul", # iki nokta ile değer atıyosun
        "phone" : "12345"
        
        }

    }

print(users["çınarturan"]) # çınarturan hakkında tanımladğımız bütün değerleri  verir
# print(users["çınarturan"]["age"]) # 21 verir
# print(users["çınarturan"]["email"]) # sadikbebek@gmail.com verir
# print(users["çınarturan"]["adress"]) #"istanbul verir

print(users["çınarturan"]["role"])# admin users verir
print(users["çınarturan"]["role"][0]) # admin verir

#!!!!!! bir değerlerer bir değer atıyoruz key - values ilişkisi

#UYGULUMA PYTHON DICTIONARY-----------------------------------------------------------------------------------






