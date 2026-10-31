class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        sum = 0
        def backtrack(start,remaining):
            if remaining == 0:
                res.append(combination.copy())
                return 

            if remaining < 0:
                return

            
            
            for i in range(start,len(nums)):
                
                combination.append(nums[i])
                backtrack(i,remaining-nums[i])
                combination.pop()


        backtrack(0,target)
        return res


            








        