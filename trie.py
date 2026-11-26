class TrieNode():
    def __init__(self):
        self.child=dict()
        self.isEndOfWord=False

class TrieDataStructure():
    def __init__(self):
        self.root = TrieNode()

    def inserting(self, word):
        currentNode=self.root
        for char in word:
            if char not in currentNode.child:
                currentNode.child[char]=TrieNode()
            currentNode=currentNode.child[char]
        currentNode.isEndOfWord=True

    def searching(self, word):
        currentNode=self.root
        for char in word:
            if char not in currentNode.child:
                return False
            currentNode=currentNode.child[char]
        return currentNode.isEndOfWord

    def prefixSearching(self, prefix):
        currentNode=self.root
        for char in prefix:
            if char not in currentNode.child:
                return False
            currentNode=currentNode.child[char]
        return True

    def displayingAutoCompleteSuggestions(self, prefix):
        pass

    
