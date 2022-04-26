# n = int(input("Enter lenth of array: "))
ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
# print(type(ar))
def aVeryBigSum(ar):
    sum_arr = 0
    for i in ar:
        arr = int(i)
        sum_arr+=i
    return sum_arr
    
    
    
    

print(aVeryBigSum(ar))