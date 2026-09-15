class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:
            if token == "*":
                a = stack.pop()
                b = stack.pop()
                result = b * a
                stack.append(result)
            elif token == "+":
                a = stack.pop()
                b = stack.pop()
                result = b + a
                stack.append(result)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                result = int(b/a)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]



                
            

        