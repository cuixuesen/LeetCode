class Solution:
    def binaryGap(self, N: int) -> int:
        index = [i for i,v in enumerate(bin(N)) if v == "1"]
        return max([index[i+1] - index[i] for i in range(len(index) - 1)], default = 0)