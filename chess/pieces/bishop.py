class Bishop:
    def __init__(self, color):
        self.color = color
    def is_valid(self, board, sr, sc, er, ec):
        if abs(er - sr) != abs(ec - sc):
            return False
        change_col = 1 if ec > sc else -1 if ec < sc else 0
        change_row = 1 if er > sr else -1 if er < sr else 0

        for i in range(1, abs(er - sr)):
            if board[sr + (i*change_row)][sc + (i*change_col)] != ".":
                return False

        target = board[er][ec]
        if self.color == "black" and target.islower():
            return False
        if self.color == "white" and target.isupper():
            return False

        return True
