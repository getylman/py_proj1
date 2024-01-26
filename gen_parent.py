import cell


class GenBase:
    @staticmethod
    def remove_walls(cells, width, cur_x, cur_y, neighbor_x, neighbor_y):
        dx = cur_x - neighbor_x
        dy = cur_y - neighbor_y
        if dx == 1:
            cells[cur_x + cur_y * width].brake_wall('left')
            cells[neighbor_x + neighbor_y *
                  width].brake_wall('right')
        if dx == -1:
            cells[cur_x + cur_y * width].brake_wall('right')
            cells[neighbor_x + neighbor_y *
                  width].brake_wall('left')
        if dy == 1:
            cells[cur_x + cur_y * width].brake_wall('top')
            cells[neighbor_x + neighbor_y *
                  width].brake_wall('bottom')
        if dy == -1:
            cells[cur_x + cur_y * width].brake_wall('bottom')
            cells[neighbor_x + neighbor_y *
                  width].brake_wall('top')
