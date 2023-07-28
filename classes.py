class Tile:
    """
    A class that represents a single tile in the board, it contains the letter it represents
    and any possible modifiers
    """
    def __init__(self, value: str):
        """
        Takes a string with a letter and a possible symbol and initializes the class.
        * = double value letter
        & = triple value letter
        ^ = 2x value of total word
        default is no_mod
        :param value: string
        """
        if '*' in value:
            self.modifier = "dl"
        elif '&' in value:
            self.modifier = "tl"
        elif '^' in value:
            self.modifier = "2x"
        else:
            self.modifier = "no_mod"
        self.value = value.strip('^&*')

    def __call__(self):
        return self.value


class TreeNode:
    """
    Represents a node in the Trie data structure.

    Attributes:
        children (dict): A dictionary representing the children nodes, where keys are characters and values are TrieNode objects.
        is_end_of_word (bool): A flag indicating whether the current node represents the end of a valid word.
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Tree:
    """
    Represents a Trie data structure for efficient word lookup. Takes no parameters
    """

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie.

        :param word: The word to be inserted into the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the Trie and returns True if found, False otherwise.

        :param word: The word to be searched in the Trie.
        :return: True if the word is found in the Trie, False otherwise.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word