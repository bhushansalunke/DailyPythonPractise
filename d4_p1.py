# Check the status - Python
# Difficulty: EasyAccuracy: 20.06%Submissions: 143K+Points: 2Average Time: 5m
#
# Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.
#
# Return True for the following cases:
#
#     Either a or b (not both) is non-negative and the flag is false.
#     Both a and b are negative and the flag is true.
#
# Otherwise, return False.
def checkvariable(a, b, flag):
    # Check if either a or b is non-negative and flag is false
    if (a >= 0) ^ (b >= 0) and not flag:
        return True
    # Check if both a and b are negative and flag is true
    elif a < 0 and b < 0 and flag:
        return True
    # Otherwise, return False
    return False
# Example usage
print(checkvariable(5, -3, False))  # Expected output: True
print(checkvariable(-1, -2, True))   # Expected output: True
print(checkvariable(1, 2, False))    # Expected output: False
print(checkvariable(-1, 2, False))   # Expected output: False
