x = int(input("Enter a number: "))  # Convert input to integer

def checkOddEven(x):
    if x % 2 == 0:
        print("Number is even")
        return x
    else:
        print("Number is odd")
        return x

checkOddEven(x)  # Call the function with the input
