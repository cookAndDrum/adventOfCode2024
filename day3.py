# part 1
import re

ex = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

pattern = r'mul\((\d+),(\d+)\)'
matches = re.findall(pattern, ex)

products = [int(a)*int(b) for a, b in matches]
sum_products = sum(products)
print(sum_products)

with open('day3-1-input.txt') as file:
    lines = file.readlines()

out = 0
for l in lines:
    m = re.findall(pattern, l)
    out += sum([int(a)*int(b) for a, b in m])
print(out)

# part two
new_pattern= r'mul\((\d+),(\d+)\)|(do\(\)|don\'t\(\))'
do_p = r'do\(\)'
dont_p = r'don\'t\(\)'

ex = "mul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

r = re.finditer(f'{pattern}|{do_p}|{dont_p}', ex)
# print(r)

is_do = True
out_2 = 0

for l in lines:
    r = re.finditer(f'{pattern}|{do_p}|{dont_p}', l)

    for m in r:
        # print(m.group(0))
        # print(m.group(1))
        # print(m.group(2))
        # print('='*8)

        if m.group(0).startswith('do()'):
            is_do=True
        elif m.group(0).startswith('don\'t'):
            is_do=False
        else:
            if is_do:
                a, b = m.groups()
                out_2+= int(a)*int(b)
print(out_2)