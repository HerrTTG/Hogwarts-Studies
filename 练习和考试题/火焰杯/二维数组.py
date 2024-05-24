class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        """
        中间是你要实现的代码

        示例：
        M x N二维数组
        grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
        规则：
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 100
        -100 <= grid[i][j] <= 100
        """

        count = 0
        for i in range(len(grid)):
            for j in grid[i]:
                if j < 0:
                    count += 1
        return count


if __name__ == '__main__':
    tester = Solution()
    result = tester.countNegatives([[3, 2], [1, 0]])
    print(result)
