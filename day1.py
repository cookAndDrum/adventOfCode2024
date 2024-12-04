# part 1
l, r = [], []
with open('day1-1-input.txt') as file:
    for line in file.readlines():
        temp = list(map(int, line.split()))
        if temp:
            l.append(temp[0])
            r.append(temp[1])
l.sort()
r.sort()

distance = sum([abs(left - right) for left, right in zip(l, r)])
print(distance)

# part 2
l_set = set(l)
similarity_score = sum([left * r.count(left) for left in l_set])
print(similarity_score)
