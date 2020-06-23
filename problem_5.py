#!/usr/bin/env python
# coding: utf-8

# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# In[1]:


## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.trie = dict()
        self.word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in list(self.trie.keys()):
            self.trie[char] = TrieNode()
            
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        ans = list()

        if self.word and suffix != '':
            ans.append(suffix)

        if len(self.trie) == 0:
            return ans

        ans = list()

        if self.word and suffix != '':
            ans.append(suffix)

        for i in self.trie:
            ans.extend(self.trie[i].suffixes(suffix = suffix + i))

        return ans
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.trie = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        trie = self.trie

        for i in word:
            trie.insert(i)
            trie = trie.trie[i]

        trie.word = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        trie = self.trie

        for i in prefix:
            if i not in trie.trie:
                return False
            trie = trie.trie[i]

        return trie


# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# In[31]:


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod",
    "Search anything...", "descendants", "descendant", "moon"
]
for word in wordList:
    MyTrie.insert(word)


# In[32]:


def my_test(expected, t):
    try:
        output = MyTrie.find(t).suffixes()
    
        if output == expected:
            print("\033[1;32;40m Accepted\n")
        else:
            print("\033[1;31;40mWrong Answer\n")
    except:
        print("\033[1;31;40mWrong Answer\n")


# In[33]:


my_test(['hology', 'agonist', 'onym'], "ant")


# In[34]:


my_test(['logy'], "antho")


# In[37]:


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
        print('Welcome to Google! Search anything today!')

interact(f,prefix='Search anything...')
widgets.Button(description='I\'m feeling lucky!')


# In[ ]:




