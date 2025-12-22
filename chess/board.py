class Board:
    def __init__(self):
        self.board = self._create_board()
    # لصنع البورد
    def _create_board(self):
        return [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]
    # لعرض البورد
    def display(self):
        print("\n    a b c d e f g h")
        print("  +-----------------+")
        for i, row in enumerate(self.board):
            # إضافة رقم الصف وحواجز جانبية لشكل احترافي
            row_str = " ".join(row)
            print(f"{8 - i} | {row_str} | {8 - i}")
        print("  +-----------------+")
        print("    a b c d e f g h\n")
    # لتحريك قطعة بدون القواعد (حاليا)
    def move(self, start, end):
        col_map = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}

    
    

b = Board()
b.display()
