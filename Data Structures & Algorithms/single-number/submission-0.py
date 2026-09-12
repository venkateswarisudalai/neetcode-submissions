class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i,num in enumerate(nums):
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num]+=1
                if hashmap[num] == 2:
                    del hashmap[num]

        return list(hashmap.keys())[0]
        