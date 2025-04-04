#!/usr/bin/env python3

import random as ra
import math


def grid_print(grid): #only for testing purposes!
    for line in grid:
        for num in line:
            print(num, end=" ")
        print()


def to_2d_grid(grid):
    complex_grid = []
    index = 0
    grid_size = int(math.sqrt(len(grid)))
    for i in range(grid_size):
        one_line = []
        for j in range(grid_size):
            one_line.append(grid[index])
            index += 1
        complex_grid.append(one_line)
    return complex_grid

def num_of_tents(grid_size, choice):
    min_tent = grid_size + 2
    max_tent = ((grid_size + 1) // 2) ** 2 - (grid_size + 1) // 2 if grid_size % 2 else (grid_size // 2) ** 2 - grid_size // 2
    print("mint: ", min_tent, "maxt: ", max_tent)
    lst = list(range(min_tent, max_tent + 1))
    n = len(lst)
    base_size = n // 3
    remainder = n % 3
    
    sizes = [base_size] * 3
    if remainder == 1:
        sizes[1] += 1  # Középső lista kap egy extra elemet
    elif remainder == 2:
        sizes[1] += 1  # Második lista kap egy extra elemet
        sizes[2] += 1  # Harmadik lista kap egy extra elemet
    
    result = []
    index = 0
    for size in sizes:
        result.append(lst[index:index + size])
        index += size
    
    if choice == 1:
        return ra.choice(result[0])
    elif choice == 2:
        return ra.choice(result[2])
    elif choice == 3:
        return ra.choice(result[1])
    else:
        raise ValueError("A második paraméternek 1, 2 vagy 3-nak kell lennie.")



def place_tents(grid_size, difficulty):
    grid = [0] * grid_size ** 2
    tents_num = num_of_tents(grid_size, difficulty)
    indexes = list(range(grid_size ** 2))
    for i in range(tents_num):
        index = ra.choice(indexes)
        grid[index] = 2
        indexes.remove(index)
        
        if index % grid_size != 0 and index - 1 in indexes: #vele egy sorban, tőle balra
            indexes.remove(index - 1)
        if index % grid_size != grid_size - 1 and index + 1 in indexes: #vele egy sorban, tőle jobbra
            indexes.remove(index + 1)

        if index + grid_size < grid_size ** 2: #alatta
            if index + grid_size in indexes:
                indexes.remove(index + grid_size)
            if index % grid_size != grid_size - 1 and index + grid_size + 1 in indexes:
                indexes.remove(index + grid_size + 1)
            if index % grid_size != 0 and index + grid_size - 1 in indexes:
                indexes.remove(index + grid_size - 1)
        if index >= grid_size: #felette
            if index - grid_size in indexes:
                indexes.remove(index - grid_size)
            if index % grid_size != 0 and index - grid_size - 1 in indexes:
                indexes.remove(index - grid_size - 1)
            if index % grid_size != grid_size - 1 and index - grid_size + 1 in indexes:
                indexes.remove(index - grid_size + 1)

    grid2 = to_2d_grid(grid)
    return grid2

def place_trees(grid):
    for i, place in enumerate(grid[0]): #első sor
        if place == 2:
            rand_places = []
            if i != 0 and grid[0][i - 1] == 0:
                rand_places.append(1)
            if i != len(grid) - 1 and grid[0][i + 1] == 0:
                rand_places.append(2)
            if grid[1][i] == 0:
                rand_places.append(3)
            rand_place = ra.choice(rand_places)
            if rand_place == 1:
                grid[0][i - 1] = 1
            if rand_place == 2:
                grid[0][i + 1] = 1
            if rand_place == 3:
                grid[1][i] = 1
    for i, place in enumerate(grid[-1]): #utolsó sor
        if place == 2:
            rand_places = []
            if i != 0 and grid[-1][i - 1] == 0:
                rand_places.append(1)
            if i != len(grid) - 1 and grid[-1][i + 1] == 0:
                rand_places.append(2)
            if grid[-2][i] == 0:
                rand_places.append(3)
            rand_place = ra.choice(rand_places)
            if rand_place == 1:
                grid[-1][i - 1] = 1
            if rand_place == 2:
                grid[-1][i + 1] = 1
            if rand_place == 3:
                grid[-2][i] = 1
    for i in range(1, len(grid) - 1): #első oszlop
        if grid[i][0] == 2:
            rand_places = []
            if i != 0 and grid[i - 1][0] == 0:
                rand_places.append(1)
            if i != len(grid) - 1 and grid[i + 1][0] == 0:
                rand_places.append(2)
            if grid[i][1] == 0:
                rand_places.append(3)
            rand_place = ra.choice(rand_places)
            if rand_place == 1:
                grid[i - 1][0] = 1
            if rand_place == 2:
                grid[i + 1][0] = 1
            if rand_place == 3:
                grid[i][1] = 1
    for i in range(1, len(grid) - 1): #utolsó oszlop
        if grid[i][-1] == 2:
            rand_places = []
            if i != 0 and grid[i - 1][-1] == 0:
                rand_places.append(1)
            if i != len(grid) - 1 and grid[i + 1][-1] == 0:
                rand_places.append(2)
            if grid[i][-2] == 0:
                rand_places.append(3)
            rand_place = ra.choice(rand_places)
            if rand_place == 1:
                grid[i - 1][-1] = 1
            if rand_place == 2:
                grid[i + 1][-1] = 1
            if rand_place == 3:
                grid[i][-2] = 1
    for i, line in enumerate(grid[1:-1]):       #ésatöbbi
        i += 1
        for j, place in enumerate(line[1:-1]):
            j += 1
            if place == 2:
                rand_places = []
                if grid[i][j - 1] == 0:
                    rand_places.append(1)
                if grid[i][j + 1] == 0:
                    rand_places.append(2)
                if grid[i - 1][j] == 0:
                    rand_places.append(3)
                if grid[i + 1][j] == 0:
                    rand_places.append(4)
                rand_place = ra.choice(rand_places)
                if rand_place == 1:
                    grid[i][j - 1] = 1
                if rand_place == 2:
                    grid[i][j + 1] = 1
                if rand_place == 3:
                    grid[i - 1][j] = 1
                if rand_place == 4:
                    grid[i + 1][j] = 1
    return grid

def generate_tents_grid(difficulty):
    if difficulty == 1:
        grid_size = ra.randrange(7, 9)
    elif difficulty == 2:
        grid_size = ra.choice([8, 10])
    else:
        grid_size = ra.randrange(9, 13) 
    grid = place_tents(grid_size, difficulty)
    grid2 = place_trees(grid)
    return grid2

def check_trees_n_tents_num(grid): #for testing purposes only!
    tents_num = 0
    trees_num = 0
    for line in grid:
        tents_num += line.count(2)
        trees_num += line.count(1)
    print("tents: ", tents_num, " trees: ", trees_num)
    return tents_num == trees_num




if __name__ == '__main__':
    the_grid = generate_tents_grid(3)
    print(check_trees_n_tents_num(the_grid))
    grid_print(the_grid)