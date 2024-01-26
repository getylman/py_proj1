import gen_parent
from random import choice
from random import randint


class MstGen:
    @staticmethod
    def mst_gen(width, height):
        cells = [gen_parent.cell.Cell(col, row)
                 for row in range(height) for col in range(width)]
        # using Prim algorithm
        # list of visited
        visited = [False] * (width * height)
        start_id = choice(range(width * height))
        cur_cell = [cells[start_id].x, cells[start_id].y]
        visited[start_id] = True
        neighbors = []

        def get_neighbors(x_cur, y_cur):
            def check_cell(x_cur, y_cur):
                if x_cur >= 0 and x_cur < width and y_cur >= 0 and y_cur < height:
                    return True
                return False
            # top
            if check_cell(x_cur, y_cur - 1) and not visited[x_cur + (y_cur - 1) * width]:
                neighbors.append(
                    [[x_cur, y_cur - 1], [x_cur, y_cur]].copy())
            # bottom
            if check_cell(x_cur, y_cur + 1) and not visited[x_cur + (y_cur + 1) * width]:
                neighbors.append(
                    [[x_cur, y_cur + 1], [x_cur, y_cur]].copy())
            # left
            if check_cell(x_cur - 1, y_cur) and not visited[(x_cur - 1) + y_cur * width]:
                neighbors.append(
                    [[x_cur - 1, y_cur], [x_cur, y_cur]].copy())
            # right
            if check_cell(x_cur + 1, y_cur) and not visited[(x_cur + 1) + y_cur * width]:
                neighbors.append(
                    [[x_cur + 1, y_cur], [x_cur, y_cur]].copy())
        get_neighbors(cur_cell[0], cur_cell[1])
        while neighbors:
            # getting a random neighbor index
            index = randint(0, len(neighbors) - 1)
            # current not merged neigbor
            next_cell = [neighbors[index][0][0], neighbors[index][0][1]]
            # merged neighbor of did not merged
            cur_cell = [neighbors[index][1][0], neighbors[index][1][1]]
            # remove it from list
            del neighbors[index]
            # if we visited this neighbor we skip it
            if visited[next_cell[0] + next_cell[1] * width]:
                continue
            # remove wall to merge neihbor
            gen_parent.GenBase.remove_walls(cells, width, cur_cell[0], cur_cell[1],
                                            next_cell[0], next_cell[1])
            # mark as visited
            visited[next_cell[0] + next_cell[1] * width] = True
            # push new neigbours from new merged
            get_neighbors(next_cell[0], next_cell[1])

        return cells
