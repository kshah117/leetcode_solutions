class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_words(self, word):
        cur = self.root
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()

            cur = cur.child[c]

        cur.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        word_tries = Trie()
        for word in words:
            word_tries.add_words(word)

        m = len(board)
        n = len(board[0])
        res = set()
        visited = set()

        def helper(r, c, word, node):
            if (
                ((r, c) in visited)
                or (r < 0)
                or (r == m)
                or (c < 0)
                or (c == n)
                or (board[r][c] not in node.child)
            ):
                return

            visited.add((r, c))
            node = node.child[board[r][c]]
            word += board[r][c]
            if node.is_word:
                res.add(word)

            helper(r + 1, c, word, node)
            helper(r - 1, c, word, node)
            helper(r, c + 1, word, node)
            helper(r, c - 1, word, node)

            visited.remove((r, c))

        for r in range(m):
            for c in range(n):
                helper(r, c, "", word_tries.root)

        return list(res)
