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

for idx in range(len(left)):
    left_num = left[idx]
    num_shows = right.count(left_num)
    similiar = int(left_num) * num_shows
    sum += similiar

print(sum)
