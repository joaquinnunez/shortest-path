import argparse
import csv
from collections import defaultdict

parser = argparse.ArgumentParser(description='Calcula la menor distancia entre 2 estaciones de tren')
parser.add_argument('file', help='Archivo de texto a leer')
args = parser.parse_args()

inf = float('inf')
dist = {}
prev = {}
neighbours = defaultdict(list)

with open(args.file, 'r') as csvfile:
  reader = csv.reader(csvfile)
  for station1, station2, distance in reader:
    dist[station1] = inf
    dist[station2] = inf
    prev[station1] = None
    prev[station2] = None
    neighbours[station1].append((station2, int(distance)))
    neighbours[station2].append((station1, int(distance))) # bidirectional

unvisited = set(dist.keys())
dist[station1] = 0

while unvisited: # not empty
  node = min(unvisited, key=lambda uv: dist[uv]) # use a better data-structure
  unvisited.remove(node)
  for end, cost in neighbours[node]:
    if dist[node] + cost < dist[end]:
      dist[end] = dist[node] + cost
      prev[end] = node

print(dist)
