from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap= defaultdict(set)
        columnMap = defaultdict(set)
        # checking for repetiion in rows
        squareMap = defaultdict(set)
        
        for row in range(9):
            for column in range(9):
                entrie = board[row][column]
                if entrie == ".":
                    continue
                if  (entrie in rowMap[row] or entrie in columnMap[column] or entrie in squareMap[(row//3)*3 + (column//3)]):
                    return False
                else:
                    rowMap[row].add(entrie)
                    columnMap[column].add(entrie)
                    squareMap[(row//3)*3 + (column//3)].add(entrie)
        return True
                    
            

        
       
          
        
    
        


                
                
     

        
        
        
           
            
            
                
        