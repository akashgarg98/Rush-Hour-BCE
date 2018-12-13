"""
Module containing Breadth First algorithm which only holds the previous
generation as archive.
"""

from rush import RushHour
from collections import deque


def breadth_first_small_archive(game):
    """ Create queue for all child fields of Rush Hour board, get first in
    first out. Check if next field is not in the parent layer.
    Return number of moves needed to solve the game and number of states checked.

    Keyword arguments:
    game -- RushHour object
    """

    queue = deque()
    moves = 0
    states = 0
    vehicles = list(game.vehicles.values())
    queue.append(vehicles)
    queue.append(moves)
    previous = []
    current = []
    previous.append(game.create_hash_hex(vehicles))

    while not game.won(vehicles):
        vehicles = queue.popleft()
        moves = queue.popleft()
        game.fill_field(vehicles)
        child_fields = game.get_child_fields_whole_step(vehicles)
        moves += 1
        states += 1
        print(moves, states)
        for field in child_fields:
            hash = game.create_hash_hex(field)
            if not hash in previous:
                queue.append(field)
                queue.append(moves)
                current.append(hash)
        previous = current

    return moves, states
