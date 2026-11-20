class Solution:
    def isValid(self, s: str) -> bool:
        pila = []
        pares = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in "([{":
                pila.append(c)
            else:
                if not pila or pila[-1] != pares[c]:
                    return False
                pila.pop()
            
        return len(pila) == 0