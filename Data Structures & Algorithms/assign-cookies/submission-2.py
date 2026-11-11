class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
         s.sort()
         g.sort()
         l,r,res=0,0,0
         while r<len(s) and l<len(g):
           if s[r]>=g[l]:
               res+=1
               r+=1
               l+=1
           else:
               r+=1
         return res  
        