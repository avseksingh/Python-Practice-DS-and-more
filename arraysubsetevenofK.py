arr= [1,2,3,4,5,6,7,8,9,10]
n = len(arr)
k = 3
startpos = 0
lastpos = k-1
total = 0
evencount = 0
sum = 0
i = 0
for a in range(n):
    if a <= lastpos:
        sum = sum + arr[a]
        if lastpos < n and lastpos == a:
            lastpos += 1
            if sum%2 ==0:
                evencount += 1
            print("condition", sum)
            sum = sum - arr[i]
            i +=1

print(evencount)




