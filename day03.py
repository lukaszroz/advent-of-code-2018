import re
from collections import namedtuple
from itertools import product		

with open('input_03.txt') as f:
	lines = f.read().splitlines()

Claim = namedtuple('Claim', ['ID', 'x', 'y', 'width', 'height'])
p = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
def line_to_claim(line):
	return Claim(*map(int, p.match(line).groups()))
claims = [line_to_claim(line) for line in lines]

def star1(claims):
	fabric = {}
	overlap = 0
	for claim in claims:
		for pos in product(range(claim.x, claim.x+claim.width), range(claim.y, claim.y+claim.height)):		
			if pos in fabric:
				if fabric[pos] != 0:
					fabric[pos] = 0
					overlap += 1
			else:
				fabric[pos] = claim.ID
	return (fabric, overlap)

def star2(claims, fabric):
	for claim in claims:
		if 0 not in (fabric[pos] for pos in product(range(claim.x, claim.x+claim.width), range(claim.y, claim.y+claim.height))):
			return claim.ID

(fabric, overlap) = star1(claims)

print("Star 1:", overlap)
print("Star 2:", star2(claims, fabric))