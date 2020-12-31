from game import Game
import numpy as np

SLIDE_DIRS = ('up', 'down', 'left', 'right')
ALT_SLIDE_DIRS = {'u': 'up', 'd': 'down', 'l': 'left', 'r': 'right'}


def user_choice(game):
    print(game)
    direction = input("Enter direction to slide: ")

    # sanitize input
    if direction in SLIDE_DIRS:
        return direction
    elif direction in ALT_SLIDE_DIRS.keys():
        return ALT_SLIDE_DIRS[direction]
    else:
        print('Not a valid entry.')
        direction = user_choice(game)

    return direction


def random_choice(game):
    return SLIDE_DIRS[np.random.randint(0,4)]


def always_down_then_random(game):
    new_board, add_score = game.slide_board(game.board, 'down')
    if np.array_equal(new_board, game.board):
        return SLIDE_DIRS[np.random.randint(0,4)]
    else:
        return 'down'


def maximize_add_score(game):
    best_add_score = 0
    best_direction = 'down'
    for direction in SLIDE_DIRS:
        new_board, add_score = game.slide_board(game.board, direction)
        if add_score >= best_add_score and not np.array_equal(new_board,game.board):
            best_direction = direction
            best_add_score = add_score
    return best_direction


def play_game(choice_func,verbose=False):
    game = Game()
    game.add_tile()

    i = 0
    while True:
        if game.is_game_over():
            break

        direction = choice_func(game)
        game.iterate_game(direction)
        if verbose and i%10==0:
            print(i, game.score, game.board)
        i += 1

    return game.score, game.board


def record_many_games(choice_func,ngames=1000,label=None,dir_name='./'):
    fname = dir_name+label+'game_data.txt'
    f = open(fname,'w')
    for i in range(ngames):
        score, board = play_game(choice_func)
        line = str(score)+' '+str(board.tolist())+'\n'
        f.write(line)
    f.close()


if __name__ == '__main__':
    record_many_games(maximize_add_score,ngames=1000,label='max_add_score_')