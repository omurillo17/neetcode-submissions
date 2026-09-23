class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        vistos = {}

        for palabra in strs:
            indice = "".join(sorted(palabra))
            if indice in vistos:
                vistos[indice].append(palabra)
            else:
                vistos[indice] = [palabra]
        return list(vistos.values())