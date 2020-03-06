#!/usr/bin/env python
# coding: utf-8

import argparse
import csv
from collections import defaultdict
import sys

parser = argparse.ArgumentParser(description='Calcula la menor distancia entre 2 estaciones de tren')
parser.add_argument('file', help='Archivo de texto a leer')
parser.add_argument('start', help='Nombre estación origen')
parser.add_argument('destination', help='Nombre estación destino')
args = parser.parse_args()

inf = float('inf')
dist = {}
neighbours = defaultdict(dict)

with open(args.file, 'r') as csvfile:
  reader = csv.reader(csvfile)
  for station1, station2, distance in reader:
    dist[station1] = inf
    dist[station2] = inf
    d = int(distance)
    neighbours[station1][station2] = d
    neighbours[station2][station1] = d # bidirectional

# validate start and destination are present
if not args.start in dist:
    sys.exit('Start {} is not present'.format(args.start))

if not args.destination in dist:
    sys.exit('Destination {} is not present'.format(args.destination))

unvisited = set(dist.keys())
dist[args.start] = 0
while unvisited: # not empty
  node = min(unvisited, key=lambda uv: dist[uv]) # use a better data-structure
  unvisited.remove(node)
  if args.destination == node or dist[node] == inf: # unreachable nodes or destination
    break
  for end, cost in neighbours[node].items():
    if dist[node] + cost < dist[end]:
      dist[end] = dist[node] + cost

print('The shortest path from {} to {} is {}'.format(args.start, args.destination, dist[args.destination]))
