import labyrinth_map
import tkinter as tk


class LabyrinthUser:
    def __init__(self):
        pass

    # executing program
    def execute_program(self):
        self._starter()

    def _main_menu(self):
        # create window and print a labyrinth
        def print_button_pressed():
            self._print_labyrinth_in_window()

        # save labyrinth into file
        def save_button_pressed():
            self._save_labyrinth()

        def rebuild_button_pressed():
            self._labyrinth_bilder()

        def run_button_pressed():
            self._trevel_runner()

        def exit_button_pressed():
            cur_win.destroy()

        cur_win = tk.Tk()
        cur_win.title('')
        label_option = tk.Label(
            cur_win, text='This is main menu.\n'
            + 'Here you can choose activity by pressing a button.\n'
            + '\'Print\' - printing the labyrinth\n'
            + '\'Save\' - save a labyrinth into a file\n'
            + '\'Rebuild\' - rebuild the labyrinth\n'
            + '\'Run the labyrinth\' - try to run labyrinth (have an opportunity run with friend)\n'
            + '\'Exit\' - end this program')
        label_option.pack()
        print_button = tk.Button(
            cur_win, text="Print", command=print_button_pressed)
        print_button.pack()

        save_button = tk.Button(
            cur_win, text="Save", command=save_button_pressed)
        save_button.pack()

        rebuild_button = tk.Button(
            cur_win, text="Rebuild", command=rebuild_button_pressed)
        rebuild_button.pack()

        run_button = tk.Button(
            cur_win, text="Run the labyrinth", command=run_button_pressed)
        run_button.pack()

        exit_button = tk.Button(
            cur_win, text="Exit", command=exit_button_pressed)
        exit_button.pack()

        cur_win.mainloop()

    def _starter(self):
        def select_option():
            cur_win.destroy()
            self._labyrinth_bilder()
            self._main_menu()

        cur_win = tk.Tk()
        cur_win.title('')
        label_option = tk.Label(
            cur_win, text='Hello, this is labyrinth generator.\n'
            + 'I have many abilities, but firstly let\'s create labyrinth.\n'
            + 'Please, press botton \'Start\' to start a process.')
        label_option.pack()

        submit_button = tk.Button(
            cur_win, text="Start", command=select_option)
        submit_button.pack()
        cur_win.mainloop()

    def _create_labyrinth(self, arg1, arg2):
        self._labyrinth = labyrinth_map.LabyrinthMap(arg1, arg2)

    def _labyrinth_bilder(self):
        # создать лабиринт по рамеру и стилю
        def create_by_WHS():
            def select_option():
                width = int(entry_width.get())
                height = int(entry_height.get())

                option = var.get()

                if option == "DFS":
                    self._create_labyrinth(1, [width, height, 'dfs'])
                elif option == "MST":
                    self._create_labyrinth(1, [width, height, 'mst'])
                elif option == "Aldus-Broder":
                    self._create_labyrinth(1, [width, height, 'aldus_broder'])
                elif option == "Rassel-Bolt":
                    self._create_labyrinth(1, [width, height, 'rassel_bolt'])

                cur_win.destroy()

            cur_win = tk.Tk()
            cur_win.title('')
            label_width = tk.Label(cur_win, text="Width:")
            label_width.pack()

            entry_width = tk.Entry(cur_win)
            entry_width.pack()

            label_height = tk.Label(cur_win, text="Height:")
            label_height.pack()

            entry_height = tk.Entry(cur_win)
            entry_height.pack()

            label_option = tk.Label(cur_win, text="Choose a style")
            label_option.pack()

            var = tk.StringVar(cur_win)
            var.set("DFS")  # Значение по умолчанию

            option_menu = tk.OptionMenu(
                cur_win, var, "DFS", "MST", "Aldus-Broder", "Rassel-Bolt")
            option_menu.pack()

            submit_button = tk.Button(
                cur_win, text="Create", command=select_option)
            submit_button.pack()

        # создание лабиринта по файлу
        def create_by_file():
            def select_option():
                filename = str(entry_filename.get())

                self._create_labyrinth(2, filename)

                cur_win.destroy()

            cur_win = tk.Tk()
            cur_win.title('')
            label_width = tk.Label(cur_win, text="Name of file:")
            label_width.pack()

            entry_filename = tk.Entry(cur_win)
            entry_filename.pack()

            submit_button = tk.Button(
                cur_win, text="Create", command=select_option)
            submit_button.pack()

        def select_option():
            option = var.get()

            if option == "By width, height and style":
                create_by_WHS()
            elif option == "By file":
                create_by_file()
            selection_win.destroy()

        selection_win = tk.Tk()
        selection_win.title('')

        label_option = tk.Label(
            selection_win, text="Choose the option to create a labyrinth")
        label_option.pack()

        var = tk.StringVar(selection_win)
        var.set("By width, height and style")  # Значение по умолчанию
        option_menu = tk.OptionMenu(
            selection_win, var, "By width, height and style", "By file")
        option_menu.pack()
        submit_button = tk.Button(
            selection_win, text="Next", command=select_option)
        submit_button.pack()
        selection_win.mainloop()

    def _print_labyrinth_in_terminal(self):
        print(self._labyrinth.get_str_map())

    def _print_labyrinth_in_window(self):
        cur_win = tk.Tk()
        cur_win.title("Представление лабиринта")
        # получение памаметров лабиринта
        right_walls, bottom_walls = self._labyrinth.get_map_info()
        # размер каждой ячейки
        square_size = 50
        cur_win.canvas = tk.Canvas(cur_win, width=(
            square_size * self._labyrinth.get_width()), height=(square_size * self._labyrinth.get_height()))
        cur_win.canvas.pack()
        finish_point = self._labyrinth.get_finish_point()
        self._draw_grid(cur_win, square_size, right_walls, bottom_walls)
        # self._draw_finish(cur_win, square_size, finish_point, {})
        cur_win.mainloop()
        # TODO сделать более адаптивным окно (на будующее)

    # to draw full map
    def _draw_grid(self, cur_win, square_size, right_walls, bottom_walls):
        cur_win.canvas.create_line(
            0, 0, (self._labyrinth.get_width() * square_size), 0, width=2, fill='black')
        cur_win.canvas.create_line(
            0, 0, 0, (self._labyrinth.get_height() * square_size), width=2, fill='black')
        for row in range(self._labyrinth.get_height()):
            for col in range(self._labyrinth.get_width()):
                if right_walls[row][col]:
                    x0, y0 = (col + 1) * square_size, row * square_size
                    x1, y1 = (col + 1) * square_size, (row + 1) * square_size
                    cur_win.canvas.create_line(
                        x0, y0, x1, y1, width=2, fill='black')
                if bottom_walls[row][col]:
                    x0, y0 = col * square_size, (row + 1) * square_size
                    x1, y1 = (col + 1) * square_size, (row + 1) * square_size
                    cur_win.canvas.create_line(
                        x0, y0, x1, y1, width=2, fill='black')

    # to draw finish mark im cell
    def _draw_finish(self, cur_win, square_size, finish_point, trevelers_dic):
        if trevelers_dic:
            for color, coord in trevelers_dic.items():
                if coord == finish_point:
                    return
        x00, y00 = finish_point[0] * square_size + \
            2, finish_point[1] * square_size + 2
        x01, y01 = (finish_point[0] + 1) * square_size - \
            3, (finish_point[1] + 1) * square_size - 3
        x10, y10 = finish_point[0] * square_size + \
            2, (finish_point[1] + 1) * square_size - 3
        x11, y11 = (finish_point[0] + 1) * square_size - \
            3, finish_point[1] * square_size + 2
        cur_win.canvas.create_line(x00, y00, x01, y01, width=5, fill='red')
        cur_win.canvas.create_line(x10, y10, x11, y11, width=5, fill='red')

    def _trevel_runner(self):
        def solo_button_pressed():
            self._set_start_and_finish(
                0, 0, self._labyrinth.get_width() - 1, self._labyrinth.get_height() - 1)
            cur_win.destroy()

            def close_button_pressed():
                instructions_win.destroy()

            instructions_win = tk.Tk()
            instructions_win.title('')
            label_intructions = tk.Label(
                instructions_win, text='This is instructions of moving.\n'
                + 'Player 1.\n'
                + '\'w\' - move to top direction\n'
                + '\'a\' - move to left direction\n'
                + '\'s\' - move to bottom direction\n'
                + '\'d\' - move to right direction\n'
                + 'Press \'Close\' to close instruction')
            label_intructions.pack()
            close_button = tk.Button(
                instructions_win, text="Close", command=close_button_pressed)
            close_button.pack()
            # запускаем игру для двух
            self._trevel([[0, 0]])
            instructions_win.mainloop()

        def duo_button_pressed():
            cur_win.destroy()
            start_point1 = [0, 0]
            start_point2 = [self._labyrinth.get_width() - 1,
                            self._labyrinth.get_height() - 1]
            # рандомно выбирается финиш
            finish_point = [labyrinth_map.rassel_bolt_gen.randrange(start_point2[0] + 1),
                            labyrinth_map.rassel_bolt_gen.randrange(start_point2[1] + 1)]
            self._labyrinth.set_finish_point(finish_point[0], finish_point[1])

            def close_button_pressed():
                instructions_win.destroy()

            instructions_win = tk.Tk()
            instructions_win.title('')
            label_intructions = tk.Label(
                instructions_win, text='This is instructions of moving.\n'
                + 'Player 1.\n'
                + '\'w\' - move to top direction\n'
                + '\'a\' - move to left direction\n'
                + '\'s\' - move to bottom direction\n'
                + '\'d\' - move to right direction\n'
                + 'Player 2.\n'
                + '\'i\' - move to top direction\n'
                + '\'j\' - move to left direction\n'
                + '\'k\' - move to bottom direction\n'
                + '\'l\' - move to right direction\n'
                + 'Press \'Close\' to close instruction')
            label_intructions.pack()
            close_button = tk.Button(
                instructions_win, text="Close", command=close_button_pressed)
            close_button.pack()
            # запускаем игру для двух
            self._trevel([start_point1, start_point2])
            instructions_win.mainloop()

        cur_win = tk.Tk()
        cur_win.title('')
        label_option = tk.Label(cur_win, text='Choose option')
        label_option.pack()
        solo_button = tk.Button(cur_win, text='Solo',
                                command=solo_button_pressed)
        solo_button.pack()

        duo_button = tk.Button(cur_win, text='Duo',
                               command=duo_button_pressed)
        duo_button.pack()

        cur_win.mainloop()

    def _trevel(self, trevelers):
        # trevelers - list of start position of players
        # Обработка нажатий клавиш
        def on_key_press(event):
            nonlocal cur_win
            nonlocal square_size
            nonlocal travalers_units
            nonlocal trevelers_dic
            # для перемещения первого персонажа
            if event.keysym == "w":
                trevelers_dic['red'] = move_treveler(
                    cur_win, travalers_units['red'], trevelers_dic['red'], [0, -1], square_size, 'red')  # Вверх
            elif event.keysym == "a":
                trevelers_dic['red'] = move_treveler(
                    cur_win, travalers_units['red'], trevelers_dic['red'], [-1, 0], square_size, 'red')  # Влево
            elif event.keysym == "s":
                trevelers_dic['red'] = move_treveler(
                    cur_win, travalers_units['red'], trevelers_dic['red'], [0, 1], square_size, 'red')  # Вниз
            elif event.keysym == "d":
                trevelers_dic['red'] = move_treveler(
                    cur_win, travalers_units['red'], trevelers_dic['red'], [1, 0], square_size, 'red')  # Вправо
            # для перемещения второго персонажа
            elif event.keysym == "i":
                trevelers_dic['blue'] = move_treveler(
                    cur_win, travalers_units['blue'], trevelers_dic['blue'], [0, -1], square_size, 'blue')  # Вверх
            elif event.keysym == "j":
                trevelers_dic['blue'] = move_treveler(
                    cur_win, travalers_units['blue'], trevelers_dic['blue'], [-1, 0], square_size, 'blue')  # Влево
            elif event.keysym == "k":
                trevelers_dic['blue'] = move_treveler(
                    cur_win, travalers_units['blue'], trevelers_dic['blue'], [0, 1], square_size, 'blue')  # Вниз
            elif event.keysym == "l":
                trevelers_dic['blue'] = move_treveler(
                    cur_win, travalers_units['blue'], trevelers_dic['blue'], [1, 0], square_size, 'blue')  # Вправо

        # Установка обработчиков клавиш
        def setup_keyboard_bindings():
            nonlocal cur_win
            cur_win.bind("<KeyPress>", on_key_press)

        # отрисока персонажей
        def draw_players(cur_win, square_size, trevelers_dic):
            travlers_units = {}
            for color, coord in trevelers_dic.items():
                x0, y0 = coord[0] * square_size + 5, coord[1] * square_size + 5
                x1, y1 = x0 + square_size - 11, y0 + square_size - 11
                travlers_units[color] = cur_win.canvas.create_oval(
                    x0, y0, x1, y1, fill=color)
            return travlers_units

        # Перемещение игрока
        def move_treveler(cur_win, treveler_unit, old_pos, direction, square_size, color):
            new_row = old_pos[1] + direction[1]
            new_col = old_pos[0] + direction[0]

            # to check is it possible to go another cell
            def direction_checker(direction, old_pos):
                if direction[0] == -1:
                    return self._labyrinth.get_cur_wall_status(old_pos[0], old_pos[1], 'left')
                if direction[0] == 1:
                    return self._labyrinth.get_cur_wall_status(old_pos[0], old_pos[1], 'right')
                if direction[1] == -1:
                    return self._labyrinth.get_cur_wall_status(old_pos[0], old_pos[1], 'top')
                if direction[1] == 1:
                    return self._labyrinth.get_cur_wall_status(old_pos[0], old_pos[1], 'bottom')

            if 0 <= new_row < self._labyrinth.get_height() and 0 <= new_col < self._labyrinth.get_width() and not direction_checker(direction, old_pos):
                old_pos = [new_col, new_row].copy()
                cur_win.canvas.move(treveler_unit, direction[0] *
                                    square_size, direction[1] * square_size)
            if old_pos == self._labyrinth.get_finish_point():
                # если мы тут то получается что какой-то игрок дошёл до финиша
                cur_win.destroy()
                congratulation = tk.Tk()
                congratulation.title('Завершение путешествия')
                label = tk.Label(congratulation, text=(
                    'Congratulation player with ' + color + ' color!'))
                label.pack()
                congratulation.mainloop()
            return old_pos

        cur_win = tk.Tk()
        cur_win.title("Прохождение лабиринта")
        # получение памаметров лабиринта
        right_walls, bottom_walls = self._labyrinth.get_map_info()
        colors = ['red', 'blue']
        # словарь бегущих по лабиринту и их цвета
        # просто каждому отдаю свои цвета
        trevelers_dic = {}
        for i in trevelers:
            index = 0
            trevelers_dic[colors[index]] = i
            del colors[index]
        square_size = 50
        cur_win.canvas = tk.Canvas(cur_win, width=(
            square_size * self._labyrinth.get_width()), height=(square_size * self._labyrinth.get_height()))
        cur_win.canvas.pack()
        finish_point = self._labyrinth.get_finish_point()
        # отрисовка карты
        self._draw_grid(cur_win, square_size, right_walls, bottom_walls)
        # отрисовка положений игроков и создание словаря каждого игрока
        travalers_units = draw_players(
            cur_win, square_size, trevelers_dic)
        # отрисока финиша
        self._draw_finish(
            cur_win, square_size, finish_point, trevelers_dic)
        # обработка нажатий на клавиши
        setup_keyboard_bindings()
        cur_win.mainloop()

    def _save_labyrinth(self):
        def select_option():
            file_name = str(entry_filename.get())
            file = ''
            try:
                file = open(file_name, "w")
            except Exception:
                raise
            file.write(self._labyrinth.get_str_map())
            file.close()
            cur_win.destroy()

        cur_win = tk.Tk()
        cur_win.title('')
        label_filename = tk.Label(
            cur_win, text="Enter name of file (expected .txt format)")
        label_filename.pack()
        entry_filename = tk.Entry(cur_win)
        entry_filename.pack()
        submit_button = tk.Button(
            cur_win, text="Save", command=select_option)
        submit_button.pack()
        cur_win.mainloop()

    def _set_start_and_finish(self, start_x, start_y, finish_x, finish_y):
        self._labyrinth.set_start_point(start_x, start_y)
        self._labyrinth.set_finish_point(finish_x, finish_y)

    def _get_start_and_finish(self):
        return self._labyrinth.get_start_point(), self._labyrinth.get_finish_point()

    def _solve_the_labyrinth(self):
        print(self._labyrinth.walker())
