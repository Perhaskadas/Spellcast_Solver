"""from classes import*
def load_dictionary_into_tree(file_path, tree: Tree) -> None:
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip().lower()
            tree.insert(word)


def find_words(board: list[list[Tile]], tree: Tree) -> set:
    def backtrack(row, col, node, path, visited):
        if node.is_end_of_word:
            found_words.append(path)

        visited[row][col] = True
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < 5 and 0 <= new_col < 5 and not visited[new_row][new_col]:
                    letter = board[new_row][new_col]
                    if letter.value in node.children:
                        backtrack(new_row, new_col, node.children[letter.value], path + [letter], visited)

        visited[row][col] = False

    found_words = []
    visited = [[False for _ in range(5)] for _ in range(5)]

    for r in range(5):
        for c in range(5):
            starting_letter = board[r][c]
            if starting_letter.value in tree.root.children:
                backtrack(r, c, tree.root.children[starting_letter.value], [starting_letter], visited)
    return found_words


def find_values(words: list[list[Tile]]) -> dict:
    words_with_values = {}
    letter_values = {'a': 1, 'e': 1, 'i': 1, 'o': 1,
                     'n': 2, 'r': 2, 's': 2, 't': 2,
                     'd': 3, 'g': 3, 'l': 3,
                     'b': 4, 'h': 4, 'p': 4, 'm': 4, 'u': 4, 'y': 4,
                     'c': 5, 'f': 5, 'v': 5, 'w': 5,
                     'k': 6,
                     'j': 7, 'x': 7,
                     'q': 8,'z': 8,
                     }
    for word in words:
        twotime = False
        total = 0
        word_string = ''
        for tile_letter in word:
            word_string = word_string + tile_letter.value
            if tile_letter.modifier == 'dl':
                total += 2 * letter_values[tile_letter.value]
            elif tile_letter.modifier == 'tl':
                total += 3 * letter_values[tile_letter.value]
            elif tile_letter.modifier == '2x':
                twotime = True
                total += letter_values[tile_letter.value]
            else:
                total += letter_values[tile_letter.value]
        if twotime:
            total = total * 2
        if len(word_string) >= 6:
            total += 10
        words_with_values[word_string] = total
    return words_with_values

def find_top_10(word_and_value: dict) -> dict:
    top_10_words_list = sorted(word_and_value, key=lambda x: word_and_value[x], reverse=True)[:10]
    top_10_words_dict = {}
    for word in top_10_words_list:
        top_10_words_dict[word] = word_and_value[word]
    return top_10_words_dict"""
