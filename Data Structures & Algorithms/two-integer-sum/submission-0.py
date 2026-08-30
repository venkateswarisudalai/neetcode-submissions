class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        hashmap = {}

        for i,num in enumerate(nums):
            two_sum = target - num

            if two_sum in hashmap:
                return [hashmap[two_sum],i]
            else:
                hashmap[num] = i

        return []
                


            
            
