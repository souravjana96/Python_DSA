def followTheKnight(board, row, col, k):
    if row < 0 or col < 0 or row >= len(board) or col >= len(board):
        return
    
    if k == 0:
        board[row][col] = 1
        return
    
    followTheKnight(board, row+2, col-1, k - 1)
    followTheKnight(board, row+2, col+1, k - 1)
    followTheKnight(board, row-2, col-1, k - 1)
    followTheKnight(board, row-2, col+1, k - 1)
    followTheKnight(board, row-1, col+2, k - 1)
    followTheKnight(board, row-1, col-2, k - 1)
    followTheKnight(board, row+1, col-2, k - 1)
    followTheKnight(board, row+1, col+2, k - 1)


def findPositions(board, row, col, k):
    followTheKnight(board, row, col, k)

    count = 0
    for r in board:
        for ele in r:
            if ele == 1:
                count += 1
    return count

board = [[0 for _ in range(8)] for _ in range(8)]

result = findPositions(board, 3, 3, 5)
print(result)