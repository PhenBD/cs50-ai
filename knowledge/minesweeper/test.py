from minesweeper import *

board = Minesweeper(3,3,3)
ai = MinesweeperAI(3,3)

count = board.nearby_mines((1,1))

ai.add_knowledge((1,1), count)

print(ai.knowledge[0])

move = ai.make_safe_move()
if move is None:
    move = ai.make_random_move()
    if move is None:
        flags = ai.mines.copy()

print(move)
nearby = board.nearby_mines(move)
ai.add_knowledge(move, nearby)

board.print()