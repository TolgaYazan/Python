# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:41:06 2020

@author: tolga
"""
def hi():
    print("hi")
    
hi()   


def makeIdenyMatrix( data):
    for i in range(0, data):
        for j in range(0, data):
            if(j==i):
                print(1,end=" ")
            else:
                print(0,end = " ")
        print()          
      
                
makeIdenyMatrix(6)
makeIdenyMatrix(3)

print("quesiton 2-----")

t1 = [[1,2],
      [1,3]]
t2 = [[3,5],
      [5,6]]


def PrintTable(data1, data2): 
  result=[[0,0],[0,0]]  
  
  for i in range(len(data1)):
      for j in range(len(data2)):
          k =data1[i][j] + data2[i][j]
          result[i][j] = k
      return result

print(PrintTable(t1,t2))




  


#def dotProduct  (data , data):
 #   for i in