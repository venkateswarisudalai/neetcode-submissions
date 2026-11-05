class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        hashmap = {}
        for char in s:
            if char not in hashmap:
                hashmap[char]=1
            else:
                hashmap[char]+=1

        for char in t:
            if char in hashmap:
                hashmap[char]-=1
            else:
                return False

        return all(value==0 for value in hashmap.values())

        
        