# -*- coding: utf-8 -*-
from pathlib import Path
from sys import exit
from importlib_metadata import import_module

NORMAL='\033[0m'

RED='\033[31m'
GREEN='\033[32m'
YELLOW='\033[33m'
BLUE='\033[34m'
PURPLE='\033[35m'
CYAN='\033[36m'
#ORANGE='\033[38;5;220m'

BOLD='\033[1m'
UNDERLINE='\033[4m'

def h1(title):
    barre='-'*len(title)
    print(f'{BOLD}{YELLOW}+{barre}+')
    print(f'|{NORMAL}{title.upper()}{BOLD}{YELLOW}|')
    print(f'+{barre}+{NORMAL}')
def h2(title):
    spaces=' '*2
    barre='-'*len(title)
    print(f'{CYAN}{spaces}{title}')
    print(f'{RED}{spaces}{barre}{NORMAL}')
def h3(title):
    spaces=' '*4
    print(f'{BOLD}{spaces}{UNDERLINE}{title}{NORMAL}')
def h4(title):
    spaces=' '*6
    print(f'{BOLD}{PURPLE}{spaces}{title}{NORMAL}')

def debug(message,name=''):
    if len(name)>0:
        print(f'{RED}{name}=',end='')
    print(f'{RED}{message}{NORMAL}')
    
exos_desc=dict()
p = Path('.')
for f in p.iterdir():
    if f.is_dir() and f.name.startswith('exercise_'):
        n=f.name.strip()[-1]
        with open(f'exercise_{n}/exercise.txt') as exo_desc:
            exos_desc[n]=exo_desc.readline()[:-1] +' '+exo_desc.readline()[:-1]
        
print(f'Nombre d\'exercice : {len(exos_desc.keys())}')
choice=-1
while(choice != 0):
    h2('Exercices')
    for i in exos_desc.keys():
        print(f'  {i} = {exos_desc[i]}')
    print('  q = EXIT')
    choice=input("Choix : ")
    if choice not in exos_desc.keys():
        if choice == 'q':
            h4('FIN')
            exit()
        else:
            print(f'{RED}Pas compris{NORMAL}')
    else:
        h4(f'Exercise {choice}')
        runner=import_module(f'exercise_{choice}.exercise')
        with open(f'exercise_{choice}/exercise.txt') as exo_descc:
            for j,l in enumerate(exo_descc):
                if l.endswith('\n'):
                        l=l[:-1]
                if len(l)==0 or j==0 or j==1:
                    continue
                print(f' in={l}')
                ex=runner.soluce(f'exercise_{choice}/'+l,debug)
                ex.soluce()
                
                
                
                
                