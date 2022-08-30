# a = [4,2,1,5,3]
a = [5,6,2,3,1,7]
n = len(a)
for i in range(1,n):
    if a[i-1] > a[i]:
        a[i-1] = a[i]
    else:
        a[i-1] = -1
    if i == n - 1:
        a[i] = -1
print(a)