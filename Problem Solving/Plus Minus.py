n = 6
arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    if n == 0:
        print("No elements found")
    proportion_positive_values = 0
    proportion_of_negative_values = 0
    proportion_of_zeros = 0
    for i in range(0, n):
        if arr[i] > 0 :
            proportion_positive_values+=1
        elif arr[i] < 0:
            proportion_of_negative_values+=1
        else:
            proportion_of_zeros+=1
    print("{:.6f}".format(proportion_positive_values/n))
    print("{:.6f}".format(proportion_of_negative_values/n))
    print("{:.6f}".format(proportion_of_zeros/n))
plusMinus(arr)

