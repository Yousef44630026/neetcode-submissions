class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        res=0
        m=len(skill)
        skill.sort()
        middle=len(skill)//2
        for i in range(middle):
            if skill[i]+skill[len(skill)-1-i]!=skill[0]+skill[-1]:
                return -1
            else:
                res+=skill[i]*skill[len(skill)-1-i]
        return res        
                  

