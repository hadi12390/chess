class Pawn:
    def __init__(self, color):
        self.color = color

    def is_valid(self, board, sr, sc, er, ec):
        direction = -1 if self.color == "white" else 1

        # خطوة للأمام
        if sc == ec and er == sr + direction and board[er][ec] == '.':
            return True

        # خطوتين للأمام
        if sc == ec and board[er][ec] == '.':
            if (self.color == "white" and sr == 6 and er == 4) or \
               (self.color == "black" and sr == 1 and er == 3):
                if board[sr + direction][ec] == '.':
                    return True

        # أكل قطري
        if abs(sc - ec) == 1 and er == sr + direction and board[er][ec] != '.':
            target = board[er][ec]
            if (self.color == "black" and target.isupper()) or \
               (self.color == "white" and target.islower()):
                return True

        return False
