D = open('input.txt').read()
D = str(D)
lines = D.splitlines()
answ = 0
def check_X(lines, j, i):
    if (lines[j-1][i-1] == 'M' and lines[j+1][i+1] == 'S') and (lines[j-1][i+1] == 'M' and lines[j+1][i-1] == 'S'):
        return True
    elif ((lines[j-1][i-1] == 'S' and lines[j+1][i+1] == 'M') and (lines[j-1][i+1] == 'S' and lines[j+1][i-1] == 'M')):
        return True
    elif ((lines[j-1][i-1] == 'M' and lines[j+1][i+1] == 'S') and (lines[j-1][i+1] == 'S' and lines[j+1][i-1] == 'M')):
        return True
    elif ((lines[j-1][i-1] == 'S' and lines[j+1][i+1] == 'M') and (lines[j-1][i+1] == 'M' and lines[j+1][i-1] == 'S')):
        return True
print(lines)
for j, line in enumerate(lines[:-1]):
    for i, char in enumerate(line):
        if char == 'A' and i > 0 and i < len(line)-1:
            #print(f'found an A')
            if check_X(lines, j, i):
                answ += 1
print(answ)