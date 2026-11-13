class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score,ans=0,0
        t=power
        l,r=0,len(tokens)-1
        while l<=r:
            if t>=tokens[l]:
                t-=tokens[l]
                score+=1
                l+=1
                ans=max(score,ans)
            elif score>0:
                score-=1
                t+=tokens[r]
                r-=1
            else:
                break
        return ans            

                


        

        
        
        
        
