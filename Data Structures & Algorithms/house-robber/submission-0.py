class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        house_1 = nums[0]
        house_2 = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            max_amount = max(house_2,house_1 + nums[i])

            house_1 = house_2
            house_2 =  max_amount

        return house_2
        