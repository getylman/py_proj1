import gen_parent
from random import choice


class DfsGen:
    @staticmethod
    def dfs_gen(width, height):
        cells = [gen_parent.cell.Cell(col, row)
                 for row in range(height) for col in range(width)]
        # list of visited for dfs
        visited = [False] * (width * height)
        # stack
        stack = []

        def get_direction(x_cur, y_cur):
            def check_cell(x_cur, y_cur):
                if x_cur >= 0 and x_cur < width and y_cur >= 0 and y_cur < height:
                    return True
                return False
            neighbors = []
            # top
            if check_cell(x_cur, y_cur - 1) and not visited[x_cur + (y_cur - 1) * width]:
                neighbors.append([x_cur, y_cur - 1].copy())
            # bottom
            if check_cell(x_cur, y_cur + 1) and not visited[x_cur + (y_cur + 1) * width]:
                neighbors.append([x_cur, y_cur + 1].copy())
            # left
            if check_cell(x_cur - 1, y_cur) and not visited[(x_cur - 1) + y_cur * width]:
                neighbors.append([x_cur - 1, y_cur].copy())
            # right
            if check_cell(x_cur + 1, y_cur) and not visited[(x_cur + 1) + y_cur * width]:
                neighbors.append([x_cur + 1, y_cur].copy())
            return choice(neighbors).copy() if neighbors else False
        cur_cell = [0, 0]
        stack.append(cur_cell.copy())
        while stack:
            next_cell = get_direction(cur_cell[0], cur_cell[1])
            if next_cell:
                visited[next_cell[0] + next_cell[1] * width] = True
                gen_parent.GenBase.remove_walls(cells, width, cur_cell[0], cur_cell[1],
                                                next_cell[0], next_cell[1])
                stack.append(next_cell)
                cur_cell = next_cell.copy()
            else:
                cur_cell = stack.pop().copy()

        return cells
