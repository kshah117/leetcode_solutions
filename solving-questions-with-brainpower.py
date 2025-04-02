class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]
        for i in range(len(questions) - 2, -1, -1):
            skip = questions[i][1]
            if i + skip + 1 < len(questions):
                dp[i] += questions[i][0] + dp[i + skip + 1]
            else:
                dp[i] = questions[i][0]

            dp[i] = max(dp[i], dp[i + 1])

        return dp[0]
