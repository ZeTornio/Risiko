import numpy as np
import math
class Risiko():
    def __init__(self,n:int,m_att:int,m_def:int):
        self.n=n
        self.m=min(m_att,m_def)
        self.results=np.zeros(self.m+1,dtype=np.uint)
        self.attack=np.ones(m_att,dtype=np.uint)
        self.attack[m_att-1]=0
        self.defense=np.ones(m_def,dtype=np.uint)
        while (self.step(self.attack,m_att-1)==True):
            self.defense[:]=1
            self.defense[m_def-1]=0
            while (self.step(self.defense,m_def-1)==True):
                p=math.factorial(m_att)
                for i in np.unique(self.attack,return_counts=True)[1]:
                    p/=math.factorial(i)
                p*=math.factorial(m_def)
                for i in np.unique(self.defense,return_counts=True)[1]:
                    p/=math.factorial(i)
                atk_won=0
                for i in range(self.m):
                    if self.attack[i]>self.defense[i]:
                        atk_won+=1
                self.results[atk_won]+=p
        print("ATK-DEF\tcases\tprob.")
        for i in range(self.m+1):
            print(f"{i}-{self.m-i}\t{self.results[i]}\t{round(self.results[i]/sum(self.results[:]),2)}")
    def step(self,array,i:int):
        if i==0:
            if array[i]<self.n:
                array[i]+=1
                return True
            return False
        else:
            if array[i]<array[i-1]:
                array[i]+=1
                return True
            array[i]=1
            return self.step(array,i-1)
    
