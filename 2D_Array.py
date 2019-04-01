# Given a 6x6 2D Array, arr:
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:
#
# a b c
#   d
# e f g
# There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for
#    every hourglass in , then print the maximum hourglass sum.
#
# For example, given the 2D array:
#
# -9 -9 -9  1 1 1
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
# We calculate the following  hourglass values:
#
# -63, -34, -9, 12,
# -10, 0, 28, 23,
# -27, -11, -2, 10,
# 9, 17, 25, 18
# Our highest hourglass value is  from the hourglass:
#
# 0 4 3
#   1
# 8 6 6
# Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.
#
# Function Description
#
# Complete the function hourglassSum in the editor below. It should return an integer, the maximum hourglass sum in the array.
#
# hourglassSum has the following parameter(s):
#
# arr: an array of integers
# Input Format
#
# Each of the  lines of inputs  contains  space-separated integers .
#
# Constraints
#
# Output Format
#
# Print the largest (maximum) hourglass sum found in .
#
# Sample Input
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
# Sample Output
#
# 19
# Explanation
#
#  contains the following hourglasses:
#
# image
#
# The hourglass with the maximum sum () is:
#
# 2 4 4
#   2
# 1 2 4



#==============================================================================
# Solution
#==============================================================================
def hourglassSum(arr):
    largest_sum = 0
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            top_1 = arr[i][j]
            #print(top_1)
            top_2 = arr[i][j+1]
            top_3 = arr[i][j+2]
            middle = arr[i+1][j+1]
            bottom_1 = arr[i+2][j]
            bottom_2 = arr[i+2][j+1]
            bottom_3 = arr[i+2][j+2]
            new_sum = top_1+top_2+top_3+middle+bottom_1+bottom_2+bottom_3
            if new_sum > largest_sum:
                largest_sum = new_sum

    return(largest_sum)
