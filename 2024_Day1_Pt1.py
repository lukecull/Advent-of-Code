import sys

lines = []
inputs = []
right = []
left = []
sum = 0

for line in sys.stdin:
    lines.append(line.rstrip('\n'))

for inp in lines:
    inp = inp.split()
    inputs.append(inp)

for i in inputs:
    left.append(i[0])
    right.append(i[1])

left.sort()
right.sort()
for num in range(len(left)):
    dist = int(left[num]) - int(right[num])
    if (dist) >= 0:
        sum += dist
    if dist < 0:
        dist = int(right[num]) - int(left[num])
        sum += dist
print(sum)