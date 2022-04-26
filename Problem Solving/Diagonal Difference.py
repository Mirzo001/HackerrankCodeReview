# arr = [3][ 1, 2, 3,
#            4, 5, 6,
#            9, 8, 9,]

arr = [
    [1,2,3], 
    [4,5,6], 
    [9,8,9]
    ]

def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                left_to_right += arr[i][j]  
            if i + j + 1 == len(arr):
                right_to_left += arr[i][j]
    absolute_difference = left_to_right - right_to_left
    return abs(absolute_difference)
print(diagonalDifference(arr))