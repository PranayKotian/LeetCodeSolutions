class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True

    def search(self, word: str) -> bool:
        def dfs(text, node):
            if text == "":
                return node.end
            
            c = text[0]
            if c == ".":
                for c in node.children:
                    if dfs(text[1:], node.children[c]):
                        return True
                return False
            
            if c not in node.children:
                return False
            return dfs(text[1:], node.children[c])
        
        return dfs(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)