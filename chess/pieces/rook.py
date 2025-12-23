class Rook:
    def __init__(self, color):
        self.color = color

    def is_valid(self, board, sr, sc, er, ec):
        direction_ud = -1 if sr > er else 1
        direction_lr = -1 if sc > ec else 1
        if sc == ec and sr != er:
            for i in range(1, abs(er - sr)):
                if board[sr + i * direction_ud][sc] != '.':
                    return False

        if sc != ec and sr == er:
            for i in range(1, abs(ec - sc)):
                if board[sr][sc + i * direction_lr] != '.':
                    return False
        if sc != ec and sr != er:
            return False

        target = board[er][ec]
        if self.color == "black" and target.islower():
            return False
        if self.color == "white" and target.isupper():
            return False

        return True