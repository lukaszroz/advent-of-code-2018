from re import match
from collections import Counter, defaultdict
from heapq import *

with open('input_07.txt') as f:
	lines = f.read().splitlines()

instructions = defaultdict(list)
for line in lines:
	k, v = match("Step (.) must be finished before step (.) can begin.",line).groups()
	instructions[k] += v

steps = sorted({step for l in instructions.values() for step in l} | set(instructions.keys()))
order = ""
blocked = Counter()
for l in instructions.values():
	for step in l:
		blocked[step] += 1

available = [step for step in steps if step not in blocked]
heapify(available)

while len(available) > 0:
	step = heappop(available)
	order += step

	#handle step completion
	for s in instructions[step]:
		blocked[s] -= 1
		if blocked[s] == 0:
			heappush(available, s)

print("Star 1:", order)

blocked = Counter()
for l in instructions.values():
	for step in l:
		blocked[step] += 1

available = [step for step in steps if step not in blocked]
heapify(available)

running = []
done = 0
timer = 0

workers = 5
step_time = 60

while done < len(steps):
	#start available steps
	while len(available) > 0 and len(running) < workers:
		step = heappop(available)
		done_at = timer + step_time + ord(step) - ord('A') + 1
		heappush(running, [done_at, step])

	#wait for next step to finish
	timer = min(running)[0]

	#handle step completion
	while len(running) > 0 and running[0][0] == timer:
		step = heappop(running)[1]
		done += 1
		for s in instructions[step]:
			blocked[s] -= 1
			if blocked[s] == 0:
				heappush(available, s)

print("Star 2:", timer)