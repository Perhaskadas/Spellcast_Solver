class Board:
    pass


class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Tree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TreeNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word