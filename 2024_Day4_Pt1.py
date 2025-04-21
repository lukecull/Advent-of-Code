import re
D = open('input.txt').read()
D = str(D)
lines = D.splitlines()
answ = 0
def check_horzRight(lines):
    matches = []
    for line in lines:
        match = re.findall(r"(XMAS)", line)
        if match != []:
            matches += match
    return len(matches)

def check_horzLeft(lines):
     matches = []
     rev_lines = []
     for line in lines:
        rev_line = line[::-1]
        rev_lines.append(rev_line)
     for line in rev_lines:
        match = re.findall(r"(XMAS)", line)
        if match != []:
            matches += match
     return len(matches)

def check_downLeft(lines, rev_lines):
    matches = []
    total = 0
    for j, line in enumerate(lines[:-3]):
        i = 0
        for i, char in enumerate(line):
            if char == 'X' and lines[j+1][i-1] == "M" and i >= 3:
                if lines[j+2][i-2] == "A" and lines[j+3][i-3] == "S":
                    total += 1
                    matches.append(("XMAS", [(j,i), (j+1, i-1), (j+2, i-2), (j+3, i-3)]))
    
    for j, line in enumerate(rev_lines[:-3]):
            for i, char in enumerate(line):
                if char == 'X' and rev_lines[j+1][i-1] == "M" and i >= 3:
                    if rev_lines[j+2][i-2] == "A" and rev_lines[j+3][i-3] == "S":
                        total += 1
                        matches.append(("SAMX", [(j,i), (j+1, i-1), (j+2, i-2), (j+3, i-3)]))
    return total

def check_downRight(lines, rev_lines):
    matches = []
    total = 0
    for j, line in enumerate(lines[:-3]):
        i = 0
        for i, char in enumerate(line):
            if char == 'X' and i < (len(line)-3) and lines[j+1][i+1] == "M": 
                if lines[j+2][i+2] == "A" and lines[j+3][i+3] == "S":
                    total += 1
                    matches.append(("XMAS", [(j,i), (j+1, i+1), (j+2, i+2), (j+3, i+3)]))
        
    for j, line in enumerate(rev_lines[:-3]):
        for i, char in enumerate(line):
            if char == 'X' and i < (len(line)-3) and rev_lines[j+1][i+1] == "M":
                if rev_lines[j+2][i+2] == "A" and rev_lines[j+3][i+3] == "S":
                    total += 1
                    matches.append(("SAMX", [(j,i), (j+1, i+1), (j+2, i+2), (j+3, i+3)]))
    return total

def check_diag(lines):
    rev_lines = lines[::-1]
    total = 0
    total += (check_downLeft(lines, rev_lines) + check_downRight(lines, rev_lines))
    return total

def check_vert(lines):
    vert= []
    matches= []
    total = 0
    for char in lines[0]:
        vert.append('')

    for line in lines:
        for i, char in enumerate(line):
            vert[i] += char
    total += (check_horzRight(vert) + check_horzLeft(vert))
    return total

answ += (check_diag(lines) + check_horzRight(lines) + check_horzLeft(lines) + check_vert(lines))
print(answ)