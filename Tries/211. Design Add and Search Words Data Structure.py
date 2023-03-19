class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currLevel = self.root
        for ch in word:
            if ch not in currLevel.children.keys():
                currLevel.children[ch] = TrieNode()
            currLevel = currLevel.children[ch]
        currLevel.isEndOfWord = True

    def search(self, word: str) -> bool:
        return self.searchHelper(word, 0, self.root)

    def searchHelper(self, word: str, index: int, node: TrieNode) -> bool:
        if len(word) == index:
            return node.isEndOfWord
        elif word[index] != '.' and word[index] in node.children:
            if(self.searchHelper(word, index + 1, node.children[word[index]])):
                return True
        elif word[index] == '.':
            for child in node.children:
                if(self.searchHelper(word, index + 1, node.children[child])):
                    return True
                else:
                    continue
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
# print(obj.search(".at"))
# obj.addWord("bat")
# print(obj.search(".at"))
# print(obj.search("b."))
print(obj.search("a.d"))
