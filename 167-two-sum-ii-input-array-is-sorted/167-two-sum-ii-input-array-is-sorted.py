class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1
        output = []
        while numbers[l] + numbers[r] != target:
            if (numbers[l] + numbers[r]) < target:
                l += 1
                r += 1
            elif (numbers[l] + numbers[r]) > target:
                l -= 1
                
        output.append(l + 1)                
        output.append(r + 1)
                
        return output