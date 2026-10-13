class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(current,opencount,closedcount):
            if len(current) == 2 * n:
                res.append(current)
                return

            if opencount < n:
                backtrack(current+"(",opencount+1,closedcount)
            if closedcount < opencount:
                backtrack(current+")",opencount,closedcount+1)

        backtrack("",0,0)
        return res
        