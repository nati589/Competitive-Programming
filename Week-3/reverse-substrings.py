class Solution:
    def reverseParentheses(self, s: str) -> str:
        output = []
        container = []
        for index in range(len(s)):
            if s[index] != ')':
                output.insert(0, s[index])
            else:
                while output[0] != '(':
                    container.append(output.pop(0))
                output.pop(0)
                for item in container:
                    output.insert(0, item)
                container = []
        s = ''
        for index in reversed(range(len(output))):
            s += output[index]
        return s
