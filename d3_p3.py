#User function Template for python3

#Write the complete argumentFunction below.
#The function should take two arguments a and b
#The function should return a+b
#code here
def argumentFunction(a,b):
    sum = a + b
    return sum
#Write the argumentFunction above.
a=int(input("Enter value for a: "))
b=int(input("Enter value for b: "))

result=argumentFunction(a,b)
print("The sum a and b is: ",result)