import gen_parent
from random import randrange
from random import shuffle


# Генерация лабиринта с использованием алгоритма Рассела-Болта
class RasselBoltGen:
    @staticmethod
    def ressel_bolt_gen(width, height):
        cells = [gen_parent.cell.Cell(col, row)
                 for row in range(height) for col in range(width)]
        visited = [False] * (width * height)

        def is_valid(visited, width, cur_x, cur_y):
            return 0 <= cur_x < width and 0 <= cur_y < height and not visited[cur_x + cur_y * width]

        cur_x, cur_y = randrange(width), randrange(height)
        stack = [(cur_x, cur_y)]
        visited[cur_x + cur_y * width] = True

        while stack:
            cur_x, cur_y = stack[-1]
            neighbors = [(cur_x, cur_y - 1), (cur_x - 1, cur_y),
                         (cur_x, cur_y + 1), (cur_x + 1, cur_y)]
            shuffle(neighbors)

            for neighbor_x, neighbor_y in neighbors:
                if is_valid(visited, width, neighbor_x, neighbor_y):
                    gen_parent.GenBase.remove_walls(
                        cells, width, cur_x, cur_y, neighbor_x, neighbor_y)
                    visited[neighbor_x + neighbor_y * width] = True
                    stack.append((neighbor_x, neighbor_y))
                    break
            else:
                stack.pop()

        return cells
