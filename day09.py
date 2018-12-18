from collections import defaultdict

# players_n = 9
# last_marble = 25
players_n = 428
# last_marble = 70825
last_marble = 7082500

class Node:
	def __init__(self, value):
		self.value = value

scores = defaultdict(int)
player = 1
current = Node(0)
current.next = current
current.prev = current
max_score = 0

for marble in range(1, last_marble - (last_marble % 23)):
	if marble % 23 == 0:
		scores[player] += marble
		for _ in range(7):
			current = current.prev
		scores[player] += current.value
		max_score = max(max_score, scores[player])
		#remove node
		current.prev.next = current.next
		current.next.prev = current.prev
		current = current.next		
	else:
		current = current.next
		#add node
		next_node = Node(marble)
		next_node.prev = current
		next_node.next = current.next
		current.next.prev = next_node
		current.next = next_node
		current = next_node
	player += 1
	if player > players_n:
		player = 1

print("Star:", max_score)