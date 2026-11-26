# Trie Data Structure Implementation

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
            currentNode.child[char]=TrieNode()
        currentNode.isEndOfWord=True

<h>function inserting(self,word)</h>
<p>Whenever we start inserting we will start from root node so we will start 
from root, currentNode=self.root it's a node from TrieNode.
we need to go through all characters in a word so we will implemented 
for loop over it so for every iteration char= characters in word.
at first we will check whether the character is in that nodes or not if char is not in node then '''python currentNode.child[char]=TrieNode()''' orelse char is not in that node then insert it in current node and map it to new node '''python ccurrentNode.child[char]=TrieNode()''' if it's last character in that word then add True.  </p>


