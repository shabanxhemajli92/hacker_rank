"""
This problem is asking you to write a function in Python that takes a square matrix represented as a 2D array of integers, and calculates the absolute difference between the sums of its two diagonals. The primary diagonal is the diagonal from the top-left corner to the bottom-right corner, and the secondary diagonal is the diagonal from the top-right corner to the bottom-left corner. The function should return a single integer, which is the absolute difference between the two diagonal sums.

To solve this problem, you can iterate through the array and add up the elements on the primary and secondary diagonals separately, then calculate the absolute difference between the two sums and return that value. You can use a nested for loop to iterate through the array, and use the indices of the loop to determine which elements belong to the primary and secondary diagonals.
"""
#solution
def diagonalDifference(arr):
    primary_sum = 0
    secondary_sum = 0
    n = len(arr)
    
    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n-i-1]
    
    return abs(primary_sum - secondary_sum)
