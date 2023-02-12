class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        while len(stones) > 1:
            stones.sort()
            stone1 = stones.pop()
            stone2 = stones.pop()
            if stone1 > stone2:
                stones.append(stone1 - stone2)
        
        if not len(stones):
            return 0
        elif len(stones) == 1:
            return stones[0]
        else:
            return abs(stones[1] - stones[0])