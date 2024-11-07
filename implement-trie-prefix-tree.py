class TrieNode:
    def __init__(self):
        self.child = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.child:
                cur = cur.child[c]
            else:
                cur.child[c] = TrieNode()
                cur = cur.child[c]

        cur.word = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.child:
                cur = cur.child[c]
            else:
                return False

        return cur.word 


    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.child:
                cur = cur.child[c]
            else:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)