class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        def dfs(start,subset):
            res.append(subset.copy())

            for i in range(start,len(nums)):
                subset.append(nums[i])
                print("Add:", subset)
                dfs(i+1,subset)
                subset.pop()
                print("Pop:", subset)
        dfs(0,[])
        return res


 

        