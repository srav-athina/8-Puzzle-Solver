FINAL_BOARD = ((1,2,3),
              (4,5,6),
              (7,8,0))

# We are running bfs, which needs a queue. 
class Queue:

    def __init__(self):
        self.L = []

    def enqueue(self, val):
        self.L.append(val)

    def dequeue(self):
        return self.L.pop(0)

    def __len__(self):
        return len(self.L)
    
# Each node is a single board state.
# Nodes are connected if one move from the current board gets to the next board

# Run bfs starting from the given node
def bfs(start_board):
    if is_invalid(start_board):
        return None
    visited = set()
    q = Queue()
    # instead of just storing the node, store the path
    q.enqueue([start_board])
    while len(q) != 0:
        # get the path
        path = q.dequeue()
        # get the last node
        n = path[-1]
        if n not in visited:
            visited.add(n)
            # if last node is our goal, return the path
            if is_final(n):
                return path
            for nbr in get_neighbors(n):
                # for each nbr, make a copy of the path and append neighbor
                new_path = path[:]
                new_path.append(nbr)
                q.enqueue(new_path)
    return None

# if a board is invalid, (does not have all numbers from 0-8), return a NULL path
def is_invalid(board):
    numbers = [0 for i in range(9)]
    for i in range(3):
        for j in range(3):
            if board[i][j] <= 8 and  board[i][j] >= 0:
                numbers[board[i][j]] = 1
    return any(i==0 for i in numbers)
                          
# Helper function used to figure out where the space is
def find_space(n):
    zero_row = 0
    zero_col = 0
    for i in range(3):
        for j in range(3):
            if n[i][j] == 0:
                zero_row = i
                zero_col = j
                break
    return zero_row, zero_col

# Returns the list of (upto) 4 neigbors of the current board
# The neighbors are by making 1 of up,down,left,right
def get_neighbors(n):
    neighbors = []
    zero_row, zero_col = find_space(n)

    # move down
    if zero_row > 0:
        m_down = [list(row) for row in n]
        m_down[zero_row][zero_col] = m_down[zero_row - 1][zero_col]
        m_down[zero_row - 1][zero_col] = 0
        neighbors.append(make_tuple(m_down))

    # move up
    if zero_row < 2:
        m_up = [list(row) for row in n]
        m_up[zero_row][zero_col] = m_up[zero_row + 1][zero_col]
        m_up[zero_row + 1][zero_col] = 0
        neighbors.append(make_tuple(m_up))

    # move right
    if zero_col > 0:
        m_right = [list(row) for row in n]
        m_right[zero_row][zero_col] = m_right[zero_row][zero_col - 1]
        m_right[zero_row][zero_col - 1] = 0
        neighbors.append(make_tuple(m_right))

    # move left
    if zero_col < 2:
        m_left = [list(row) for row in n]
        m_left[zero_row][zero_col] = m_left[zero_row][zero_col + 1]
        m_left[zero_row][zero_col + 1] = 0
        neighbors.append(make_tuple(m_left))

    
    return neighbors

# return the string of the board in the correct format
def print_board(b):
    r_str = "******************\n"
    for i in range(3):
        for j in range(3):
            r_str += str(b[i][j])
            r_str += " "
        r_str += "\n"
    r_str += "******************"
    print(r_str)

# helper function that prints correct output given a path
def print_path(path):
    counter = 0
    step_string = "Step {} :"
    for board in path:
        print(step_string.format(counter))
        print_board(board)
        counter += 1

# Returns True if we are at the current board is winning
def is_final(n):
    return n == FINAL_BOARD

#use this function to format the row, col where the space exists as a tuple
def make_tuple(a):
    return tuple(map(tuple, a))
