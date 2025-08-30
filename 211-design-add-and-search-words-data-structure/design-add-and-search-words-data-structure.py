class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def search(self, word: str, index: int) -> bool:
        if len(word) == index:
            return self.is_end
        
        char = word[index]
        
        if char == '.':
            # Wildcard: try all possible children
            for child in self.children.values():
                if child.search(word, index + 1):
                    return True
            return False
        else:
            # Regular character: check if it exists in children
            if char in self.children:
                return self.children[char].search(word, index + 1)
            return False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TreeNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self.root.search(word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)