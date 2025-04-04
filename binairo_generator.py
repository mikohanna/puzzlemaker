import numpy as np
import random

def is_valid_placement(grid, row, col, num, size):
    """Check if placing num in grid[row][col] is valid."""
    # Check if there are three consecutive numbers in the row
    if col >= 2 and grid[row, col-1] == grid[row, col-2] == num:
        return False
    if col >= 1 and col < size-1 and grid[row, col-1] == grid[row, col+1] == num:
        return False
    if col < size-2 and grid[row, col+1] == grid[row, col+2] == num:
        return False

    # Check if there are three consecutive numbers in the column
    if row >= 2 and grid[row-1, col] == grid[row-2, col] == num:
        return False
    if row >= 1 and row < size-1 and grid[row-1, col] == grid[row+1, col] == num:
        return False
    if row < size-2 and grid[row+1, col] == grid[row+2, col] == num:
        return False

    return True

def generate_filled_grid(size):
    """Generate a valid binary puzzle grid of a given size."""
    grid = np.full((size, size), 2)  # Initialize with 2s
    half_size = size // 2

    def backtrack(row, col):
        if row == size:
            return True
        
        next_row, next_col = (row, col + 1) if col + 1 < size else (row + 1, 0)
        
        # Try placing 0 and 1, ensuring balanced row and column counts
        for num in random.sample([0, 1], 2):
            row_count = np.count_nonzero(grid[row, :] == num)
            col_count = np.count_nonzero(grid[:, col] == num)

            if row_count < half_size and col_count < half_size and is_valid_placement(grid, row, col, num, size):
                grid[row, col] = num
                if backtrack(next_row, next_col):
                    return True
                grid[row, col] = 2  # Backtrack
        
        return False

    backtrack(0, 0)
    return grid


def pretty_print(the_list): # for testing purposes
    print("-"*80)
    for line in the_list:
        for n in line:
            if n == 2:
                print("-", end="")
            else:
                print(n, end="")
        print()


def simple_rules(puzzle):
    solving = np.copy(puzzle)
    is_changed = True
    counter = 0
    while is_changed:
        is_changed = False
        for i, line in enumerate(solving):
            for j, n in enumerate(line):
                if j + 2 < len(line):
                    #duo rule
                    if np.array_equal(line[j : j+3], [0, 0, 2]):
                        solving[i, j + 2] = 1
                        is_changed = True
                    if np.array_equal(line[j : j+3], [1, 1, 2]):
                        solving[i, j + 2] = 0
                        is_changed = True
                    if np.array_equal(line[j : j+3], [2, 0, 0]):
                        solving[i, j] = 1
                        is_changed = True
                    if np.array_equal(line[j : j+3], [2, 1, 1]):
                        solving[i, j] = 0 
                        is_changed = True                   
                    # trio rule rows
                    if np.array_equal(line[j : j+3], [0, 2, 0]):
                        solving[i, j+1] = 1
                        is_changed = True
                    if np.array_equal(line[j : j+3], [1, 2, 1]):
                        solving[i, j+1] = 0
                        is_changed = True
            #max element number rule
            if np.count_nonzero(line == 1) == len(line) // 2 and np.count_nonzero(line == 2) > 0:
                solving[i] = [0 if x == 2 else x for x in line]
                is_changed = True
            if np.count_nonzero(line == 0) == len(line) // 2 and np.count_nonzero(line == 2) > 0:
                solving[i] = [1 if x == 2 else x for x in line]
                is_changed = True

        counter += 1
    return (solving, counter != 1)

