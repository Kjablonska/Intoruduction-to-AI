# -------------------------------------------------------------------------------------
#   Imports:
# -------------------------------------------------------------------------------------
from copy import deepcopy
from common_val import BLACK, WHITE

# -------------------------------------------------------------------------------------
#   Implementation of minimax algorithm with alpha beta pruning:
#   board           -   value of the currently evaluated board.
#   depth           -   defined how much turns we want to get checked.
#   is_max_player   -   defines whether we want to maximize or minimize the move.
#   alpha           -   initialized to -infinity, keeps value of the maximum score
#   beta            -   initialized to +infinity, keeps value of the minimum score
#
#   Assumptions:
#   AI plays with white discs and it starts the game.
#
#   Minimax algorithm with alpha beta pruning description:
#   Alorithm is developed to find the result of all possible moves, meaning than for each potential move there is calculated difference between number of black and white moves.
#   In case when we want to maximize the move, the move resulting in the greatest difference (result) needs to be picked. Otherwise, the move resulting in the smallest difference is picked.
#
#   Alpha beta pruning is a way for minimax algorithm optimization.
#   The game tree is evaluated as long as there is a possibility of finding better move. For instance - for miximizing player, knowing that one branch will give better result than the other, there is no need for further evaluation of the "loosing" branch.
#
# -------------------------------------------------------------------------------------


def minimax(board, depth, alpha, beta, is_max_player):
    #   Case: we evaluated all the turns (speicified by depth variable) and no one has won the game yet.
    if board.get_winner() != None or depth == 0:
        return board.calculate_result(), board

    # Maximize the move.
    if is_max_player:
        maximizing_move = None
        max_score = float('-inf')
        moves = _find_possible_moves(board, WHITE)

        #   For each possible move there is a need to calcaulte the result of other player's moves.
        for move in moves:
            # minimax method returns max_score and maximizing_move, we want here only max_score value.
            score = minimax(move, depth-1, alpha, beta, False)[0]

            max_score = max(max_score, score)
            if max_score == score:
                maximizing_move = move

            alpha = max(alpha, max_score)
            if beta <= alpha:  # No need to evaluate more moves since alpha is already greater than beta => current move is selected.
                break

        return max_score, maximizing_move

    # Minimize the move.
    else:
        minimizing_move = None
        min_score = float('inf')
        moves = _find_possible_moves(board, BLACK)

        for move in moves:
            score = minimax(move, depth-1, alpha, beta, True)[0]
            min_score = min(min_score, score)
            if min_score == score:
                minimizing_move = move
            beta = min(beta, min_score)
            if beta <= alpha:  # No need to evaluate more moves.
                break

        return min_score, minimizing_move

# -------------------------------------------------------------------------------------
#   Private methods:
# -------------------------------------------------------------------------------------

def _find_possible_moves(board, color):
    possible_moves = []
    discs = board.get_discs_by_color(color)
    final_discs = []

    for disc in discs:
        valid_moves = board.get_possible_moves(disc)

        final_moves = {}
        for move in valid_moves:
            if len(valid_moves[move]) != 0:
                final_moves[move] = valid_moves[move]
                final_discs.append(disc)

        if len(final_moves) != 0:
            valid_moves = final_moves.copy()

    if len(final_discs) != 0:
        discs = final_discs

    for disc in discs:
        valid_moves = board.get_possible_moves(disc)

        # items consists of positon (row, col) and disc. This indicates that if we move the disc to the given position, we will jump over the given disc.
        for move, jumped_over in valid_moves.items():

            # Deepcopy allows for copying content of the object without the reference to it.
            board_copy = deepcopy(board)
            disc_copy = board_copy.get_disc(disc.row, disc.col)

            # Takes disc, move and deepcopy of the board.
            # Make move and returns the resulting board.
            new_board = _make_move(disc_copy, move[0], move[1], board_copy, jumped_over)
            possible_moves.append(new_board)

    return possible_moves


def _make_move(disc, row, col, board, skipped):
    board.make_move(disc, row, col)

    if skipped:    # If in this move we jumped over any disc, we need to remove it from the board.
        board.delete_jumped_over(skipped)

    return board
