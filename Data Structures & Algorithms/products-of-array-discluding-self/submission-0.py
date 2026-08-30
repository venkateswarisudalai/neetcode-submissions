class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product =1
        result = [0]*n

        for i,num in enumerate(nums):
            result[i] = left_product
            left_product *= nums[i]

        right_product = 1
        
        for i in range(len(nums)-1,-1,-1):
            result[i] *= right_product
            right_product *= nums[i]

        
        return result
            

        