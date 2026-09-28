class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["#"]

        for c in s:
            if stack[-1] == '(' and c == ')':
                stack.pop()
            elif stack[-1] == '{' and c == '}':
                stack.pop()
            elif stack[-1] == '[' and c == ']':
                stack.pop()
            else:
                stack.append(c)
        
        print(stack)
        return len(stack) == 1
            
        