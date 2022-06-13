from string import ascii_lowercase


board = [[0 for i in range(8)] for i in range(8)]

def get_figure_cords(cords):
    let_cord, num_cord = cords[0], int(cords[1])
    let_num = ascii_lowercase.index(let_cord)

    let_cord = let_num

    return (num_cord-1, let_cord)


def delete_lines(tura_cords):
    line, col = tura_cords
    for row_index in range(8):
        for col_index in range(8):
            if row_index == line:
                if board[line][col_index] == 0:
                    board[line][col_index] = 1
            else:
                board[row_index][col] = 1


def delete_diagonals(tura_cords):
    row_index, col_index = tura_cords
    m = row_index - 1
    n = col_index + 1
    # вправо вверх
    while m > -1 and n < 8: # запитати за цикл в циклі?
        board[m][n] = 1
        n+=1
        m-=1

    # вправо вниз
    k = row_index + 1
    p = col_index + 1
    while k < 8 and p < 8:
        board[k][p] = 1
        p+=1
        k+=1

    # # вліво вверх
    h = row_index - 1
    l = col_index - 1
    while h > -1 and l > -1:
        board[h][l] = 1
        l-=1
        h-=1
    
    # # вліво вниз
    q = row_index + 1
    j = col_index - 1
    while q < 8 and j > -1:
        board[q][j] = 1
        q+=1
        j-=1

def choose_change_coords(board):
    lst = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                lst.append([i, j])
    result = set()
    for elem in lst:
        elem[1] +=1
        elem[1] = str(elem[1])
        elem[0] = ascii_lowercase[elem[0]]
        result.add(elem[0]+elem[1])
    return result

def chess_puzzle(ferz1_cords, ferz2_cords):
    ferz2_cords = get_figure_cords(ferz2_cords)
    ferz1_cords = get_figure_cords(ferz1_cords)
    delete_lines(ferz1_cords)
    delete_lines(ferz2_cords)
    delete_diagonals(ferz1_cords)
    delete_diagonals(ferz2_cords)
    def draw_board(board):
        for row in board:
            print(row)
    draw_board(board)
    return choose_change_coords(board)
if __name__ == '__main__':
    print(chess_puzzle('b5', 'f4'))