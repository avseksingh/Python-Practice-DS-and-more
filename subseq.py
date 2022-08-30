l= [10,20,5,11,13,15,0,12,15,45,145]
subseq = [[]]
for e in l:
    if not subseq[-1] or subseq[-1][-1] <= e:
        subseq[-1].append(e)
    else:
        subseq.append([e])
print(l)
print(subseq)
print(max(subseq, key=len))