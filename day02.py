lines = open('input_02.txt').read().splitlines()
letters = list(map(lambda x: chr(x), list(range(ord('a'), ord('z') + 1))))

twos = 0
threes = 0
for line in lines:
	two = False
	three = False
	for c in letters:
		two |= line.count(c) == 2
		three |= line.count(c) == 3
	if two:
		twos += 1
	if three:
		threes += 1
print("Star 1:", twos*threes)

def star2(lines):
	for line1 in lines:
		for line2 in lines:
			diff = 0
			i = 0
			while i < len(line1) and diff < 2:
					if line1[i] != line2[i]:
						diff += 1
					i += 1
			if diff == 1:
				i = 0
				answer = ""
				while i < len(line1):
						if line1[i] == line2[i]:
							answer += line1[i]
						i += 1
				return answer
print("Star 2:", star2(lines))