class Solution:

    def encode(self, strs: List[str]) -> str:
        resultado = ''
        for s in strs:
            resultado += str(len(s)) + '#'+s
        return resultado

    def decode(self, s: str) -> List[str]:
        i = 0
        resultado = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            longitud_str = s[i:j]
            longitud = int(longitud_str)
            
            palabra = s[j+1 : j+1+longitud]
            
            resultado.append(palabra)
            
            i = j + 1 + longitud
            
        return resultado