import gen_parent
from random import randrange
from random import shuffle


# Генерация лабиринта с использованием алгоритма Алдуса-Бродера
class AldusBroderGen:
    @staticmethod
    def aldus_broder_gen(width, height):
        cells = [gen_parent.cell.Cell(col, row)
                 for row in range(height) for col in range(width)]
        cur_x, cur_y = randrange(width), randrange(height)
        stack = [(cur_x, cur_y)]
        visited = [False] * (width * height)
        visited[cur_x + cur_y * width] = True

        while stack:
            cur_x, cur_y = stack.pop()
            neighbors = [(cur_x, cur_y - 1), (cur_x - 1, cur_y),
                         (cur_x, cur_y + 1), (cur_x + 1, cur_y)]
            shuffle(neighbors)

            for neighbor_x, neighbor_y in neighbors:
                if 0 <= neighbor_x < width and 0 <= neighbor_y < height and not visited[neighbor_x + neighbor_y * width]:
                    gen_parent.GenBase.remove_walls(
                        cells, width, cur_x, cur_y, neighbor_x, neighbor_y)
                    visited[neighbor_x + neighbor_y * width] = True
                    stack.append((neighbor_x, neighbor_y))

        return cells
