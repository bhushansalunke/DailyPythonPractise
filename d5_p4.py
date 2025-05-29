# Fibonacci series up to Nth term
# Difficulty: EasyAccuracy: 51.0%Submissions: 56K+Points: 2Average Time: 20m
#
# You are given an integer n, return the fibonacci series till the nth(0-based indexing) term. Since the terms can become very large return the terms modulo 109+7.
#
# Example 1:
#
# Input:
# n = 5
# Output:
# 0 1 1 2 3 5
# Explanation:
# 0 1 1 2 3 5 is the Fibonacci series up to the 5th term.
#
# Example 2:
#
# Input:
# n = 10
# Output:
# 0 1 1 2 3 5 8 13 21 34 55
# Explanation:
# 0 1 1 2 3 5 8 13 21 34 55 is the Fibonacci series up to the 10th term.
#
# Your Task:
# You don't need to read input or print anything. Your task is to complete the function Series() which takes an Integer n as input and returns a Fibonacci series up to the nth term.
#
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)
#
# Constraint:
# 1 <= n <= 105
def Series(n):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    fib_series = []  # This will hold the Fibonacci series

    # Generate Fibonacci numbers up to the nth term
    for i in range(n + 1):
        fib_series.append(a)  # Add the current Fibonacci number to the list
        a, b = b, (a + b) % (10**9 + 7)  # Update to the next Fibonacci numbers

    return fib_series

# Example usage:
print(Series(5))  # Output: [0, 1, 1, 2, 3, 5]
print(Series(10)) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
