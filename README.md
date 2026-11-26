# Trie Data Structure Implementation

    class TrieNode():
        def __init__(self):
            self.child=dict()
            self.isEndOfWord=False

    class TrieDataStructure():
        def __init__(self):
            self.root = TrieNode()

## class TrieNode
<p>It's like a container which has will keep the character in dictionary 
    which has key has the character in word in child variable.
    Using dictionary we can easily map character to another node ,e.g
    '''python
        child[character]=TrieNode
        '''
    Likewise in here too ....</p>
<p>isEndOfWord is like a bottom of that container it is to verify whether 
    character in word is last character or not </p>

## class TrieDataStucture
<p>Here in this class we are initializing root as TrieNode</p>

    def inserting(self, word):
        currentNode=self.root
        for char in word:
            if char not in currentNode.child:
                currentNode.child[char]=TrieNode()
            currentNode=currentNode.child[char]
        currentNode.isEndOfWord=True

<h1>function inserting(self,word)</h1>

<p>Whenever we start inserting we will start from root node so we will start 
from root, currentNode=self.root it's a node from TrieNode.
we need to go through all characters in a word so we will implemented 
for loop over it so for every iteration char= characters in word.
at first we will check whether the character is in that nodes or not if char is not in node then '''python currentNode.child[char]=TrieNode()''' orelse char is not in that node then insert it in current node and map it to new node '''python ccurrentNode.child[char]=TrieNode()''' if it's last character in that word then add True.  </p>

    def searching(self, word):
        currentNode=self.root
        for char in word:
            if char not in currentNode.child:
                return False
            currentNode=currentNode.child[char]
        return currentNode.isEndOfWord

<h1> function searching(self,word)</h1>

<p>whenever we start searching we will start from root node right so we are initializing '''python currentNode=self.root". In searching we will search all the characters in the word so with the help of for loop we can check all the character in word by comparing character with node value then currentNode will carry forward until the boolean value True because that is end of word in trie.</p>

    def prefixSearching(self, prefix):
        currentNode=self.root
        for char in prefix:
            if char not in currentNode.child:
                return False
            currentNode=currentNode.child[char]
        return True

<h1> function prefixSearching(self,prefix)</h1>

<p>It's almost similar to searching like at first we will initialize currentNode is root because search starts from root node then it will flows from one node to other.</p>


