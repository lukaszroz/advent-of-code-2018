with open('input_02.txt') as f:
	lines = f.read().splitlines()

def star1(lines):
	twos = 0
	threes = 0
	for line in lines:
		count = {}
		for ch in line:
			count[ch] = line.count(ch)
		if 2 in list(count.values()):
			twos += 1
		if 3 in list(count.values()):
			threes += 1
	return twos * threes

def star2(lines):
	from itertools import combinations
	for line1, line2 in combinations(lines, 2):
			diff = 0
			for ch1, ch2 in zip(line1, line2):
					if ch1 != ch2:
						diff += 1
			if diff == 1:
				answer = ""
				for ch1, ch2 in zip(line1, line2):
					if ch1 == ch2:
						answer += ch1
				return answer

print("Star 1:", star1(lines))				
print("Star 2:", star2(lines))