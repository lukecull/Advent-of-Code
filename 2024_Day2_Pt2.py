import sys

def isSafe(report):
        failed = 0

        inc_report = sorted(report)
        dec_report = sorted(report, reverse=True)

        #check value distances
        for i, num in enumerate(report):
            num = int(num)
            if i < len(report) - 1:

                if report == inc_report:
                    if not ((report[i+1] <= num +3) and (report[i+1] >= num + 1)):
                        failed += 1
                    
                elif report == dec_report:
                    if not ((report[i+1] >= num - 3) and (report[i+1] <= num - 1)):
                        failed += 1
                else:
                     return False
        if failed == 0:
            return True

def findExcept(report):
     for i in range(len(report)-1):
          copy_report = report.copy()
          del copy_report[i]
          if isSafe(copy_report) == True:
            return True
     copy_report = report.copy()
     del copy_report[-1]
     if isSafe(copy_report) == True:
            return True
     return False
          

lines = []
safe = 0

for line in sys.stdin: #gathers line by line inputs 
    lines.append(line.rstrip('\n').split())


for report in lines:
     num_report = list(map(int, report))
     if isSafe(num_report) == True:
          #print(report)
          safe += 1
     elif findExcept(num_report) == True:
         #print(f'{report} is safe with exception')
         safe += 1
print(safe)