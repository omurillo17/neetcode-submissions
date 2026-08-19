class Solution:

    def encode(self, strs: List[str]) -> str:
        r = ""
        for s in strs:
            r += str(len(s)) + "#" + s
        return r

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1

            long_str = s[i:j]
            long = int(long_str)

            r = s[j+1 : j+1+long]

            res.append(r)
            i = j + 1 + long
        return res
