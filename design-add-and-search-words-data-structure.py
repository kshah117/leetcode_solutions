class TriesNode:
    def __init__(self):
        self.child = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TriesNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.child:
                cur = cur.child[c]
            else:
                cur.child[c] = TriesNode()
                cur = cur.child[c]

        cur.word = True

    def search(self, word: str) -> bool:
        def helper(word, cur):
            for i, c in enumerate(word):
                if c == '.':
                    found = False
                    for option in cur.child:
                        found = helper(word[i + 1:], cur.child[option])
                        if found:
                            return found
                    return found
                    
                else:
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]

            return cur.word
        return helper(word, self.root)