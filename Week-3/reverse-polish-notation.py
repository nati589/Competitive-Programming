class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = []
        operands = []
        for token in tokens:
            try:
                int(token)
                is_dig = True
            except ValueError:
                is_dig = False
            if is_dig:
            # if token.isnumeric(): 
                operands.insert(0, int(token))
            else: 
                value1 = operands.pop(0)                    
                value2 = operands.pop(0)
                if token == '+':
                    operands.insert(0, value1 + value2)
                elif token == '-':
                    operands.insert(0, value2 - value1)
                elif token == '*':
                    operands.insert(0, value1 * value2)
                else:
                    operands.insert(0, int(value2 / value1))
        return operands[0]