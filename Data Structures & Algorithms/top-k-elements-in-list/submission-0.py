class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap
        freq = [[] for i in range(len(nums) + 1)] # array same size as input array

        for n in nums:
            count[n] = count.get(n,0) + 1 # make count dict - for each num in nums show count
        
        for n, c in count.items(): # flip it for freq array count is index and the value is what number occurs that
            freq[c].append(n) # many times


        res = [] # final result
        for i in range(len(freq)-1, 0, -1): # start from end of fre which is a list of lists
            for n in freq[i]: # within last list in freq
                res.append(n) # append numbers in that last list in freq array
                if len(res) == k: # if numbers match k then exit
                    return res



