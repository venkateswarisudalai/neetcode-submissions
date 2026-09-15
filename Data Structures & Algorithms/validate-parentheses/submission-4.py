class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashmap = {")" : "(" , "]" : "[" , "}" : "{"}

        for char in s:
            if char in "{([":
                stack.append(char)
            elif char in "})]":
                # print(stack.pop())
                if not stack:
                    return False
                if stack.pop() != hashmap[char]:
                    return False
            

        return len(stack) == 0
