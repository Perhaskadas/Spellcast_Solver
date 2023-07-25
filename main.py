from functions import*
from classes import*


if __name__ == "__main__":
    # Load the dictionary into the tree
    dictionary_tree = Tree()
    load_dictionary_into_tree("wordlist.txt", dictionary_tree)

    # Get the 5x5 board input from the user (you can customize this part based on your needs)
    board = []
    print("Enter the 5x5 board:")
    for _ in range(5):
        row = input().split()
        board.append(row)
    print(board)

    # Find all possible words on the board
    possible_words = find_words_on_board(board, dictionary_tree)

    # Print the results
    print("Possible words on the board:")
    for word in possible_words:
        print(word)