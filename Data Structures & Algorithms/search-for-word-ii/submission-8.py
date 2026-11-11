class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:


        # 2d grid

        # list of the strings word



        class TrieNode:
            def __init__(self):
                self.children = {}
                self.word = None
        

        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        
        rows = len(board)
        columns  = len(board[0])
        result = set()


        def dfs_traverse(row, column, node):
            if (row < 0 or columns < 0 or row >= rows or column >= columns or column < 0  or board[row][column] not in node.children):
                return 
            char = board[row][column]
            curr_node = node.children[char]

            if curr_node.word:
                result.add(curr_node.word)
                curr_node.word  = None
            board[row][column] = '#'
            dfs_traverse(row-1, column, curr_node)
            dfs_traverse(row+1, column, curr_node)
            dfs_traverse(row, column- 1, curr_node)
            dfs_traverse(row, column + 1, curr_node)
            board[row][column] = char
        

        for row in range(rows):
            for column in range(columns):
                dfs_traverse(row, column, root)

        return list(result)
        

        

        







    

    

        
        

    
            













        