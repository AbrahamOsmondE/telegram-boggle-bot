from generate_trie import generate_trie
import collections
import sys

def find_words(board):
    WORD_KEY = '$'
    
    rowNum = len(board)
    colNum = len(board[0])
    trie = generate_trie()
    matchedWords = []
    dicti = collections.defaultdict(list)
    
    def backtracking(row, col, parent):

        letter = board[row][col]
        currNode = parent[letter]

        # check if we find a match of word
        word_match = currNode.pop(WORD_KEY, False)
        if word_match:
            # also we removed the matched word to avoid duplicates,
            #   as well as avoiding using set() for results.
            matchedWords.append(word_match)
            dicti[len(word_match)].append(word_match)

        # Before the EXPLORATION, mark the cell as visited
        board[row][col] = '#'
        if letter == "Q" and "U" in currNode:
            tempNode = currNode["U"]
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in tempNode:
                    continue
                backtracking(newRow, newCol, tempNode)
        
        # Explore the neighbors in 4 directions, i.e. up, right, down, left
        for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            newRow, newCol = row + rowOffset, col + colOffset
            if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                continue
            if not board[newRow][newCol] in currNode:
                continue
            backtracking(newRow, newCol, currNode)

        # End of EXPLORATION, we restore the cell
        board[row][col] = letter

        # Optimization: incrementally remove the matched leaf node in Trie.
        if not currNode:
            parent.pop(letter)

    for row in range(rowNum):
        for col in range(colNum):
            if board[row][col] in trie:
                backtracking(row, col, trie)

    string = ""
    for i in range(15, 2, -1):
        if dicti[i] == []:
            continue
        string += str(i) + " LETTERS" + " (" + str(len(dicti[i])) + ") " + "\n\n"
        string += "\n".join(dicti[i]) + "\n\n"
    return string

sys.modules[__name__] = find_words