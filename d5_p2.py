def printGfg(N):
    # Base case: if N is 0, return (stop the recursion)
    if N == 0:
        return
    # Print "GFG" followed by a space
    print("GFG", end=' ')
    # Recursive call with N decremented by 1
    printGfg(N - 1)

# Example usage
printGfg(11)