D = open('input.txt').read()
D = str(D)
lines = D.splitlines()
keys = []
reports = []

for i, line in enumerate(lines):
    if line == '':
        reports.append(lines[i+1:])
        break
    else:
        keys.append(line)
        
print(keys)
print(reports)