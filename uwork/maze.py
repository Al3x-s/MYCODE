import random
MAZE_SIZE = 10
WALL = "#"
EMPTY = " "
START = "S"
GOAL = "G"
PLAYER = "P"
EXPLORED = "."

def create_empty_maze(size):
    maze = [[EMPTY] * size for _ in range(size)]
    return maze

def add_walls(maze, num_walls):
    for i in range(num_walls):
        x = random.randint(0, MAZE_SIZE - 1)
        y = random.randint(0, MAZE_SIZE - 1)
        maze[x][y] = WALL

def place_player(maze):
    x = random.randint(0, MAZE_SIZE - 1)
    y = random.randint(0, MAZE_SIZE - 1)
    maze[x][y] = PLAYER
    return x, y

def place_goal(maze):
    x = random.randint(0, MAZE_SIZE - 1)
    y = random.randint(0, MAZE_SIZE - 1)
    maze[x][y] = GOAL

def print_maze_and_map(maze, map_maze):
    print("Maze:")
    for row in maze:
        print(" ".join(row))
    print("\nExplored Map:")
    for row in map_maze:
        print(" ".join(row))

def check_goal(maze, x, y):
    return maze[x][y] == GOAL

def play_maze_game():
    maze = create_empty_maze(MAZE_SIZE)
    add_walls(maze, MAZE_SIZE * 2)
    map_maze = create_empty_maze(MAZE_SIZE)
    x, y = place_player(maze)
    place_goal(maze)

    while True:
        map_maze[x][y] = PLAYER
        print_maze_and_map(maze, map_maze)
        move = input("Enter your move (W/A/S/D): ").upper()
        map_maze[x][y] = EXPLORED
        if move == "W":
            if x > 0 and maze[x - 1][y] != WALL:
                x -= 1
        elif move == "A":
            if y > 0 and maze[x][y - 1] != WALL:
                y -= 1
        elif move == "S":
            if x < MAZE_SIZE - 1 and maze[x + 1][y] != WALL:
                x += 1
        elif move == "D":
            if y < MAZE_SIZE - 1 and maze[x][y + 1] != WALL:
                y += 1

        if check_goal(maze, x, y):
            map_maze[x][y] = PLAYER
            print_maze_and_map(maze, map_maze)
            break

play_maze_game()

