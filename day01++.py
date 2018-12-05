with open('input_01.txt') as f:
	numbers = list(map(lambda x: int(x), f.read().splitlines()))

def star1(numbers):
	return sum(numbers)

def star2(numbers):
	from itertools import cycle
	sum = 0
	s = set()
	for n in cycle(numbers):
		sum += n
		if sum in s:
			return sum
		s.add(sum)

print("Star 1:", star1(numbers))
print("Star 2:", star2(numbers))