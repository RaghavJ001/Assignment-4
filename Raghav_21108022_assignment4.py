# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 22:12:58 2022

@author: Raghav
"""

#Made by- Raghav Jindal
#SID- 21108022
#Branch- Metallurgy

#Question 1

a=int(input("Enter your marks: "))
if a>=80:
    print("Your grade is 'A'.")
elif a>=60:
    print("Your grade is 'B'.")
elif a>=50:
    print("Your grade is 'C'.")
elif a>=45:
    print("Your grade is 'D'.")
elif a>=25:
    print("Your grade is 'E'.")
else:
    print("Your grade is 'F'.")
    


#Question 2

a=int(input("Enter a year: "))
if(a%400==0 and a%100==0):
   print(a,"is a leap year")
elif(a%4==0 and a%100!=0):
   print(a,"is a leap year")
else:
   print(a,"is not a leap year")



#Question 3

import random

i=0
while i<10:
   num1=random.randint(0,10)
   num2=random.randint(0,10)

   print("Solve {}*{}=".format(num1,num2))
   ans=int(input("Enter the answer:"))
   if ans==num1*num2:
      print("Right!")
   else:
       print("Wrong!,the answer is",num1*num2)
   i+=1



#Question 4

for candies in range(200):
  if candies % 5==2:
      if candies % 6==3:
          if candies % 7==2:
              print(candies,"candies are in the bowl")
              
              
    