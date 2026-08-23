class Solution:

    def encode(self, strs: List[str]) -> str:
        resultado = ""
        for s in strs:
            resultado += str(len(s)) + "#" + s
        return resultado

    def decode(self, s: str) -> List[str]:
        respuesta = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            long_str = s[i:j]
            long = int(long_str)
            respuesta.append(s[j + 1 : j + 1 + long])

            i = j + 1 + long
        return respuesta