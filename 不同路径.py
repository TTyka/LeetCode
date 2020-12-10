class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 因为无论怎么走都会在移动的n+m-2步中选出n-1步向下走，或者选m-1步向右走，因此只需要从n+m-2中选出n-1即可，即求组合数。
        return  comb(m + n - 2, n - 1)
        # “因为要到每一个格子只可能从他的左边或上边的格子，而最左最上为路径为1，因此可以用动态规划来解。”
        # dp = [[0] * n for _ in range(m)]

        # # 初始化
        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1
        # # 根据转移方程进行递推
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # return dp[m-1][n-1]