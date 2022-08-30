arr = [1,2,5,3,0]
f = l = total = 0
for a in range(0,len(arr)):
     total = total + arr[a]
print(total)
f = sum(arr)
l = arr[0]
if len(arr) == 1:
    True
for i in range(1, len(arr)):
    l = l + arr[i]
    f = f - arr[i-1]
    print (l, f)
    if l == f:
        print("Found", l, f)
        break



# for a in range(0,len(arr)):
#     count = count + 1
#     print(val, total, equal, "=")
#     if total == equal:
#         print(total)
#         print(count)
#         break
#     valc = val + arr[a]
#     # valm = val +
#
#     val = val + arr[a]
#     equal = total - val
#     # if equal == 0:
#     #     print(count)
#
#
# # for a, b in zip(range(len(arr)), reversed(range(len(arr)))):
# #     tempa = tempa + arr[a]
# #     tempb = tempb + arr[b]
# #     count = count+1
# #     if tempa == tempb:
# #         print(count )
# #         print(tempa, tempb)
# #         break
