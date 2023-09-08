n=int(input("Enter a year:"))
if(n%400==0):
      print("%d is a Leap Year" %n)
elif(n%100==0):
      print("%d is Not the Leap Year" %n)
elif(n%4==0):
      print("%d is a Leap Year"%n)
else:
      print("%d is Not the Leap Year" %n)