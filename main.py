from functions import*
from classes import*

"""
n n o e p
b i s e t
e a g t l
o u e v r
w o r t j
---------
N N O E P
B I S E T
E A G T L
O U E V R
W O R T J
"""
if __name__ == "__main__":
    # Load the dictionary into the tree
    dictionary_tree = Tree()
    load_dictionary_into_tree("wordlist.txt", dictionary_tree)

    # Get the 5x5 board input from the user (you can customize this part based on your needs)
    loop = 'y'
    while loop == 'y':
        board = []
        print("Enter the 5x5 board:")

        for _ in range(5):
            tile_row = []
            row = input().split()
            for tile in row:
                tile_row.append(Tile(tile))
            board.append(tile_row)

        # Find all possible words on the board
        possible_words = find_words(board, dictionary_tree)

        # Print the results

        word_value_dict = find_values(possible_words)
        print("Top 10 highest value words:")
        top_10_words = find_top_10(word_value_dict)
        for word in top_10_words:
            print(word + ': ' + str(word_value_dict[word]))
        print('')
        print('Do you want to see all the possible words? (y/n)')
        x = input()
        if x == 'y':
            for word in word_value_dict:
                print(word + ': ' + str(word_value_dict[word]))

        print('')
        print('Do you want to input a new board? (y/n)')
        loop = input()

