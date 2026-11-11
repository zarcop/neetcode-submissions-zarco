class PrefixTree:

    class Node:
        def __init__(self, char=None):
            self.char = char
            self.children = {}
            self.is_end = False

        def add(self, char):
            if char not in self.children:
                new_char = self.__class__(char)
                self.children[char] = new_char
                
    def __init__(self):
        self.root = self.Node() #empty root

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.add(char)
            curr = curr.children[char]
        curr.is_end = True


    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return curr.is_end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
        return True

        
        