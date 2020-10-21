import numpy as np
import copy
from random import randint
import random

num_of_node_explored = 0

def take_move(old_board, move, turn):
    '''
    move is a triple (x, y, direction)
    '''
    new_board = copy.deepcopy(old_board)
    x = move[0]
    y = move[1]
    direction = move[2]
    stones = old_board[x][y]*turn
    new_board[x][y] = 0

    if direction == 1:
        for i in range(3):
            if i == 0:
                new_board[x+1+i][y] = new_board[x+1+i][y] + 1*turn
                stones = stones - 1
            elif i == 1:
                if stones >= 2:
                    new_board[x+1+i][y] = new_board[x+1+i][y] + 2*turn
                    stones = stones - 2
                else:
                    new_board[x+1+i][y] = new_board[x+1+i][y] + stones*turn
                    stones = 0
            elif i == 2:
                new_board[x+1+i][y] = new_board[x+1+i][y] + stones*turn
                stones = 0
            if x+1+i+1 > 3 or new_board[x+1+i+1][y]*turn < 0 or stones == 0:
                new_board[x+1+i][y] = new_board[x+1+i][y] + stones*turn
                break
    elif direction == 2:
        for i in range(3):
            if i == 0:
                new_board[x-1-i][y] = new_board[x-1-i][y] + 1*turn
                stones = stones - 1
            elif i == 1:
                if stones >= 2: 
                    new_board[x-1-i][y] = new_board[x-1-i][y] + 2*turn
                    stones = stones - 2
                else:
                    new_board[x-1-i][y] = new_board[x-1-i][y] + stones*turn
                    stones = 0
            elif i == 2:
                new_board[x-1-i][y] = new_board[x-1-i][y] + stones*turn
                stones = 0
            if x-1-i-1 < 0 or new_board[x-1-i-1][y]*turn < 0 or stones == 0:
                new_board[x-1-i][y] = new_board[x-1-i][y] + stones*turn
                break
    elif direction == 3:
        for i in range(3):
            if i == 0:
                new_board[x][y+1+i] = new_board[x][y+1+i] + 1*turn
                stones = stones - 1
            elif i == 1: 
                if stones >= 2:
                    new_board[x][y+1+i] = new_board[x][y+1+i] + 2*turn
                    stones = stones - 2
                else:
                    new_board[x][y+1+i] = new_board[x][y+1+i] + stones*turn
                    stones = 0
            elif i == 2:
                new_board[x][y+1+i] = new_board[x][y+1+i] + stones*turn
                stones = 0
            if y+1+i+1 > 3 or new_board[x][y+1+i+1]*turn < 0 or stones == 0:
                new_board[x][y+1+i] = new_board[x][y+1+i] + stones*turn # rest of the stone
                break
    elif direction == 4:
        for i in range(3):
            if i == 0:
                new_board[x][y-1-i] = new_board[x][y-1-i] + 1*turn
                stones = stones - 1
            elif i == 1: 
                if stones >= 2:
                    new_board[x][y-1-i] = new_board[x][y-1-i] + 2*turn
                    stones = stones - 2
                else:
                    new_board[x][y-1-i] = new_board[x][y-1-i] + stones*turn
                    stones = 0
            elif i == 2:
                new_board[x][y-1-i] = new_board[x][y-1-i] + stones*turn
                stones = 0
            if y-1-i-1 < 0 or new_board[x][y-1-i-1]*turn < 0 or stones == 0:
                new_board[x][y-1-i] = new_board[x][y-1-i] + stones*turn
                break
    elif direction == 5:
        for i in range(3):
            if i == 0:
                new_board[x+1+i][y+1+i] = new_board[x+1+i][y+1+i] + 1*turn
                stones = stones - 1
            elif i == 1: 
                if stones >= 2:
                    new_board[x+1+i][y+1+i] = new_board[x+1+i][y+1+i] + 2*turn
                    stones = stones - 2
                else:
                    new_board[x+1+i][y+1+i] = new_board[x+1+i][y+1+i] + stones*turn
                    stones = 0
            elif i == 2:
                new_board[x+1+i][y+1+i] = new_board[x+1+i][y+1+i] + stones*turn
                stones = 0
            if x+1+i+1 > 3 or y+1+i+1 > 3 or new_board[x+1+i+1][y+1+i+1]*turn < 0 or stones == 0:
                new_board[x+1+i][y+1+i] = new_board[x+1+i][y+1+i] + stones*turn
                break
    elif direction == 6:
        for i in range(3):
            if i == 0:
                new_board[x+1+i][y-1-i] = new_board[x+1+i][y-1-i] + 1*turn
                stones = stones - 1
            elif i == 1: 
                if stones >= 2:
                    new_board[x+1+i][y-1-i] = new_board[x+1+i][y-1-i] + 2*turn
                    stones = stones - 2
                else:
                    new_board[x+1+i][y-1-i] = new_board[x+1+i][y-1-i] + stones*turn
                    stones = 0
            elif i == 2:
                new_board[x+1+i][y-1-i] = new_board[x+1+i][y-1-i] + stones*turn
                stones = 0
            if x+1+i+1 > 3 or y-1-i-1 < 0 or new_board[x+1+i+1][y-1-i-1]*turn < 0 or stones == 0:
                new_board[x+1+i][y-1-i] = new_board[x+1+i][y-1-i] + stones*turn
                break
    elif direction == 7:
        for i in range(3):
            if i == 0:
                new_board[x-1-i][y+1+i] = new_board[x-1-i][y+1+i] + 1*turn
                stones = stones - 1
            elif i == 1: 
                if stones >= 2:
                    new_board[x-1-i][y+1+i] = new_board[x-1-i][y+1+i] + 2*turn
                    stones = stones - 2
                else:
                    new_board[x-1-i][y+1+i] = new_board[x-1-i][y+1+i] + stones*turn
                    stones = 0
            elif i == 2:
                new_board[x-1-i][y+1+i] = new_board[x-1-i][y+1+i] + stones*turn
                stones = 0
            if x-1-i-1 < 0 or y+1+i+1 > 3 or new_board[x-1-i-1][y+1+i+1]*turn < 0 or stones == 0:
                new_board[x-1-i][y+1+i] = new_board[x-1-i][y+1+i] + stones*turn
                break
    elif direction == 8:
        for i in range(3):
            if i == 0:
                new_board[x-1-i][y-1-i] = new_board[x-1-i][y-1-i] + 1*turn
                stones = stones - 1
            elif i == 1: 
                if stones >= 2:
                    new_board[x-1-i][y-1-i] = new_board[x-1-i][y-1-i] + 2*turn
                    stones = stones - 2
                else:
                    new_board[x-1-i][y-1-i] = new_board[x-1-i][y-1-i] + stones*turn
                    stones = 0
            elif i == 2:
                new_board[x-1-i][y-1-i] = new_board[x-1-i][y-1-i] + stones*turn
                stones = 0
            if x-1-i-1 < 0 or y-1-i-1 < 0 or new_board[x-1-i-1][y-1-i-1]*turn < 0 or stones == 0:
                new_board[x-1-i][y-1-i] = new_board[x-1-i][y-1-i] + stones*turn
                break

    return new_board

