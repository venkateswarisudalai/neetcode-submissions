class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_sum = nums[0]

        for i in range(1,len(nums)):
            sum = nums[i] + nums[i-1]
            if sum > nums[i]:
                nums[i] = sum
            
            if max_sum < nums[i]:
                max_sum = nums[i]

        return max_sum
        