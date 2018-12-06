with open('input_06.txt') as f:
	points = [tuple(map(int, line.split(','))) for line in f.read().splitlines()]

x_min = min(x for (x, y) in points)
x_max = max(x for (x, y) in points)
y_min = min(y for (x, y) in points)
y_max = max(y for (x, y) in points)

grid = {}
areas = [0] * len(points)

for x in range(x_min, x_max + 1):
	for y in range(y_min, y_max + 1):
		from heapq import nsmallest
		((first_distance, first_id), (second_distance, second_id)) = nsmallest(2, ((abs(x - px) + abs(y - py), idx) for (idx, (px, py)) in enumerate(points)))
		if first_distance != second_distance:
			grid[(x, y)] = first_id
			areas[first_id] += 1
		else: 
			grid[(x, y)] = -1

#Exclude infinite areas (ones reaching an edge)
for x in range(x_min, x_max + 1):
	for y in (y_min, y_max):
		if grid[(x, y)] > 0: areas[grid[(x, y)]] = 0

for x in (x_min, x_max):
	for y in range(y_min, y_max + 1):
		if grid[(x, y)] > 0: areas[grid[(x, y)]] = 0

print("Star 1:", max(areas))

region = 0
size = 10000

for x in range(x_min, x_max + 1):
	for y in range(y_min, y_max + 1):
		if sum(abs(x - px) + abs(y - py) for (px, py) in points) < size:
			region += 1
			
print("Star 2:", region)