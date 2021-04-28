import numpy as np
import random
import utils

treePositions = []

def generate_tree_position(world):
        randomPosX = random.randint(0, (len(world) - 1))
        randomPosY = random.randint(0, (len(world) - 1))
        tileInWorld = world[randomPosX][randomPosY]

        if(tileInWorld == "P" or tileInWorld == "F"):
            treePositions.append((randomPosX, randomPosY))
        else:
            return generate_tree_position(world)

def generate_foliage(world):
    # we randomly generate points until we land on a forest biome or plains biome
    # then we generate a tree based on probability

    # get 5,000 points representing 2,000 trees (the map is 500 x 500), so rougly 2% of the map is trees
    # water makes up around 50% so most of the land will have trees

    for x in range(0, 5000):
        generate_tree_position(world)

    # now we have a bunch o tree positions,
    # i don't really care if they are close because they render based on one tile
    # and dupilcated don't matter because they will be placed in the world ontop, there will be a tree there
    # anyways now we place a tree character at each point and we can render them in the terminal

    for tree in treePositions:
        world[tree[0]][tree[1]] = "%"

    # foliage is now generated and we render them in terminal