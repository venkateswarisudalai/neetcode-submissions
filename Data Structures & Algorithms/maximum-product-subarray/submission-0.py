class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range(1,len(nums)):

            old_max = curr_max
            old_min = curr_min


            curr_max = max(nums[i],nums[i]*old_max,nums[i]*old_min)
            curr_min = min(nums[i],nums[i]*old_max,nums[i]*old_min)

            result = max(result,curr_max)

        return result
        