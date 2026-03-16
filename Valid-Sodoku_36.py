class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #create an empty set for seen values
        
        seen = set()

        #for each row and column
        
        for row in range(9):

            for column in range(9):

                #get value

                value = board[row][column]

                #if value is . skip

                if value != '.':

                    #add row,column and grid context with value to set

                    row_id = f"{value} in row {row}"
                    column_id = f"{value} in column {column}"
                    #row/column mod 3 gives us a grid coord - first grid = 0,0
                    grid_id = f"{value} in grid {row//3}-{column//3}"

                    if row_id in seen or column_id in seen or grid_id in seen:

                        #if already in set invalid return false

                        return False

                    #otherwise add id's to set

                    seen.add(row_id)
                    seen.add(column_id)
                    seen.add(grid_id)

        #if we get here return true
        return True
