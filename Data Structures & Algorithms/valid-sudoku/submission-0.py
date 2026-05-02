from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Dictionary where:
        # key = row index, value = set of numbers seen in that row
        rows = defaultdict(set)
        
        # key = column index, value = set of numbers seen in that column
        cols = defaultdict(set)
        
        # key = (row//3, col//3) → identifies each 3x3 box
        # value = set of numbers seen in that box
        squares = defaultdict(set)

        # Loop through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):

                # Skip empty cells
                if board[r][c] == ".":
                    continue

                val = board[r][c]  # current number

                # Check if number already exists in:
                # 1. current row
                # 2. current column
                # 3. current 3x3 square
                if (val in rows[r] or 
                    val in cols[c] or
                    val in squares[(r // 3, c // 3)]):
                    
                    # If duplicate found → invalid Sudoku
                    return False

                # Add the value to:
                # corresponding row set
                rows[r].add(val)
                
                # corresponding column set
                cols[c].add(val)
                
                # corresponding 3x3 square set
                squares[(r // 3, c // 3)].add(val)

        # If no duplicates found → valid Sudoku
        return True