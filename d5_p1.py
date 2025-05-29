# First Digit of a Number
# Difficulty: EasyAccuracy: 50.61%Submissions: 28K+Points: 2Average Time: 10m
#
# Given a number n, find the first digit of the number.
#
# Examples:
#
# Input: n = 123
# Output: 1
#
# Input: n = 976
# Output: 9
#
# Constraints:
# 1 <= n <= 109
def firstDigit(n):
    # Convert the number to a string to easily access the first character
    return int(str(n)[0])

# Example usage:
print(firstDigit(123))  # Output: 1
print(firstDigit(976))  # Output: 9
