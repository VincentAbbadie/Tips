# -*- coding: utf-8 -*-

class soluce:
    debug=None
    input_file=None
    
    def __init__(self,i_f,d):
        self.input_file=i_f
        self.debug=d
    
    def nextTurn(self,strs):
        if len(strs)==1:
            if len(strs[0])%2==0:
                return False
            else:
                return True
            
        freq=dict()
        for s in strs:
            if len(s)>=1:
                if s[0] in freq:
                    freq[s[0]]+=1
                else:
                    freq[s[0]]=1
        
        voyante_letter=dict()
        for s in strs:
            if len(s)==1 and s[0] in freq and freq[s[0]]==1:
                return True
            if len(s)>=2:
                if s[1] in voyante_letter:
                    voyante_letter[s[1]].append(s[2:])
                else:
                    voyante_letter[s[1]]=[s[2:]]
        
        if len(voyante_letter)==0:
            return True
        
        winable=dict()
        for k,v in voyante_letter.items():
            if len(v)==1:
                if len(v[0])%2==0:
                    winable[k]=False
                else:
                    winable[k]=True
            else:
                winable[k]=self.nextTurn(v)
        
        for res in winable.values():
            if not res:
                return False
                
        return True
    
    def soluce(self):
        # self.debug(self.input_file)
        lines=[]
        with open(self.input_file) as f:
            line=f.readline()
            while line != '':
                lines.append(line.rstrip('\n'))
                line=f.readline()
        self.debug(lines)
        
        result=dict();
        for mot in lines[1:]:
            if mot[0] in result:
                result[mot[0]].append(mot)
            else:
                result[mot[0]]=[mot]
        
        resultt=set()
        for k,v in result.items():
            if self.nextTurn(v):
                resultt.add(k)
            
        
        if(len(resultt)>0):
            resultt=sorted(resultt)
            print('\n'.join(i for i in resultt)) 
        else:
            print('impossible')
                
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