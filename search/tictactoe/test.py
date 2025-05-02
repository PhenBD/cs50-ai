from tictactoe import initial_state
from tictactoe import player
from tictactoe import X, O, EMPTY
from tictactoe import actions
from tictactoe import result
from tictactoe import winner
from tictactoe import terminal
from tictactoe import minimax

state = initial_state()

state =    [[O, O, X],
            [X, X, O],
            [O, X, X]]

print(winner(state))