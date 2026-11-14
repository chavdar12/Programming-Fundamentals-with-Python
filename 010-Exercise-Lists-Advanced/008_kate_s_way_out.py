def find_kate():
    for r in range(len(initial_maze)):
        for c in range(len(initial_maze[r])):
            if initial_maze[r][c] == "k":
                return [r, c]


def moves_count(x, y):
    # longest simple path from (x, y) to outside the maze, None if there is no way out
    if maze[x][y] == 2:
        return 0
    if maze[x][y] != 1 or visited[x][y]:
        return None

    visited[x][y] = True
    paths = [moves_count(x + dx, y + dy) for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1))]
    visited[x][y] = False
    paths = [p for p in paths if p is not None]
    return max(paths) + 1 if paths else None


initial_maze = [list(f"#{input()}#") for _ in range(int(input()))]
maze = [[1 if initial_maze[r][c] == " " else 0 for c in range(len(initial_maze[0]))] for r in range(len(initial_maze))]
maze.append([2 for _ in range(len(initial_maze[0]))])
maze.insert(0, [2 for _ in range(len(initial_maze[0]))])
for i in range(len(maze)):
    maze[i][0] = 2
    maze[i][-1] = 2

visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
x1, y1 = find_kate()
maze[x1 + 1][y1] = 1
moves = moves_count(x1 + 1, y1)
if moves is None:
    print(f"Kate cannot get out")
else:
    print(f"Kate got out in {moves} moves")
