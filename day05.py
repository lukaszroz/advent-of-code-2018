with open('input_05.txt') as f:
	lines = f.read().splitlines()

def react(polymer):
	i = 1
	while i < len(polymer):
		a = polymer[i-1]
		b = polymer[i]
		if ((a.upper() == a and b.lower() == b) or (a.lower() == a and b.upper() == b)) and a.upper() == b.upper():
		#a little bit faster:
		#if abs(ord(a)-ord(b)) == 32:
			del polymer[i-1:i+1]
			if i > 1: i = i - 1
		else: i = i + 1
	return polymer

reacted = react(list(lines[0]))

print("Star 1:", len(reacted))
#much faster when using leftover from part 1
print("Star 2:", min(len(react([x for x in reacted if x.lower() != c])) for c in map(chr, range(ord('a'), ord('z') + 1))))