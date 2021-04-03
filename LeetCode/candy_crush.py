# CANDY CRUSH
class Solution:
    def candyCrush(self, board):
        if not board:
            return board
        
        done = True

        # STEP 1: Crush rows

        for r in range(len(board)):                 # rows
            for c in range(len(board[r]) - 2):      # columns at 2 upwards
                num1 = abs(board[r][c])
                num2 = abs(board[r][c+1])
                num3 = abs(board[r][c+2])

                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r][c+1] = -num2
                    board[r][c+2] = -num3
                    done = False

        # STEP 2: Crush columns
        for c in range(len(board[0])):
            for r in range(len(board) -2):
                num1 = abs(board[r][c])
                num2 = abs(board[r+1][c])
                num3 = abs(board[r+2][c])
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = -num1
                    board[r+1][c] = -num2
                    board[r+2][c] = -num3
                    done = False
        
        # STEP 3:
        if not done:
            for c in range(len(board[0])):
                # move all positive numbers down
                idx = len(board) - 1
                for r in range(len(board) -1, -1, -1): #  get to the bottom then move upwards on the board
                    if board[r][c] > 0:
                        board[idx][c] = board[r][c]
                        idx -= 1

                # put zeros in for missing pieces
                for r in range(idx, -1, -1):
                    board[r][c] = 0

        return board if done else self.candyCrush(board)





a = Solution()

print(a.candyCrush(
    [
        [110, 5, 112, 113, 114],
        [210, 211, 5, 213, 214],
        [310, 311, 3, 313, 314],
        [410, 411, 412, 5, 414],
        [5, 1, 512, 3, 3],
        [610, 4, 1, 613, 614],
        [710, 1, 2, 713, 714],
        [810, 1, 2, 1, 1],
        [1, 1, 2, 2, 2],
        [4, 1, 4, 4, 1014]
    ]
))