class Solution:
    def getCount(self, n):
        if n == 1:
            return 10

        moves = {
            0: [0, 8],
            1: [1, 2, 4],
            2: [2, 1, 3, 5],
            3: [3, 2, 6],
            4: [4, 1, 5, 7],
            5: [5, 2, 4, 6, 8],
            6: [6, 3, 5, 9],
            7: [7, 4, 8],
            8: [8, 5, 7, 9, 0],
            9: [9, 6, 8]
        }

        dp = [1] * 10

        for _ in range(2, n + 1):
            new = [0] * 10
            for digit in range(10):
                for nxt in moves[digit]:
                    new[digit] += dp[nxt]
            dp = new

        return sum(dp)
