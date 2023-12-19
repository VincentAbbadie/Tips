# -*- coding: utf-8 -*-
import sys

print('DEBUT',file=sys.stderr,flush=True)

print('Read a file')
print("\nMethode 1 : Lire tout le fichier en liste")
with open("input.txt") as f:
    lines = f.readlines()
    print(f'{lines} == {type(lines)}')

print("\nMethode 2 : lire ligne par ligne avec le retour a la ligne")
with open("input.txt") as f:
    [print(f'{line} == {type(line)}') for line in f.readlines()]

print("\nMethode 3 : lire ligne par ligne sans le retour a la ligne")
with open("input.txt") as f:
    [print(f'{line.strip()} == {type(line)}') for line in f.readlines()]

print("\nMethode 4 : lire le fichier entier en str")
with open("input.txt") as f:
    lines = f.read()
    print(f'{lines} == {type(lines)}')

print("\nMethode 5 : lire ligne par ligne sans le retour a la ligne grace au strip")
with open("input.txt") as f:
    for line in f:
        print(f'{line.strip()} == {type(line)}')