class Node:
    def __init__(self, board, turn, depth, parent_move_index, parent=None):
        self.board = copy.deepcopy(board)
        self.moves = [] # only store player moves
        self.player_moves = 0
        self.opponent_moves = 0
        self.evaluation_value = 0
        self.turn = turn # if turn is +1, it's white turn, if turn is -1, it's black turn
        self.child_list = []
        self.lw = -np.inf
        self.hi = np.inf
        self.parent = parent
        self.depth = depth
        self.parent_move_index = parent_move_index
        self.optimal_move_index = -1
        self.player_occupied = 0
        self.opponent_occupied = 0

    def print_board(self):
        for i in [3,2,1,0]:
            print(str(self.board[0][i]) + " " + str(self.board[1][i]) + " " + str(self.board[2][i]) + " " + str(self.board[3][i]))
        print("################")

    def get_random_move(self):
        return self.moves[randint(0,len(self.moves)-1)]

    def get_random_move_index(self):
        return randint(0,len(self.moves)-1)
    
    def get_moves(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j]*self.turn > 0: # occupied by the player
                    self.player_occupied = self.player_occupied + 1
                    self.calculate_available_player_moves((i,j))
        random.shuffle(self.moves)
        self.child_list = [None]*len(self.moves)

    def get_opponent_moves(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j]*self.turn < 0: # occupied by the opponent
                    self.opponent_occupied = self.opponent_occupied + 1
                    # self.calculate_available_opponent_moves((i,j))
    
    def update_bounds(self, max_depth):
        global num_of_node_explored
        if self.depth == max_depth:
            self.get_opponent_moves()
            if self.depth%2 == 1:
                # min
                # self.evaluation_value = self.opponent_moves - self.player_moves
                self.evaluation_value = self.opponent_occupied - self.player_occupied
                if self.evaluation_value > self.parent.lw:
                    # update parent lower bound
                    self.parent.lw = self.evaluation_value
                    self.parent.optimal_move_index = self.parent_move_index
            else:
                # max
                # self.evaluation_value = self.player_moves - self.opponent_moves
                self.evaluation_value = self.player_occupied - self.opponent_occupied
                if self.parent.hi > self.evaluation_value:
                    # update upper bound of parent node
                    self.parent.hi = self.evaluation_value
                    self.parent.optimal_move_index = self.parent_move_index

        elif len(self.moves) == 0:
            # terminating state!
            if self.depth%2 == 1:
                # smart agent winning
                self.evaluation_value = np.inf
                if self.evaluation_value > self.parent.lw:
                    # update parent lower bound
                    self.parent.lw = self.evaluation_value
                    self.parent.optimal_move_index = self.parent_move_index
            else:
                # random agent winning
                self.evaluation_value = -np.inf
                if self.parent.hi > self.evaluation_value:
                    # update upper bound of parent node
                    self.parent.hi = self.evaluation_value
                    self.parent.optimal_move_index = self.parent_move_index
        else:
            # expand
            for i in range(len(self.moves)):
                self.child_list[i] = Node(
                            take_move(self.board,self.moves[i],self.turn),
                            -self.turn,
                             self.depth+1,
                             i, # parent move index
                             self
                            )
                num_of_node_explored = num_of_node_explored + 1
                self.child_list[i].get_moves()
                self.child_list[i].update_bounds(max_depth)
                if self.parent is not None:
                    if self.depth%2 == 1:
                        # min node
                        if self.hi > self.parent.lw:
                            # update parent lower bound
                            self.parent.lw = self.hi
                            self.parent.optimal_move_index = self.parent_move_index
                        else:
                            # no need to further update
                            break
                    else:
                        # max node
                        if self.parent.hi > self.lw:
                            # update upper bound of parent node
                            self.parent.hi = self.lw
                            self.parent.optimal_move_index = self.parent_move_index
                        else:
                            break
        return

    def search_optimal_move_index(self,max_depth):
        self.update_bounds(max_depth)
        return self.optimal_move_index


    def evaluate(self):
        for i in range(4):
            for j in range(4):
                if self.board[i][j]*self.turn > 0: # occupied by the player
                    self.calculate_available_player_moves((i,j))
                elif self.board[i][j]*self.turn < 0: # occupied by the opponent
                    self.calculate_available_opponent_moves((i,j))
        self.evaluation_value = self.player_moves - self.opponent_moves

    def calculate_available_player_moves(self, pos):
        '''
        if color is positive, then pos is occupied by white stones, otherwise it is occupied by black stones
        '''
        x = pos[0]
        y = pos[1]
        if x + 1 <= 3 and self.board[x+1][y]*self.turn >= 0:
            # direction 1
            self.player_moves = self.player_moves + 1
            self.moves.append((x, y, 1))
        if x - 1 >= 0 and self.board[x-1][y]*self.turn >= 0:
            # direction 2
            self.player_moves = self.player_moves + 1
            self.moves.append((x, y, 2))
        if y + 1 <= 3 and self.board[x][y+1]*self.turn >= 0:
            # direction 3
            self.player_moves = self.player_moves + 1
            self.moves.append((x, y, 3))
        if y - 1 >= 0 and self.board[x][y-1]*self.turn >= 0:
            # direction 4
            self.player_moves = self.player_moves + 1
            self.moves.append((x, y, 4))
        if x + 1 <= 3 and y + 1 <= 3 and self.board[x+1][y+1]*self.turn >= 0:
            # direction 5
            self.player_moves = self.player_moves + 1
            self.moves.append((x, y, 5))
        if x + 1 <= 3 and y - 1 >= 0 and self.board[x+1][y-1]*self.turn >= 0:
            # direction 6
            self.player_moves = self.player_moves + 1
            self.moves.append((x, y, 6))
        if x - 1 >= 0 and y + 1 <= 3 and self.board[x-1][y+1]*self.turn >= 0:
            # direction 7
            self.player_moves = self.player_moves + 1
            self.moves.append((x, y, 7))
        if x - 1 >= 0 and y - 1 >= 0 and self.board[x-1][y-1]*self.turn >= 0:
            # direction 6
            self.player_moves = self.player_moves + 1
            self.moves.append((x, y, 8))

    def calculate_available_opponent_moves(self, pos):
        '''
        if color is positive, then pos is occupied by white stones, otherwise it is occupied by black stones
        '''
        x = pos[0]
        y = pos[1]
        if x + 1 <= 3 and self.board[x+1][y]*self.turn >= 0:
            self.opponent_moves = self.opponent_moves + 1
        if x - 1 >= 0 and self.board[x-1][y]*self.turn >= 0:
            self.opponent_moves = self.opponent_moves + 1
        if y + 1 <= 3 and self.board[x][y+1]*self.turn >= 0:
            self.opponent_moves = self.opponent_moves + 1
        if y - 1 >= 0 and self.board[x][y-1]*self.turn >= 0:
            self.opponent_moves = self.opponent_moves + 1
        if x + 1 <= 3 and y + 1 <= 3 and self.board[x+1][y+1]*self.turn >= 0:
            self.opponent_moves = self.opponent_moves + 1
        if x + 1 <= 3 and y - 1 >= 0 and self.board[x+1][y-1]*self.turn >= 0:
            self.opponent_moves = self.opponent_moves + 1
        if x - 1 >= 0 and y + 1 <= 3 and self.board[x-1][y+1]*self.turn >= 0:
            self.opponent_moves = self.opponent_moves + 1
        if x - 1 >= 0 and y - 1 >= 0 and self.board[x-1][y-1]*self.turn >= 0:
            self.opponent_moves = self.opponent_moves + 1


