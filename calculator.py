'''
num3 = []
num5 = []
num3_5 = []
for i in range(0,1000):
    if (i % 3 == 0):
        num3.append(i)
    if (i % 5 == 0):
        num5.append(i)
    if (i % 3 == 0) and (i % 5 == 0):
        num3_5.append(i)
sum_all = sum(num3) + sum(num5) - sum(num3_5)
print(num3_5)

print(str(sum_all))
'''

sum_all = 0
for i in range(0,1000000000):
    if (i % 3 == 0) or (i % 5 == 0):
        sum_all += i
print(str(sum_all))
