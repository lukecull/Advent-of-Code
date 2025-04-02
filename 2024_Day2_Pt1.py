import sys

reports = []
lines = []
safe = 0
unsafe = 0

for line in sys.stdin: #gathers line by line inputs 
    lines.append(line.rstrip('\n'))

for line in lines: #sets each input in each line to its own str
    reports.append(line.split(' '))

for report in reports:
    num_report = list(map(int, report))
        
    inc_report = sorted(num_report)
    dec_report = sorted(num_report, reverse=True)

    #check value distances
    for i, num in enumerate(num_report):
        num = int(num)
        if i < len(num_report) - 1:

            if num_report == inc_report:
                if not ((num_report[i+1] <= num +3) and (num_report[i+1] >= num + 1)):
                    unsafe += 1
                
            elif num_report == dec_report:
                if not ((num_report[i+1] >= num - 3) and (num_report[i+1] <= num - 1)):
                    unsafe += 1
    
    if (num_report == inc_report or num_report == dec_report) and unsafe == 0:
        safe += 1
    
    unsafe = 0

print(safe)