def fact(n):
   if n==1:
      return n
   else:
      return n*fact(n-1)
a=int(input("Enter a number:"))
num=fact(a)
print("Factorial value of %d is %d"%(a,num))


