import gen_parent


class FileGen:
    @staticmethod
    def file_gen(file_name):
        file = ''
        try:
            file = open(file_name, "r")
        except Exception:
            raise
        content = file.read()
        file.close()
        lines = []
        tmp_str = ''
        for i in content:
            if i == '\n':
                lines.append(tmp_str)
                tmp_str = ''
                continue
            tmp_str += i
        height = len(lines) // 2
        width = len(lines[0]) // 2

        cells = [gen_parent.cell.Cell(col, row)
                 for row in range(height) for col in range(width)]
        for i in range(1, len(lines), 2):
            for j in range(1, len(lines[i]), 2):
                if lines[i][j + 1] == ' ':
                    gen_parent.GenBase.remove_walls(cells, width,
                                                    j // 2, i // 2, j // 2 + 1, i // 2)
                if lines[i + 1][j] == ' ':
                    gen_parent.GenBase.remove_walls(cells, width,
                                                    j // 2, i // 2, j // 2, i // 2 + 1)
        return cells, width, height
