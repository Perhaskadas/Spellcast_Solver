def load_dictionary_into_tree(file_path, tree):
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip().lower()
            tree.insert(word)


def find_words_on_board(board, tree):
    def backtrack(row, col, node, path, visited):
        if node.is_end_of_word:
            found_words.add(''.join(path))

        visited[row][col] = True
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < 5 and 0 <= new_col < 5 and not visited[new_row][new_col]:
                    letter = board[new_row][new_col]
                    if letter in node.children:
                        backtrack(new_row, new_col, node.children[letter], path + [letter], visited)

        visited[row][col] = False

    found_words = set()
    visited = [[False for _ in range(5)] for _ in range(5)]

    for r in range(5):
        for c in range(5):
            starting_letter = board[r][c]
            if starting_letter in tree.root.children:
                backtrack(r, c, tree.root.children[starting_letter], [starting_letter], visited)

    return found_words