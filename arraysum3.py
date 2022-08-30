a = [1,2,1,3,2,1,1,1,0]
lst = []
for i in range(len(a)):
    # print(i)
    n = a[i]
    for j in range(i + 1, len(a)):
        if n < 4:
            if n == 3:
                v = (i, j-1)
                lst.append(v)
                break
            else:
                n = n + a[j]
        else:
            break
print(lst)









