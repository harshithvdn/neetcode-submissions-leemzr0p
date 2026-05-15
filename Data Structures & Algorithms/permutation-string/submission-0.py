class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1list=list(s1)
        s2list=list(s2)

        s1sort=sorted(s1list)
        x=0

        right=len(s1)

        for left in range(len(s2)):
            s2newlist= list(s2[left:right])
            s2newlist.sort()
            if s1sort==s2newlist:
                x += 1
            else:
                
                right +=1
        if x>=1:
            return True
        else:
            return False
            



        