def harder_rule(puzzle):
    solving = np.copy(puzzle)
    is_changed = True
    counter = 0
    while is_changed:
        is_changed = False
        for i, line in enumerate(solving):
            if (np.count_nonzero(line == 1) == len(line) // 2 - 1 and 
                np.count_nonzero(line == 0) < len(line) // 2 - 1):
                for z, _ in enumerate(line):
                    if solving[i, z] == 2:
                        for k, _ in enumerate(line[:-2]):
                            if k != z and k+1 != z and k+2 != z and (
                                np.array_equal(line[k:k+3], [2, 2, 2]) or
                                np.array_equal(line[k:k+3], [0, 2, 2]) or 
                                np.array_equal(line[k:k+3], [2, 2, 0])):
                                solving[i, z] = 0
                                is_changed = True
            elif (np.count_nonzero(line == 0) == len(line) // 2 - 1 and 
                np.count_nonzero(line == 1) < len(line) // 2 - 1):
                for w, n in enumerate(line):
                    if solving[i, w] == 2:
                        for k, n in enumerate(line[:-2]):
                            
                            if k != w and k+1 != w and k+2 != w and (
                                np.array_equal(line[k:k+3], [2, 2, 2]) or
                                np.array_equal(line[k:k+3], [1, 2, 2]) or 
                                np.array_equal(line[k:k+3], [2, 2, 1])):
                                solving[i, w] = 1
                                is_changed = True
        counter += 1
    return (solving, counter != 1)


def remove_elements(grid):
    for i, line in enumerate(grid):
        for j, _ in enumerate(line[:-2]):
            if (np.array_equal(line[j:j+3], [1, 0, 0]) or
                np.array_equal(line[j:j+3], [0, 1, 1])):
                grid[i][j] = 2
            if (np.array_equal(line[j:j+3], [1, 0, 1]) or
                np.array_equal(line[j:j+3], [0, 1, 0])):
                grid[i][j+1] = 2
            if (np.array_equal(line[j:j+3], [0, 0, 1]) or
                np.array_equal(line[j:j+3], [1, 1, 0])):
                grid[i][j+2] = 2
    return grid


def solve_grid(puzzle, difficulty):
    sol = np.array(puzzle)
    is_changed = [True] * 4
    harder_rule_used = 0
    while any(is_changed):
        sol, is_changed[0] = simple_rules(sol)
        sol, is_changed[1] = simple_rules(sol.T)
        if is_changed[0] or is_changed[1]:
            continue
        if difficulty == 3 or difficulty == 2 and harder_rule_used < 3:
            sol, is_changed[2] = harder_rule(sol)
            if is_changed[2]:
                harder_rule_used += 1
                continue
            sol, is_changed[3] = harder_rule(sol.T)
            if is_changed[3]:
                harder_rule_used += 1
        else:
            is_changed[2], is_changed[3] = False, False
    if not is_grid_solved(sol):
        return -1
    return (sol, harder_rule_used)

def is_grid_solved(grid):
    """Check if the puzzle is fully solved (i.e., contains only 0s and 1s)."""
    for row in grid:
        if 2 in row:
            return False
    return True

def set_size(difficulty):
    if difficulty == 1:
        return 8
    if difficulty == 2:
        return 10
    return 12

def collect_non_empty(matrix):
    indices = np.flatnonzero(matrix != 2)  # nem üres mezők indexei sorfolytonosan
    return indices.tolist()

#difficulty: 1 = easy, 2 = medium, 3 = hard
def generate_binairo_puzzle(difficulty=1):
    size = set_size(difficulty)
    filled = generate_filled_grid(size)
    
    puzzle = remove_elements(filled.copy())
    puzzle = remove_elements(puzzle.copy().T).T

    if difficulty == 1:
        return {'solution': filled, 'puzzle': puzzle}

    for row in range(size):
        for col in range(size):
            if puzzle[row, col] != 2:  # Find a non-2 value
                original_value = puzzle[row, col]
                puzzle[row, col] = 2  # Temporarily change it to 2
                
                # Try solving the puzzle with the updated grid
                solved = solve_grid(puzzle.copy(), difficulty)
                
                # Check if the grid is fully solved
                if solved != -1:
                    # If it remains solvable, keep it as 2
                    continue
                else:
                    # If not solvable, revert back to the original value
                    puzzle[row, col] = original_value
    return {'solution': filled, 'puzzle': puzzle}

