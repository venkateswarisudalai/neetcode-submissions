class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        

        def robber(nums):
            house_1 = 0
            house_2 = 0

            for money in nums:

                current = max(house_1+money,house_2)

                house_1 = house_2
                house_2 = current
            
            return house_2


        return max(robber(nums[1:]),robber(nums[:-1]))
        