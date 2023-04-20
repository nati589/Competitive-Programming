class Solution:
    def romanToInt(self, s: str) -> int:
        weight = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        stack = [weight[s[0]]]
        
        for i in range(1, len(s)):
            if weight[s[i]] > stack[-1]:
                stack[-1] = weight[s[i]] - stack[-1]
            else:
                stack.append(weight[s[i]])
        
        sum = 0
        for i in range(len(stack)):
            sum += stack[i]
            
        return sum
        