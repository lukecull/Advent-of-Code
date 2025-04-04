import sys
import re

lines = []
matches = []
for line in sys.stdin: #gathers line by line inputs 
    lines.append(line.rstrip('\n'))

print(lines)
# lines = [['mul(123,4)'], ['uegfusymul(23,3)'], ['gehugedaugd']]

for i, line in enumerate(lines):
    print(line)
    matches = re.findall(r"mul\((\d+),(\d+)\)", line)

for match in matches:
    print(match)