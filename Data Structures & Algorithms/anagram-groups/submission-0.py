class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # dictionary of lists

        for s in strs:
            count = [0] * 26 #[0,0,0,0.....0]

            for c in s:
                count[ord(c)- ord("a")] +=  1 # a which is 65 - 65 = 0 so increment index 1 by 1
            
            res[tuple(count)].append(s) # append this lists of count pattern to res 
            # have to make the key a tuple because list is mutable and keys cannot be mutable 
        # [0,1,0,0,0,1,,,,]: [eat, ate]
        return list(res.values())