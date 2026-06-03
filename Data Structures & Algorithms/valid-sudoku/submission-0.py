class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9): 
            for c in range(9): 
                value = board[r][c]
        
                if value == ".":
                    continue 

                square_index = (r // 3) * 3 + (c // 3)

                if value in rows[r] or value in columns[c] or value in squares[square_index]:
                    return False 
        
                rows[r].add(value)
                columns[c].add(value)
                squares[square_index].add(value)


        return True