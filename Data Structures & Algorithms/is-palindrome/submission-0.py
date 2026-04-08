class Solution:
    def isPalindrome(self, s: str) -> bool:
        sstrip= "".join(s.strip())
        a= sstrip.lower()
        sstripmain= ''.join(ch for ch in a if ch.isalnum())
        srevmain= "".join(reversed(sstripmain))
        
        if sstripmain==srevmain:
            return True
        else:
            return False
