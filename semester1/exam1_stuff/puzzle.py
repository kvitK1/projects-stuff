"""module checking if the board is ready for the game"""


def create_bord(board):
    """
    Create list from the board.
    Return list.
    """
    lst = []
    for elem in board:
        elem1 = list(elem)
        lst.append(elem1)
    return lst


def check_horizontal(lst):
    """
    Check if row have same numbers.
    Return True or False whether there are the same numbers or not.
    """
    data = []
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            if lst[i][j] != "*":
                counter = lst[i].count(lst[i][j])
                if counter > 1:
                    data.append(False)
                else:
                    data.append(True)
    if False in data: return False
    else: return True


def check_vertical(lst):
    """
    Check if columns have the same numbers.
    Return True if all numbers are unique, and False if not.
    """
    new_lst = []
    for i in range(len(lst[0])):
        lstk = []
        for j in range(len(lst)):
            el = lst[j][i]
            lstk.append(el)
        new_lst.append(lstk)
    data = []
    for i in range(len(new_lst)):
        for j in range(len(new_lst[0])):
            if new_lst[i][j] != "*":
                counter = new_lst[i].count(new_lst[i][j])
                if counter > 1:
                    data.append(False)
                else:
                    data.append(True)
    if False in data: return False
    else: return True


def check_violet(board):
    """
    Check if numbers in violet figure are not the same.
    Return True or False whether there are the same numbers or not.
    """
    violet = []
    data = []
    violet.append(board[0][3:6]+[board[1][4]]+[board[2][4]]+[board[3][4]]+board[4][3:6])
    for element in violet:
        if element != "*":
                counter = violet.count(element)
                if counter > 1:
                    data.append(False)
                else:
                    data.append(True)
    if False in data: return False
    else: return True

def check_orange(board):
    """
    Check if numbers in orange figure are not the same.
    Return True or False whether there are the same numbers or not.
    """
    orange = []
    data = []
    orange.append(board[5][:2]+board[5][7:]+board[6][:2]+board[6][7:]+\
        board[7][:2]+board[7][7:]+board[8][:3]+board[8][6:])
    for element in orange:
        if element != "*":
            counter = orange.count(element)
            if counter > 1:
                data.append(False)
            else:
                data.append(True)
    if False in data: return False
    else: return True


def check_green(board):
    """
    Check if numbers in green figure are not the same.
    Return True or False whether there are the same numbers or not.
    """
    pass


def check_yellow(board):
    """
    Check if numbers in yellow figure are not the same.
    Return True or False whether there are the same numbers or not.
    """
    pass


# def colorful_figures(board):
#     """
#     Check if figures of different colors have the same numbers.
#     Return True if all numbers are unique, and False if not.
#     """
#     violet = check_violet(board)
#     orange = check_orange(board)
#     green = check_green(board)
#     yellow = check_yellow(board)
#     pass
    # if violet == orange == green == yellow == True: return True
    # else: return False


def validate_board(board):
    """
    The main function.
    Combine all additional functions to check if all conditions are True.
    Return True, if the board is correct, and False, if vice versa.
    """
    lst = create_bord(board)
    first = check_vertical(lst)
    second = check_horizontal(lst)
    # third = colorful_figures(lst)
    if first == False or second == False: return False
    elif first == True and second == True: return True

boar = [
"*1**4***5",
"**3***27*",
"4***2**6*",
"*76**91**",
"**83**5**",
"*4**8**3*",
"***7*1**8",
"2**5***4*",
"*6***2**9"
]

print(validate_board(boar))
