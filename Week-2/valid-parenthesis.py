class Solution:
    def isValid(self, s: str) -> bool:
        output = []
        check = [']', ')', '}']
        for index in range(len(s)):
            if s[index] in check:
                if len(output) > 0:
                    last_value = output[-1]
                    if s[index] == chr(ord(last_value) + 1) or s[index] == chr(ord(last_value) + 2):
                        output.pop()
                    else:
                        return False
                else:
                    return False
            else:
                output.append(s[index])
        if len(output) == 0:
            return True
        else:
            return False
