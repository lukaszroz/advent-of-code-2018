import re
from collections import defaultdict

with open('input_04.txt') as f:
	lines = f.read().splitlines()

guards = defaultdict(lambda:[0]*59)
id = 0
falls = 0
for line in sorted(lines):	
	if 'Guard' in line:
		id = int(re.findall('#(\d+)', line)[0])
		continue
	minute = int(re.findall(':(\d+)\]', line)[0])
	if 'falls asleep' in line: 
		falls = minute
	else:
		for m in range(falls, minute):
			guards[id][m] += 1

def star1(guards):
	_, guard_id = max((sum(minutes), guard) for (guard, minutes) in guards.items())
	_, chosen_minute = max((m, idx) for (idx, m) in enumerate(guards[guard_id]))
	return guard_id * chosen_minute

def star2(guards):	
	_, chosen_minute, guard_id = max((minute, idx, guard) for (guard, minutes) in guards.items() for (idx, minute) in enumerate(minutes))
	return guard_id * chosen_minute

print("Star 1:", star1(guards))
print("Star 2:", star2(guards))