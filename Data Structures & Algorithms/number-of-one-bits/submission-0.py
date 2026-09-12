class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)[2:]
        print(n)
        count =0 
        for i in n:
            print(n)
            if i == "1":
                count+=1

        return count        