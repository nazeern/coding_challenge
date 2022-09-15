class TrieNode:
    """A single Node of the Trie structure."""

    def __init__(self, char):
        # The character this node holds
        self.char = char

        # Whether this node marks the end of a word
        self.is_end = False

        # The number of times this word is in the word set
        self.counter = 0

        # (key, value) = (character, node)
        self.children = {}


class Trie:

    def __init__(self, words=None):
        self.root = TrieNode("")
        for word in words:
            self.insert(word)

    
    def insert(self, word):
        curr_node = self.root

        for char in word:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                new_node = TrieNode(char)
                curr_node.children[char] = new_node
                curr_node = new_node
        
        curr_node.is_end = True

        curr_node.counter += 1


    def dfs(self, node, prefix):
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)




    def complete_prefix(self, prefix):
        self.output = []
        curr_node = self.root

        for char in prefix:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return []

        self.dfs(curr_node, prefix[:-1])

        return sorted([x[0] for x in self.output], key=lambda x: x[1], reverse=True)

        
        



def autocomplete(words, prefix):
    """
    Implement an autocomplete system. 
    That is, given a query string s and a set of all possible query strings, 
    return all strings in the set that have s as a prefix.
    >>> autocomplete(["dog", "deer", "deal"], "de")
    ["deer", "deal"]
    """
    words_trie = Trie(words)
    return words_trie.complete_prefix(prefix)


if __name__ == "__main__":
    print(autocomplete(["dog", "deer", "deal"], "de"))


    

    

