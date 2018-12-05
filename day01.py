with open('input_01.txt') as f:
	lines = f.read().splitlines()

numbers = list(map(lambda x: int(x), lines))

sum = 0
for n in numbers:
	sum += n
print("Star 1:", sum)

sum = 0
i = 0
s = set()

while True:
	sum += numbers[i]
	if(sum in s):
		break
	s.add(sum)
	i += 1
	i %= len(numbers)
print("Star 2:", sum)