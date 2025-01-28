n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
vals = {}
for i in a:
    if i not in vals:
        vals[i] = -1
    else:
        vals[i] -= 1
for i in b:
    if i not in vals:
        vals[i] = 1
    else:
        vals[i] += 1
pos = []
for i in vals:
    if vals[i] > 0:
        pos.append(i)
pos.sort()
print(*pos)