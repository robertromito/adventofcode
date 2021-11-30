#!/usr/bin/env python3

# . is open, # is tree
# Slope of right 3, down 1
# How many trees are hit?

tree_count = 0
with open('input') as f:
    line_position = 0
    line_length = len(f.readline()) - 1
    for l in f:
        
        line_position += 3
        if line_position >= line_length:
            line_position = line_position % line_length
        
        what_we_hit = l[line_position]
        
        print(f"Going down on line position {line_position} we hit {what_we_hit}")
        
        if what_we_hit == "#":
            tree_count += 1

print(f"We hit {tree_count} trees")