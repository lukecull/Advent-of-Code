import re

do = True
matches = []
total = 0
D = open('input.txt').read()
matches = (re.findall(r"(do)\(\)|(don't)\(\)|mul\((\d+),(\d+)\)", D))
print(matches)
for d, dn, x, y in matches:
    if d == 'do':
        do = True
    if dn == "don't":
        do = False
    if do == True and (x != ''):
        total += int(x) * int(y)
print(total)