if __name__ == "__main__":
    board = [[0 for x in range(4)] for y in range(4)]
    board[0][3] = -10 # black
    board[3][0] = 10 # white

    stop = False
    win = False
    start_node = Node(board,-1, 0, -1)
    start_node.get_moves()

    depth_limit = 2
    max_depth  = depth_limit
    # we assume black moves first
    turn_count = 0

    while True:
        start_node.print_board()
        print("start node depth: {}".format(start_node.depth))
        if len(start_node.moves) == 0:
            # the random agent won!
            print("random agent won!")
            print("total depth of the tree: {}".format(max_depth-2))
            win = False
            break
        player_move_index = start_node.search_optimal_move_index(max_depth)
        turn_count = turn_count + 1
        destination_node = start_node.child_list[player_move_index] # we must have created destination node before
        destination_node.print_board()
        if len(destination_node.moves) == 0:
            # we won!
            print("we won!")
            print("total depth of the tree: {}".format(max_depth))
            win = True
            break
        else: 
            opponent_move_index = destination_node.get_random_move_index()
            turn_count = turn_count + 1
            if destination_node.child_list[opponent_move_index] is None:
                # we have not created this node
                start_node = Node(
                    take_move(destination_node.board,destination_node.moves[opponent_move_index],destination_node.turn),
                    -destination_node.turn,
                    destination_node.depth+1,
                    -1
                )
                start_node.get_moves()
            else:
                # we have created this node
                start_node = destination_node.child_list[opponent_move_index]
                start_node.parent = None # clear old tree
            max_depth = max_depth + 2
    
    print("turn count: {}".format(turn_count))
    print("num of nodes explored: {}".format(num_of_node_explored))
    print("depth explored each time: {}".format(depth_limit))

