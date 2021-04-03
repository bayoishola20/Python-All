# NUMBER OF ISLANDS
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        count = 0

        

        for i in range(len(grid)): # rows
            for j in range(len(grid[0])): # columns
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'
            self.dfs(grid, i+1, j) # south
            self.dfs(grid, i-1, j) # north
            self.dfs(grid, i, j+1) # east
            self.dfs(grid, i, j-1) # west



a = Solution()

# TIME COMPLEXITY O(N*M) - traversing an n by m matrix

print( a.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) ) # 1

print( a.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]) ) # 3