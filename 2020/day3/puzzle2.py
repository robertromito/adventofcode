#!/usr/bin/env python3

# . is open, # is tree
# Slope of right 3, down 1
# How many trees are hit?

import math

with open('input') as f:

    lines = f.readlines()
    line_num = len(lines) - 1 
    line_length = len(lines[0]) - 1
    trees_hit = []

    for s in [[1,1], [3,1], [5,1], [7,1], [1,2]]:

        tree_count = 0
        line = 0
        line_position = 0
        right_by = s[0]
        down_by = s[1]

        while line < line_num:
            line += down_by
            if line > line_num:
                continue

            line_position += right_by
            if line_position >= line_length:
                line_position = line_position % line_length
            
            what_we_hit = lines[line][line_position]
           
            if what_we_hit == "#":
                tree_count += 1

        trees_hit.append(tree_count)
        print(f"We hit {tree_count} trees")

print(f"Product of trees hit is {math.prod(trees_hit)}")