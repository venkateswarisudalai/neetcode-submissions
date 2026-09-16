class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                #if the temperature is greater than the top of the element stack  then i need to pop the stack and find the diffference between the 

                stackt , stackindex = stack.pop()

                result[stackindex] = i - stackindex
            stack.append([t,i])
        return result