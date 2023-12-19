# -*- coding: utf-8 -*-

class soluce:
    debug=None
    input_file=None
    
    def __init__(self,i_f,d):
        self.input_file=i_f
        self.debug=d

    def soluce(self):
        with open(self.input_file) as f:
            cat_num = int(f.readline().strip())
            for i in range(cat_num):
                cat=f.readline().strip().split(" ")[1]
                print(f'{cat} :')
                print(f'{"  ".join(["-".join([s[k*2:(k+1)*2] for k in range(len(s)//2)]) for s in f.readline().strip().split(" ")])}')

if __name__=="__main__":
    NORMAL='\033[0m'
    
    def debug(message,name=''):
        CYAN='\033[36m'
        if len(name)>0:
            print(f'{CYAN}{name}=',end='')
        print(f'{CYAN}{message}{NORMAL}')
    
    def ok():
        GREEN='\033[32m'
        print(f'{GREEN}[ OK ]{NORMAL}')
        
    def ko():
        RED='\033[31m'
        print(f'{RED}[ KO ]{NORMAL}')
    
    with open('exercise.txt') as exo_descc:
        for j,l in enumerate(exo_descc):
            if l.endswith('\n'):
                    l=l[:-1]
            if len(l)==0 or j==0:
                continue
            if j==1:
                if l=='OK':
                    ok()
                else:
                    ko()
                continue
            print(f' in={l}')
            s=soluce(l,debug)
            s.soluce()