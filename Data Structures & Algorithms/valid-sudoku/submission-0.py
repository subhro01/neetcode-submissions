class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                box = (r // 3) * 3 + (c // 3)
                if board[r][c] != '.':
                    if board[r][c] in rows[r]:
                        return False
                    elif board[r][c] in cols[c]:
                        return False
                    elif board[r][c] in boxes[box]:
                        return False
                    else:
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        boxes[box].add(board[r][c])
        
        return True