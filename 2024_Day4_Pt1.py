import re
D = open('input.txt').read()
answ = 0
def check_horz(D):
    #use regex to find xmas or samx in every line of the text
    matches = ['[]']
    D = str(D)
    lines = D.splitlines()
    copys = lines.copy()
    for line in copys:
        rev_line = line[::-1]
        lines.append(rev_line)
    for i, line in enumerate(lines):
        match = re.findall(r"(XMAS)", line)
        if match != []:
            matches.append(match)
    return len(matches) - 1
def check_diag(D):
    #cycle through each char in each line and check below it
    #look at the next lines and determine if theres a match
    #if match find the direction word is traveling
    #only check the next 3 lines rather than all of them
    #dont check the last 3 rows
    ###X########
    ##A#M#######
    #####A######
    ######S#####
    #TODO
    pass
def check_vert(D):
    vert= []
    matches= []
    D = str(D)
    lines = D.splitlines()
    for char in lines[0]:
        vert.append('')

    for line in lines:
        for i, char in enumerate(line):
            vert[i] += char
    vert_copy = vert.copy()
    for line in vert_copy:
        rev_line = line[::-1]
        vert.append(rev_line)
    print(f'{vert} length: {len(vert)}')
    for i, line in enumerate(vert):
        match = re.findall(r"(XMAS)", line)
        if match != []:
            matches.append(match)
    return len(matches)

answ += (check_diag(D) + check_horz(D) + check_vert(D))
print(answ)