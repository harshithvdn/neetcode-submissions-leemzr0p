class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen= set()
        for n in range(9):
            for m in range(9):
                val=board[n][m]

                if val==".":
                    continue

                box=(n//3,m//3)

                row_key=("row", n, val)
                column_key=("column", m, val)
                box_key=("box", box, val)

                if row_key in seen or column_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(column_key)
                seen.add(box_key)
        return True

             

        
            
            

        