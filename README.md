# Trie Data Structure Implementation

class TrieDataStructure():
    def __init__(self):
        self.root = TrieNode()

### class TrieNode
<p>It's like a container which has will keep the character in dictionary 
    which has key has the character in word in child variable.
    Using dictionary we can easily map character to another node ,e.g
    '''python
        child[character]=TrieNode
        '''
    Likewise in here too ....</p>
<p>isEndOfWord is like a bottom of that container it is to verify whether 
    character in word is last character or not </p>

### TrieDataStucture
<p>Here in this class we are initializing root as TrieNode</p>

