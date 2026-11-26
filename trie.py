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
        currentNode=self.root
        for char in prefix:
            if char not in currentNode.child:
                return []
            currentNode=currentNode.child[char]
        suggestions=[]
        self.completeSuggestions(currentNode, prefix, suggestions)
        return suggestions

    def completeSuggestions(self, node, prefix, suggestions):
        if node.isEndOfWord:
            suggestions.append(prefix)
        for char, child_node in node.child.items():
            self.completeSuggestions(child_node, prefix + char, suggestions)
