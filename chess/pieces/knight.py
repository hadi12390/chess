class Knight:
    def __init__(self, color):
        self.color = color
    def is_valid(self, board, sr, sc, er, ec):
        delta_R = abs(er - sr)
        delta_C = abs(ec - sc)
        if not ((delta_R == 1  and delta_C == 2) or (delta_R == 2 and delta_C == 1)):
            return False
        target = board[er][ec]
        if (self.color == "black" and target.islower()) or (self.color == "white" and target.isupper()):
            return False
        return True