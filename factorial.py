def factorial(x):
   if x == 1:
       return 1
   else:
       return(x * factorial(x-1))
num=int(input("Enter a number: "))
print("The factorial of",num,"is",factorial(num))
