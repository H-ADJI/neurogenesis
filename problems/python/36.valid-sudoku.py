# Category: algorithms
# Level: Medium
# Percent: 61.42863%


# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
#
# 	Each row must contain the digits 1-9 without repetition.
# 	Each column must contain the digits 1-9 without repetition.
# 	Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
#
# Note:
#
#
# 	A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# 	Only the filled cells need to be validated according to the mentioned rules.
#
#
#
# Example 1:
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
# Example 2:
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
#
#
# Constraints:
#
#
# 	board.length == 9
# 	board[i].length == 9
# 	board[i][j] is a digit 1-9 or '.'.
#


from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        current_boxes = [set() for _ in range(3)]
        current_columns = [set() for _ in range(9)]
        for i, row in enumerate(board):
            current_row = set()
            for j, num in enumerate(row):
                if num == ".":
                    continue
                if num in current_row or num in current_boxes[j // 3] or num in current_columns[j]:
                    return False
                current_row.add(num)
                current_boxes[j // 3].add(num)
                current_columns[j].add(num)
            if (i + 1) % 3 == 0:
                current_boxes = [set() for _ in range(3)]
        return True
