# Function With Return Value
# Difficulty: BasicAccuracy: 62.86%Submissions: 22K+Points: 1Average Time: 10m
#
# Here one integer n is given. You need to write the complete function returnValueFunction that takes n as a parameter and uses the return keyword to return double the value of n.
#
# Examples:
#
# Input: n = 2
# Output: 4
# Explanation: 2 * 2 = 4

def returnValueFunction(n):
    value = 2 * n
    return value

# Get user input and convert it to an integer
n = int(input("Enter your number: "))
result = returnValueFunction(n)

# Print the result
print(result)
