class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        max_len = 0
        left = 0
        res= 0

        for right in range(len(s)):
            ch = s[right]

            count[ch] = count.get(ch,0)+1
            max_freq = max(max_freq,count[ch])

            while((right-left+1)-max_freq)>k:
                count[s[left]]-=1
                left+=1

            res = max(res,right-left+1)
        return res


           


