class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
     res = []
     i = 0

     while i < len(s):
        j = i

        # move j until '#'
        while s[j] != "#":
            j += 1

        # extract length
        length = int(s[i:j])

        # move past '#'
        j += 1

        # extract word
        word = s[j:j + length]
        res.append(word)

         # move i to next segment
        i = j + length

     return res