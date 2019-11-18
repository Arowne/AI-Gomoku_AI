class MinMaxBot:

    def __init__(self):
        self.size = None
        self.move_index = 0
        self.current_board = []

    def play(self, board, current_player, board_size, move_index):
        self.size = board_size
        self.move_index = move_index
        self.current_board = board
        available_move = self.get_possible_move(board, board_size)
        get_max = self.max_score(current_player, available_move)
        self.current_board[get_max[0][0]][get_max[0][1]] = current_player

    def max_score(self, current_player, available_move):
        max_score = -1000
        max_move = []
        for move in available_move:
            self.current_board[move[0]][move[1]] = current_player

            if self.check_victory("O"):
                get_move = [move[0], move[1]]
                score = 1
            else:
                get_move = [move[0], move[1]]
                score = 0
            
            if score > max_score:
                max_score = score
                max_move = get_move
            self.current_board[move[0]][move[1]] = '-'
        return [max_move, max_score]
    
    def get_possible_move(self, board, board_size):
        available_move = []
        for y in range(board_size):
            for x in range(board_size):
                if board[y][x] == '-':
                    available_move.append([y, x])
        return available_move

    # Check victory
    def check_victory(self, player):
        get_board_size = self.size
        get_board = self.current_board
        current_player = player
        current_player_name = player

        for y in range(get_board_size):
            for x in range(get_board_size):
                if get_board[y][x] == current_player:
                    if self.check_horizontal_victory(x, y , current_player, current_player_name):
                        return True
                    if self.check_vertical_victory(x, y , current_player, current_player_name):
                        return True
                    if self.check_diagonnal_victory_1(x, y , current_player, current_player_name):
                        return True
                    if self.check_diagonnal_victory_2(x, y , current_player, current_player_name):
                        return True
        return False

    # Check horizontal victory
    def check_horizontal_victory(self, x, y, current_player, current_player_name):
        win_index = 0
        for index in range(5):
            try:
                if self.current_board[y][x+index] == current_player:
                    print(current_player)
                    win_index += 1
                    if win_index == 5:
                        return True
                else:
                    win_index = 0
            except:
                win_index = 0
        return False

    # Check vertical victory
    def check_vertical_victory(self, x, y, current_player, current_player_name):
        win_index = 0
        for index in range(5):
            try:
                if self.current_board[y + index][x] == current_player:
                    print(current_player)
                    win_index += 1
                    if win_index == 5:
                        return True
                else:
                    win_index = 0
            except:
                win_index = 0
        return False

    # Check diagonal victory  (left to  right)
    def check_diagonnal_victory_1(self, x, y, current_player, current_player_name):
        win_index = 0
        for index in range(5):
            try:
                if self.current_board[y + index][x + index] == current_player:
                    print(current_player)
                    win_index += 1
                    if win_index == 5:
                        return True
                else:
                    win_index = 0
            except:
                win_index = 0
        return False

    # Check diagonal victory  (right to left)
    def check_diagonnal_victory_2(self, x, y, current_player, current_player_name):
        win_index = 0
        for index in range(5):
            try:
                if self.current_board[y + index][x - index] == current_player and x - index > 0:
                    win_index += 1
                    if win_index == 5:
                        return True
                else:
                    win_index = 0
            except:
                win_index = 0
        return False