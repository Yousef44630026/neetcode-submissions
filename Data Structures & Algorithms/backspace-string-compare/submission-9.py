class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        L=[]
        Q=[]
        for w in s:
            if w!="#":
                L.append(w)
            elif L:
                L.pop()
        for w in t:
            if w!="#":
                Q.append(w)
            elif Q:
                Q.pop() 
        return ''.join(L)==''.join(Q)                  
                 

        
