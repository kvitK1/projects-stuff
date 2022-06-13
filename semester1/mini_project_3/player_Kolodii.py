#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    This is a bot for the 3rd project.
    Maybe, a pretty bad bot, but it fills maps, so...
"""

from random import choice
from logging import DEBUG, debug, getLogger


getLogger().setLevel(DEBUG)

field_height = 0
field_width = 0

figure_height = 0
figure_width = 0

def parse_field_info():
    """
    Parse the info about the field.

    The input may look like this:

    Plateau 15 17:
    """
    global field_height, field_width
    l = input()
    debug(f"Description of the field: {l}")
    l = l.split()
    field_height = int(l[1])
    field_width = int(l[2].replace(":", ""))


def parse_field(player: int):
    """
    Parse the field.

    Return field to another function,
    where the logic for choosing the move will be.

    The input may look like this:

        01234567890123456
    000 .................
    001 .................
    002 .................
    003 .................
    004 .................
    005 .................
    006 .................
    007 ..O..............
    008 ..OOO............
    009 .................
    010 .................
    011 .................
    012 ..............X..
    013 .................
    014 .................

    :param player int: Represents whether we're the first or second player
    """
    field = []
    for _ in range(field_height+1):
        l = input()
        debug(f"Field: {l}")
        field.append(list(l[4:].lower()))
    field = field[1:]
    return field


def parse_figure():
    """
    Parse the figure.

    The function parses the height and width of the figure,
    and then returns it.

    The input may look like this:

    Piece 2 2:
    **
    ..
    """
    global figure_height, figure_width
    l = input()
    debug(f"Piece: {l}")
    figure_height = int(l.split()[1])
    figure = []
    for _ in range(figure_height):
        l = input()
        debug(f"Piece: {l}")
        figure.append(list(l))
    return figure


def go(player, field, piece):
    """
    Function to choose where the next figure will be placed.

    Return list with two coordinates.

    :param player int: Represents whether we're the first or second player
    :param field list: Array with each line of the field.
    :param piece list: Array with each line of the figure.
    """
    my_fig = "o" if player == 1 else "x"
    not_my_fig = "x" if player == 1 else "o"
    possible_moves = []
    for row_pos in range(len(field)-len(piece)+1):
        for col_pos in range(len(field[0])-len(piece[0])+1):
            my_counter = 0
            opp_counter = 0
            for f_row in range(len(piece)):
                for f_col in range(len(piece[0])):
                    if piece[f_row][f_col] == "*":
                        if field[row_pos+f_row][col_pos+f_col] == my_fig:
                            my_counter += 1
                        elif field[row_pos+f_row][col_pos+f_col] == not_my_fig:
                            opp_counter += 1
            if my_counter == 1 and opp_counter == 0:
                possible_moves.append([row_pos, col_pos])
    
    if possible_moves != []:
        return choice(possible_moves)
    else:
        return [0,0]


def step(player: int):
    """
    Perform one step of the game.

    :param player int: Represents whether we're the first or second player
    """
    parse_field_info()
    field = parse_field(player)
    piece = parse_figure()
    move = go(player, field, piece)

    return move


def play(player: int):
    """
    Main game loop.

    :param player int: Represents whether we're the first or second player
    """
    while True:
        move = step(player)
        print(*move)


def parse_info_about_player():
    """
    This function parses the info about the player.

    It can look like this:

    $$$ exec p2 : [./player1.py]
    """
    i = input()
    debug(f"Info about the player: {i}")
    return 1 if "p1 :" in i else 2


def main():
    player = parse_info_about_player()
    try:
        play(player)
    except EOFError:
        debug("Oops, seems game is over..")


if __name__ == "__main__":
    main()
