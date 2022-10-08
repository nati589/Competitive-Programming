class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushIndex = 0
        popIndex = 0
        output = []
        size = len(pushed)

        while len(popped) > 0:
            if len(pushed) == 0 and len(output) == 0:
                return False
            if len(pushed) == 0:
                if output[0] == popped[0]:
                    output.pop(0)
                    popped.pop(0)
                else:
                    print(output)
                    return False
            else:
                if len(output) != 0:
                    if output[0] == popped[0]:
                        output.pop(0)
                        popped.pop(0)
                    else:
                        output.insert(0, pushed[0])
                        pushed.pop(0)
                        if output[0] == popped[0]:
                            output.pop(0)
                            popped.pop(0)
                else:
                    output.insert(0, pushed[0])
                    pushed.pop(0)
                    if output[0] == popped[0]:
                        output.pop(0)
                        popped.pop(0)

        if len(output) != 0:
            return False
        else:
            return True
