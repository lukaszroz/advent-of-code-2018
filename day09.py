from collections import defaultdict, deque

# players_n = 9
# last_marble = 25
players_n = 428
# last_marble = 70825
last_marble = 7082500


scores = defaultdict(int)
player = 1
circle = deque([0])
max_score = 0

# for marble in range(1, last_marble + 1):
for marble in range(1, last_marble - (last_marble % 23) + 1):
	if marble % 23 == 0:
		scores[player] += marble
		circle.rotate(7)
		scores[player] += circle.pop()
		circle.rotate(-1)
		max_score = max(max_score, scores[player])
	else:
		circle.rotate(-1)
		circle.append(marble)
	# for m in circle:
	# 	print("%4d" % m, end='')
	# print()
	player += 1
	if player > players_n:
		player = 1

print("Star:", max_score)