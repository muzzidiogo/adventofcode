file = open('input.txt', 'rt')

lines = []
for line in file:
    lines.append(line.removesuffix('\n'))

left, right = [], []
for line in lines:
    separated_line = line.split('   ')
    left.append(separated_line[0])
    right.append(separated_line[1])

right.sort()
left.sort()

dist = []
for i in range(len(right)):
    dist.append(abs(int(right[i]) - int(left[i])))

result = sum(dist)

print(f'Sum:{result}')