class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        top_k = sorted(hashmap,key=hashmap.get,reverse=True)
        top_k = top_k[:k]

        return top_k
        