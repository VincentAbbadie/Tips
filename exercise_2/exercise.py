# -*- coding: utf-8 -*-

class soluce:
    debug=None
    input_file=None
    
    def __init__(self,i_f,d):
        self.input_file=i_f
        self.debug=d
    
    def findRecette(self,recette,target):
        res=None
        for r in recette:
            rr=r.split(' ')
            if rr[0]==target:
                res=[rr[1],rr[2]]
                break
            
        return res
    
    def soluce(self):
        # self.debug(self.input_file)
        lines=[]
        with open(self.input_file) as f:
            line=f.readline()
            while line != '':
                lines.append(line.rstrip('\n'))
                line=f.readline()
        self.debug(lines)
        
        target=lines[0]
        basePotion=lines[2].split(' ')
        recette=lines[4:]
        
        self.debug(target)
        self.debug(basePotion)
        self.debug(recette)
        children=[target]
        result=0
        
        while True :
            newChild=[]
            for c in children:
                if c in basePotion:
                    result+=1
                else: 
                    recetteFound=self.findRecette(recette,c)
                    if recetteFound!=None:
                        newChild.append(recetteFound[0])
                        newChild.append(recetteFound[1])
            
            if len(newChild)>0:
                children=newChild
            else :
                break;
                
        if result==0:
            print('impossible')
        else:
            print(result)
                
        
                
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