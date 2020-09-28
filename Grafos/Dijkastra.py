import math
import heapq

inf = math.inf

class Grafo:
	def __init__(self, dist = inf, peso = 0):
		self.dist = dist
		self.peso = peso
	def __lt__(self, other):
		return self.dist < other.dist
	#def __repr__(self):
		#return f'A({self.dist})'

v1 = Grafo(30)
v2 = Grafo(10)
v3 = Grafo(20)
G = [v1,v2,v3]
for v in G:
	print(v.dist)
heapq.heapify(G)
for v in G:
	print(v.dist)


def dijkastra(G,s):
	for v in G:
		v.dist = inf
	s.dist = 0
	heapq.heapify(G) #Transfor G em Heap
	



dijkastra(G,v2)
