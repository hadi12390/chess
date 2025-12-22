import os
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
    def check_move_for_board(self, start_row, start_col, end_row, end_col):
        start_piece = self.board[start_row][start_col]
        end_piece = self.board[end_row][end_col]

        if start_piece == ".": # اذا حاول يحرك من مكان فاضي
            return False

        if (start_piece.isupper() and end_piece.isupper()) or (start_piece.islower() and end_piece.islower()): # اذا حاول يوكل قطع نفسه
            return False

        return True
    def move(self):
        col_map = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7} # خريطة لمساواة بين الحرف و رقم لسهولة تحويله لاحداثيات عامود
        while True:
            start = input("Enter the starting position: ").lower()
            end = input("Enter the ending position: ").lower()
            start_col = col_map[start[0]]  # اخذ اول حرف من المدخل و وضعه في الخريطة لنحصل على الرفم المقابل له
            start_row = 8 - int(start[1]) # لعكس الموقع نطرح من رقم سبعة الرقم المدخل و نزيد واحد نحصل على الصف
            end_col = col_map[end[0]]
            end_row = 8 - int(end[1])
            if self.check_move_for_board(start_row, start_col, end_row, end_col) == False:
                print("Invalid Move")
                continue
            else:
                break
        self.board[end_row][end_col] = self.board[start_row][start_col] # نضع مكان الوجهة ما كان موجود في مكان البداية و مكان البداية نضع نقطة
        self.board[start_row][start_col] = "."
b = Board()
b.display()
b.display()