
game = None
class Game_Play():

    def __init__(self, p1_name , p2_name , p1_is_computer , p2_is_computer , com_intelligence = 0):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p2iscom = p2_is_computer
        self.p1iscom = p1_is_computer
        self.intel = com_intelligence
        self.tablo = {p1_name :[] ,p2_name :[]}
        self.score_board = {p1_name :0, p2_name :0}
        self.count = 0
        self.game_count = 0

    def current_player(self):
        if len(self.tablo[self.p1_name] ) +len(self.tablo[self.p2_name]) == 0:
            if self.game_count % 2 == 0:
                return self.p1_name
            else:
                self.count += 1
                return self.p2_name

        if self.count % 2 == 0:

            return self.p1_name
        else :
            return self.p2_name

    def other_player(self):
        if self.current_player() == self.p1_name:
            return self.p2_name
        else : return self.p1_name

    def check_for_winner(self):
        winning_series = [[1 ,2 ,3], [1 ,4 ,7], [1 ,5 ,9], [4 ,5 ,6], [7 ,8 ,9], [2 ,5 ,8], [3 ,6 ,9], [3 ,5 ,7]]
        for j in winning_series:
            if all(i in self.tablo[self.current_player()] for i in j):
                return True
        else: return False

    def check_for_draw(self):
        if len(self.tablo[self.p1_name] ) +len(self.tablo[self.p2_name]) == 9:
            return True
        else: return False
