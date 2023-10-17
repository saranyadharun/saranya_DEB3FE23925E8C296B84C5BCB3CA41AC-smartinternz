Year=int(input("enter the year:"))

if(Year%400==0) and (Year%100==0):
  print(Year,"is leap year") 

elif(Year%4==0) and (Year%100 !=0):
  print(Year," is leap year") 

else:
  print(Year,"is not leap year")