class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda x :x[0])
        if len(intervals)==0:
            return
            
        result = [intervals[0]]

        for i in range(1,len(intervals)):
            current_interval = result[-1]
            next_interval = intervals[i]
            if current_interval[1] >= next_interval[0]:
                current_interval[1] = max(current_interval[1],next_interval[1])
            else:
                result.append(next_interval)
        return result


        