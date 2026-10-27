class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = ""
        result = []
        for number in digits:
            res += str(number)
            

        res = int(res)

        res = res + 1
        res = str(res)

        for char in res:
            result.append(char)

        return result



        




        