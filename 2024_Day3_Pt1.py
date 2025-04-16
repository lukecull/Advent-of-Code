import re

lines = []
matches = []
D = open('input.txt').read()
matches = (re.findall(r"mul\((\d+),(\d+)\)", D))
total = sum(int(x) * int(y) for x, y in matches)
print(total)