import random
from typing import Tuple, Callable

def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    global player_ini
    player_ini = state.player

    perfect_move = MAX(state, max_depth, True, eval_func, float('-inf'), float('inf'))[1]
    return perfect_move

def MAX(state, max_depth:int, isMax:bool, eval_func:callable, alpha:float, beta:float):
    if(max_depth == 0) or (state.is_terminal()):
        return eval_func(state, player_ini), None
    v = float('-inf')

    for move in state.legal_moves():
        next_state = state.next_state(move)

        v_new  = MIN(next_state, max_depth - 1, False, eval_func, alpha, beta)[0]
        if v_new > v:
            v = v_new
            best_move = move
        if v >= beta:
            break
        alpha = max(alpha, v)
    return v, best_move

def MIN(state, max_depth:int, isMax:bool, eval_func:callable, alpha:float, beta:float):
    if(max_depth == 0) or (state.is_terminal()):
        return eval_func(state, player_ini), None
    v = float('inf')

    for move in state.legal_moves():
        next_state = state.next_state(move)
        
        v_new  = MAX(next_state, max_depth - 1, True, eval_func, alpha, beta)[0]
        if v_new < v:
            v = v_new
            best_move = move
        if v <= alpha:
            break
        beta = min(beta, v)
    return v, best_move