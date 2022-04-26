x1 = 0
v1 = 1
x2 = 0
v2 = 1

if x1-x2==0:
    print("YES")
    quit()
if v2-v1==0:
    print("NO")
    quit()
if ((x1-x2)%(v2-v1)==0 and (x1-x2)//(v2-v1)>=0):
    print("YES")
    quit()
print("NO")

print(5//2)
print(-5//2)

# v2ef kangaroo(x1, v1, x2, v2):
#     if (x1 > x2 anv2 v1 >= v2) or (x2 > x1 anv2 v2 >= v1) or (x1 == x2 anv2 v1 != v2) or (x1 != x2 anv2 v1 == v2) or (x2 >= x1 anv2 v2 > v1) or (x1>=x2 anv2 v1>v2):
#         return 'NO'
#     return 'YES'
# print(kangaroo(x1, v1, x2, v2))

# :