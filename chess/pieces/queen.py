class Queen:
    def __init__(self, color):
        self.color = color
    def is_valid(self, board, sr, sc, er, ec):
        if abs(er - sr) == abs(ec - sc):
            vertical = False
            diagonal = True
        elif sr == er or sc == ec:
            vertical = True
            diagonal = False
        else:
            return False
        if diagonal:
            change_col = 1 if ec > sc else -1 if ec < sc else 0
            change_row = 1 if er > sr else -1 if er < sr else 0

            for i in range(1, abs(er - sr)):
                if board[sr + (i * change_row)][sc + (i * change_col)] != ".":
                    return False

            target = board[er][ec]
            if self.color == "black" and target.islower():
                return False
            if self.color == "white" and target.isupper():
                return False

            return True
        else:
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

