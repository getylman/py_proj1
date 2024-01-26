import dfs_gen
import mst_gen
import file_gen
import aldus_broder_gen
import rassel_bolt_gen


class LabyrinthMap:
    def __init__(self, arg1, arg2):
        self._cells = []
        self._height = 0
        self._width = 0
        if arg1 == 1:
            style = arg2[2]
            # styel -> style of creating map
            self._width = arg2[0]
            self._height = arg2[1]
            # our map
            if style == 'dfs':
                self._cells = dfs_gen.DfsGen.dfs_gen(arg2[0], arg2[1])
            if style == 'mst':
                self._cells = mst_gen.MstGen.mst_gen(arg2[0], arg2[1])
            if style == 'aldus_broder':
                self._cells = aldus_broder_gen.AldusBroderGen.aldus_broder_gen(
                    arg2[0], arg2[1])
            if style == 'rassel_bolt':
                self._cells = rassel_bolt_gen.RasselBoltGen.ressel_bolt_gen(
                    arg2[0], arg2[1])
        else:
            self._cells, self._width, self._height = file_gen.FileGen.file_gen(
                arg2)
        self._start = [0, 0]
        self._finish = [self._width - 1, self._height - 1]

    def set_start_point(self, new_start_x, new_start_y):
        self._start = [new_start_x, new_start_y]

    def set_finish_point(self, new_finish_x, new_finish_y):
        self._finish = [new_finish_x, new_finish_y]

    def get_start_point(self):
        return self._start.copy()

    def get_finish_point(self):
        return self._finish.copy()

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_str_map(self):
        map_str = '-' * (2 * self._width + 1) + '\n'
        for i in range(self._height):
            map_str += '|'
            tmp = '|'
            for j in range(self._width):
                if not self._cells[j + i * self._width].get_walls_status()['right'] and j != self._width - 1:
                    map_str += '  '
                else:
                    map_str += ' |'
                if not self._cells[j + i * self._width].get_walls_status()['bottom'] and i != self._height - 1:
                    tmp += ' -'
                else:
                    tmp += '--'
            map_str += '\n' + (tmp if i != self._height -
                               1 else ('-' * (2 * self._width + 1))) + '\n'
        return map_str

    def get_cur_wall_status(self, cur_x, cur_y, direction):
        return self._cells[cur_x + cur_y * self._width].get_walls_status()[direction]

    def get_map_info(self):
        right_walls = []
        bottom_walls = []
        for i in range(self._height):
            right_walls_line = []
            bottom_walls_line = []
            for j in range(self._width):
                right_walls_line.append(
                    self._cells[j + i * self._width].get_walls_status()['right'])
                bottom_walls_line.append(
                    self._cells[j + i * self._width].get_walls_status()['bottom'])
            right_walls.append(right_walls_line.copy())
            bottom_walls.append(bottom_walls_line.copy())
        return right_walls, bottom_walls

    def walker(self):
        start_cell = self._start
        finish_cell = self._finish
        walker_way = [False] * (self._width * self._height)
        visited = [False] * (self._width * self._height)
        cur_cell = start_cell.copy()
        final_path = []
        stack = []

        stack.append(start_cell.copy())
        # visited[start_x + start_y * self._width] = True

        def path_finder(x, y, path, final_path):
            def check_cell(x_cur, y_cur):
                if x_cur >= 0 and x_cur < self._width and y_cur >= 0 and y_cur < self._height:
                    return True
                return False
            if not check_cell(x, y) or visited[x + y * self._width] or len(final_path) > 0:
                return
            visited[x + y * self._width] = True
            if path[len(path) - 1] == finish_cell:
                final_path = path.copy()
                return
            if not self._cells[x + y * self._width].get_walls_status()['top']:
                new_path1 = path.copy()
                new_path1.append([x, y - 1])
                path_finder(x, y - 1, new_path1, final_path)
            if not self._cells[x + y * self._width].get_walls_status()['bottom']:
                new_path2 = path.copy()
                new_path2.append([x, y + 1])
                path_finder(x, y + 1, new_path2, final_path)
            if not self._cells[x + y * self._width].get_walls_status()['left']:
                new_path3 = path.copy()
                new_path3.append([x - 1, y])
                path_finder(x - 1, y, new_path3, final_path)
            if not self._cells[x + y * self._width].get_walls_status()['right']:
                new_path4 = path.copy()
                new_path4.append([x + 1, y])
                path_finder(x + 1, y, new_path4, final_path)

        path_finder(self._start[0], self._start[1], stack, final_path)
        print(len(final_path))

        for i in final_path:
            walker_way[i[0] + i[1] * self._width] = True

        map_str = '-' * (2 * self._width + 1) + '\n'
        for i in range(self._height):
            map_str += '|'
            tmp = '|'
            for j in range(self._width):
                if i == self._start[1] and j == self._start[0]:
                    if not self._cells[j + i * self._width].get_walls_status()['right'] and j != self._width - 1:
                        map_str += ('S*' if walker_way[j +
                                    i * self._width] else 'S ')
                    else:
                        map_str += 'S|'
                elif i == self._finish[1] and j == self._finish[0]:
                    if not self._cells[j + i * self._width].get_walls_status()['right'] and j != self._width - 1:
                        map_str += ('F*' if walker_way[j +
                                    i * self._width] else 'F ')
                    else:
                        map_str += 'F|'
                else:
                    if not self._cells[j + i * self._width].get_walls_status()['right'] and j != self._width - 1:
                        map_str += ('**' if walker_way[j +
                                    i * self._width] else '  ')
                    else:
                        map_str += ' |'
                if not self._cells[j + i * self._width].get_walls_status()['bottom'] and i != self._height - 1:
                    tmp += ('*' if walker_way[j +
                            i * self._width] else ' ') + '-'
                else:
                    tmp += '--'
            map_str += '\n' + (tmp if i != self._height -
                               1 else ('-' * (2 * self._width + 1))) + '\n'

        return map_str
