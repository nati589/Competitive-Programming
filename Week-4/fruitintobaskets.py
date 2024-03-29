class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = i = 0
        count = collections.Counter()
        tree = fruits
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans