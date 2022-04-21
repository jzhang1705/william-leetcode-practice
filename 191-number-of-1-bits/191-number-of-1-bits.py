class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        while n:
            n &= (n-1)
            num_ones += 1
        return num_ones
    