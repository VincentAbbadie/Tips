# -*- coding: utf-8 -*-

class soluce:
    debug=None
    input_file=None
    
    def __init__(self,i_f,d):
        self.input_file=i_f
        self.debug=d

    def build_letter_and_ind(self,str_a,str_b):
        letter_a_in_b=list()
        # [0] letter
        # [1] ind_a
        # [2] =[] ind_b
        for i,c_a in enumerate(str_a):
            added=False
            for j in range(len(str_b)):
                if c_a==str_b[j]:
                    if added:
                        letter_a_in_b[-1][2].append(j)
                    else:
                        letter_a_in_b.append([c_a,i,[j]])
                        added=True
        return letter_a_in_b
    
    def soluce(self):
        # self.debug(self.input_file)
        with open(self.input_file) as f:
            wish_a=f.readline()[:-1]
            wish_b=f.readline()
            self.debug(wish_a,'a')
            self.debug(wish_b,'b')
            letter_a_in_b=self.build_letter_and_ind(wish_a, wish_b)
            letter_b_in_a=self.build_letter_and_ind(wish_b, wish_a)
            self.debug(letter_a_in_b,'a in b')
            self.debug(letter_b_in_a,'b in a')
            
                
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