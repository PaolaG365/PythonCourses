maze_lines = int(input())
maze = []
starting_point = []
steps = 1

for i in range(maze_lines):
    maze_line = [ch for ch in input()]
    if "k" in maze_line:
        starting_point = [i, maze_line.index("k")]
    maze.append(maze_line)


def is_valid_kate_direction(a_maze, index1, index2):
    if a_maze[index1] and 0 <= index2 < len(a_maze[index1]):
        return True
    return False


def find_the_way_out(kates_maze, kate_point, step):

    kate_row, kate_col = kate_point

    if kate_row == len(kates_maze) - 1 and kates_maze[kate_row][kate_col] == "k":
        return f"Kate got out in {step} moves"

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dr, dc in directions:
        new_row, new_col = kate_row + dr, kate_col + dc
        if is_valid_kate_direction(kates_maze, new_row, new_col) and kates_maze[new_row][new_col] not in "k#":
            kates_maze[new_row][new_col] = "k"
            return find_the_way_out(kates_maze, (new_row, new_col), step + 1)

    return "Kate cannot get out"


print(find_the_way_out(maze, starting_point, steps))
