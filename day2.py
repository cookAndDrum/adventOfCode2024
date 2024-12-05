# part 1
def check_ok (report):
    ok = True
    only_asc = True
    only_desc = True
    for i in range(len(report)-1):
        diff = report[i+1] - report[i]

        if abs(diff) not in range(1, 4):
            ok = False
            break

        if diff > 0:
            only_desc = False
        if diff < 0:
            only_asc = False
    return (only_asc or only_desc) and ok

reports = []

with open('day2-1-input.txt') as file:
    for line in file.readlines():
        temp = list(map(int, line.split()))
        if temp:
            reports.append(temp)
        
# time complexity of n*n logn

safe_count = 0
for report in reports:
    s_report = sorted(report)
    if s_report == report or s_report[::-1] == report:
        diff = [abs(report[i] - report[i+1]) for i in range(len(report)-1)]
        if max(diff) <= 3 and min(diff) >=1:
            safe_count+=1

print(safe_count)

# another way

safe_count = 0

for report in reports:
    if check_ok(report):
        safe_count+=1

print(safe_count)


# part 2
safe_count_2 = 0

nested_list = [
    [7, 6, 4, 2, 1],  # Safe without removing any level.
    [1, 2, 7, 8, 9],  # Unsafe regardless of which level is removed.
    [9, 7, 6, 2, 1],  # Unsafe regardless of which level is removed.
    [1, 3, 2, 4, 5],  # Safe by removing the second level, 3.
    [8, 6, 4, 4, 1],  # Safe by removing the third level, 4.
    [1, 3, 6, 7, 9]   # Safe without removing any level.
]

for report in reports:
    # part 1 case pattern:
    if check_ok(report):
        print(report)
        safe_count_2+=1
    else:
        # part 2
        for i in range(len(report)-1):
            diff = report[i+1] - report[i]

            # if there is obvious out of range
            if abs(diff) not in range(1, 4):
                if check_ok(report[:i+1]+report[i+2:]) or check_ok(report[:i]+report[i+1:]):
                    print(report)
                    safe_count_2+=1
                    break

            # if all of the range is correct, but might have valley or hill
            if i + 2 < len(report):
                diff2 = report[i+2] - report[i+1]
                if (diff > 0) != (diff2 > 0):
                    if check_ok(report[:i+2] + report[i+3:]) or check_ok(report[:i+1]+report[i+2:]) or check_ok(report[:i]+report[i+1:]):
                        print(report)
                        safe_count_2 += 1
                        break

print(safe_count_2) 
