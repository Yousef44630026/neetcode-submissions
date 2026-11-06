class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L=[]
        l=0
        while l+k<=len(blocks):
            te=0
            for r in range(k):
                if blocks[l+r]=="W":
                    te+=1
            L.append(te)   
            l+=1
        return min(L)   
        