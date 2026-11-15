class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1)>len(s2)):
            return False

        window_size = len(s1)
        left = 0

        for right in range(len(s2)):

            if right-left+1 == window_size:

                if sorted(s2[left:right+1]) == sorted(s1):
                    return True

                left+=1
        return False
                    


            
            


        