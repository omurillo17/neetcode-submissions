class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        diccionario = {}

        for palabra in strs:
            llave = "".join(sorted(palabra))

            if llave in diccionario:
                diccionario[llave].append(palabra)
            else:
                diccionario[llave] = [palabra]

        return list(diccionario.values())