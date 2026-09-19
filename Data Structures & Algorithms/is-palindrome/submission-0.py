class Solution:
    def isPalindrome(self, s: str) -> bool:
        izq = 0
        der = len(s) - 1
        while izq < der:
            if s[izq].isalnum() == False:
                izq += 1
                continue
            if s[der].isalnum() == False:
                der -= 1
                continue
            if s[izq].lower() != s[der].lower():
                return False
            izq += 1
            der -= 1
        return True