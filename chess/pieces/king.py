class  King:
    def __init__(self, color):
        self.color = color
    def is_valid(self, board, sr, sc, er, ec):
        if max(abs(er - sr), abs(ec - sc)) != 1:
            return False
        target = board[er][ec]
        if self.color == "black" and target.islower():
            return False
        if self.color == "white" and target.isupper():
            return False

        return True