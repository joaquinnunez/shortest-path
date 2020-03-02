import argparse
import csv

parser = argparse.ArgumentParser(description='Calcula la menor distancia entre 2 estaciones de tren')
parser.add_argument('file', help='Archivo de texto a leer')
args = parser.parse_args()

with open(args.file, 'r') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
      print ', '.join(row)
