class Communication_protocol:

    def __init__(self):
        print("Init game")
        self.size = 0
        self.current_board = []
        self._x = 'X'
        self._o = 'O'
        self.board_list = []
        self.last_move = []
        self.move_index = 0

    # Check if board size is valid
    def check_boardsize(self, boardsize):
        get_value = boardsize.split(' ')
        command = get_value[0]
        get_board_size = int(get_value[1])

        if int(get_board_size) > 4 and int(get_board_size) < 100 and command == 'START':
            self.size = get_board_size + 1
            print("OK - everything is good")
            return True
        else:
            print("ERROR message - unsupported size or other error")
            return False

    def init_game(self):
        self.init_board()

    # Init board for being displayed
    def init_board(self):
        get_board_size = int(self.size)
        board = []

        for box in range(get_board_size):
            board.append([])
            last_index = len(board)
            current_index = box
            get_last_column = board[last_index-1]
            for box in range(get_board_size):
                if box == 0 and current_index > 0:
                    get_last_column.append(current_index - 1)
                if current_index > 0:
                    get_last_column.append('-')
                elif box > 0:
                    get_last_column.append(box - 1)
                else:
                    get_last_column.append(' ')

        self.current_board = board
        self.display_board(True)

    # Display current board
    def display_board(self, is_init):
        get_board_size = len(self.current_board)
        get_board = self.current_board
        board_to_str = ''

        for box in range(get_board_size):
            current_index = box
            board_to_str += '\n'
            for box in range(get_board_size):
                if box > 0:
                    if box == 1 and current_index <= 9 + 1:
                        board_to_str += ' '
                    board_to_str += '  ' + \
                        str(get_board[current_index][box]) + ' '
                    if box > 9 + 1 and current_index > 0:
                        board_to_str += ' '
                else:
                    board_to_str += '  ' + str(get_board[current_index][box])
        if is_init == True:
            self.get_first_turn("Would you like to begin ?\n")
        else:
            if len(self.last_move) == 2:
                print('oppenent move', self.last_move[0], self.last_move[1])
        print(board_to_str)
        self.get_movement("Choose where you want to play 'x y'\n")

    # Set begginer
    def get_first_turn(self, msg):
        set_starter = input(msg)
        if set_starter == 'y':
            self.player_x = 'player'
            self.player_o = 'ia'
        elif set_starter == 'x':
            self.player_x = 'ia'
            self.player_o = 'player'
        else:
            self.get_first_turn(
                "Your previous response is invalid. Would you like to begin ?\n")

    # Get new movement
    def get_movement(self, msg):
        movement = input(msg)
        if movement == 'BOARD':
            self.set_board_movement(movement)
        else:
            self.set_movement(movement)

    # Set new movement
    def set_movement(self, coordinate):
        get_coordinate_array = coordinate.split(' ')
        get_max_coord = int(self.size)
        get_min_coord = 0
        get_current_index = self.move_index
        command = get_coordinate_array[0]
        coordinate = get_coordinate_array[1].split(',')
        x = int(coordinate[0]) + 1
        y = int(coordinate[1]) + 1

        if len(get_coordinate_array) != 2:
            self.get_movement(
                "This coordinate is not valid. Choose where you want to play 'x y' \n")
        elif command != 'TURN':
            self.get_movement(
                "This coordinate is not valid. Choose where you want to play 'x y' \n")
        elif x >= get_max_coord or y >= get_max_coord or x == 0 or y == 0:
            self.get_movement(
                "This coordinate is not valid. Choose where you want to play 'x y' \n")
        else:
            if get_current_index % 2 == 0:
                self.current_board[y][x] = self._x
            else:
                self.current_board[y][x] = self._o

            self.last_move = get_coordinate_array
            self.move_index += 1
            self.check_victory()
            self.display_board(False)

    # Set new movement
    def set_board_movement(self, coordinate):
        while 42:
            last_command = input("")
            if last_command == 'DONE':
                self.display_board(False)
                break
            else:
                get_position = last_command.split(',')
                self.current_board[int(get_position[1]) + 1][int(
                    get_position[0]) + 1] = self._x
    # Check victory
    def check_victory(self):
        get_board_size = self.size
        get_board = self.current_board

        if self.move_index % 2 == 0:
            current_player = self._o
            current_player_name = self.player_o
        else:
            current_player = self._x
            current_player_name = self.player_x

        for y in range(get_board_size):
            for x in range(get_board_size):
                if get_board[y][x] == current_player:
                    self.check_horizontal_victory(x, y , current_player, current_player_name)
                    self.check_vertical_victory(x, y , current_player, current_player_name)
                    self.check_diagonnal_victory_1(x, y , current_player, current_player_name)
                    self.check_diagonnal_victory_2(x, y , current_player, current_player_name)

    # Check horizontal victory
    def check_horizontal_victory(self, x, y, current_player, current_player_name):
        win_index = 0
        for index in range(5):
            try:
                if self.current_board[y][x+index] == current_player:
                    win_index += 1
                    if win_index == 5:
                        print(current_player_name + " win !")
                else:
                    win_index = 0
            except:
                win_index = 0

    # Check vertical victory
    def check_vertical_victory(self, x, y, current_player, current_player_name):
        win_index = 0
        for index in range(5):
            try:
                if self.current_board[y + index][x] == current_player:
                    win_index += 1
                    if win_index == 5:
                        print(current_player_name + " win !")
                else:
                    win_index = 0
            except:
                win_index = 0

    # Check diagonal victory  (left to  right)
    def check_diagonnal_victory_1(self, x, y, current_player, current_player_name):
        win_index = 0
        for index in range(5):
            try:
                if self.current_board[y + index][x + index] == current_player:
                    win_index += 1
                    if win_index == 5:
                        print(current_player_name + " win !")
                else:
                    win_index = 0
            except:
                win_index = 0

    # Check diagonal victory  (right to left)
    def check_diagonnal_victory_2(self, x, y, current_player, current_player_name):
        win_index = 0
        for index in range(5):
            try:
                if self.current_board[y + index][x - index] == current_player and x - index > 0:
                    win_index += 1
                    if win_index == 5:
                        print(current_player_name + " win !")
                else:
                    win_index = 0
            except:
                win_index = 0

if __name__ == "__main__":
    commuication_protocol = Communication_protocol()
    board_size = input("Please enter size of your board\n")
    boardsize_is_valid = commuication_protocol.check_boardsize(board_size)

    # Begin game
    if boardsize_is_valid:
        commuication_protocol.init_game()
