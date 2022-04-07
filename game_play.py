
player1 = None
player2 = None
game = None

class Player():

    def __init__(self, name, is_computer, com_intel):
        self.name = name
        self.is_computer = is_computer
        self.com_intel = com_intel


class TikTok():

    def __init__(self, player1 , player2):
        self.player1 = player1
        self.player2 = player2
        self.tablo = {player1 :[] ,player2 :[]}
        self.score_board = {player1 :0, player2 :0}
        self.count = 0
        self.game_count = 0

    def current_player(self):
        if len(self.tablo[self.player1] ) +len(self.tablo[self.player2]) == 0:
            if self.game_count % 2 == 0:
                return self.player1
            else:
                self.count += 1
                return self.player2

        if self.count % 2 == 0:

            return self.player1
        else :
            return self.player2

    def other_player(self):
        if self.current_player() == self.player1:
            return self.player2
        else : return self.player1

    def check_for_winner(self):
        winning_series = [[1 ,2 ,3], [1 ,4 ,7], [1 ,5 ,9], [4 ,5 ,6], [7 ,8 ,9], [2 ,5 ,8], [3 ,6 ,9], [3 ,5 ,7]]
        for j in winning_series:
            if all(i in self.tablo[self.current_player()] for i in j):
                return True
        else: return False

    def check_for_draw(self):
        if len(self.tablo[self.player1] ) +len(self.tablo[self.player2]) == 9:
            return True
        else: return False
