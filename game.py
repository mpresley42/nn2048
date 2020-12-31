import numpy as np


class Game:
    def __init__(self):
        self.board_size = 4
        self.board = np.zeros((self.board_size, self.board_size),dtype='int')
        self.score = 0

    def __str__(self):
        return np.array_str(self.board)

    def max_tile(self):
        return np.amax(self.board)

    def add_tile(self):
        empty_tiles = np.argwhere(self.board == 0)
        new_tile_ind = tuple(empty_tiles[np.random.randint(0, empty_tiles.shape[0])])
        two_or_four = np.random.rand()
        if two_or_four < 0.9:
            self.board[new_tile_ind] = 2
        else:
            self.board[new_tile_ind] = 4

    def get_adjacent_tiles(self,tile):
        tile = np.array(tile)
        moves = [np.array([1,0]),np.array([-1,0]),np.array([0,1]),np.array([0,-1])]
        adjacents = []
        for move in moves:
            adj = tile + move
            if np.all(adj>=0) and np.all(adj<self.board_size):
                adjacents.append(tuple(adj))
        return adjacents

    def is_game_over(self):
        # board is full
        if np.count_nonzero(self.board) == self.board_size**2:
            # check for combos
            for i in range(self.board_size):
                for j in range(self.board_size):
                    for adj in self.get_adjacent_tiles((i,j)):
                        if self.board[adj]==self.board[(i,j)]:
                            return False
            return True
        # board is not full
        else:
            return False

    def slide_arr(self, arr, has_combined=None, add_score=0):
        # takes in a 1d array and slides it to the left
        if has_combined is None:
            has_combined = np.zeros_like(arr)
        old_arr = np.copy(arr)
        #add_score = 0

        for i in range(1,len(arr)):
            if arr[i-1]==0:
                arr[i-1] = arr[i]
                arr[i] = 0
            elif arr[i-1]==arr[i] and has_combined[i-1]==0 and has_combined[i]==0:
                arr[i-1] += arr[i]
                arr[i] = 0
                add_score += arr[i-1]
                has_combined[i-1] = 1
            else:
                continue
        if np.array_equal(old_arr,arr):
            return arr, add_score
        else:
            return self.slide_arr(arr,has_combined,add_score)

    def slide_board(self, board, direction):
        old_board = np.copy(board)
        new_board = np.copy(board)

        if direction=='down':
            for col in range(0,self.board_size):
                arr = old_board[:,col][::-1]
                new_arr, add_score = self.slide_arr(arr)
                new_board[:,col] = new_arr[::-1]

        if direction=='up':
            for col in range(0,self.board_size):
                arr = old_board[:, col]
                new_arr, add_score = self.slide_arr(arr)
                new_board[:, col] = new_arr

        if direction=='left':
            for row in range(0,self.board_size):
                arr = old_board[row,:]
                new_arr, add_score = self.slide_arr(arr)
                new_board[row,:] = new_arr

        if direction=='right':
            for row in range(0,self.board_size):
                arr = old_board[row, :][::-1]
                new_arr, add_score = self.slide_arr(arr)
                new_board[row, :] = new_arr[::-1]

        return new_board, add_score

    def iterate_game(self, direction):
        new_board, add_score = self.slide_board(self.board,direction)

        # check if slide was valid
        if np.array_equal(new_board, self.board):
            return
        else:
            self.board = new_board
            self.score += add_score
            self.add_tile()
            return
