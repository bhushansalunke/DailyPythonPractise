# Juggler Sequence
# Difficulty: EasyAccuracy: 52.04%Submissions: 42K+Points: 2Average Time: 10m
#
# Juggler Sequence is a series of integers in which the first term starts with a positive integer number a and the remaining terms are generated from the immediate previous term using the below recurrence relation:
#
# Juggler Formula
#
# Given a number n, find the Juggler Sequence for this number as the first term of the sequence until it becomes 1.
#
#
# Example 1:
#
# Input: n = 9
# Output: 9 27 140 11 36 6 2 1
# Explaination: We start with 9 and use
# above formula to get next terms.
#
#
#
# Example 2:
#
# Input: n = 6
# Output: 6 2 1
# Explaination:
# [61/2] = 2.
# [21/2] = 1.
#
#
#
# Your Task:
# You do not need to read input or print anything. Your Task is to complete the function jugglerSequence() which takes n as the input parameter and returns a list of integers denoting the generated sequence.
#
#
#
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)
#
#
#
# Constraints:
# 1 ≤ n ≤ 100

def integer_square_root(x):
    """Calculate the integer square root of x without using math functions."""
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    if x == 0:
        return 0
    # Start checking from 1 upwards
    for i in range(1, x + 1):
        if i * i > x:
            return i - 1  # Return the largest integer whose square is <= x


def jugglerSequence(n):
    sequence = []  # Create an empty list to store the sequence

    while n > 1:  # Continue until n becomes 1
        sequence.append(n)  # Add the current n to the sequence
        if n % 2 == 0:  # Check if n is even
            n = integer_square_root(n)  # Get the integer square root of n
        else:  # If n is odd
            n = integer_square_root(n * n * n)  # Get the integer square root of n^3

    sequence.append(1)  # Finally, add 1 to the sequence
    return sequence  # Return the complete sequence


# Example usage
print(jugglerSequence(9))  # Output: [9, 27, 140, 11, 36, 6, 2, 1]
print(jugglerSequence(6))  # Output: [6, 2, 1]
