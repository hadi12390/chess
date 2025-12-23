import os
from pieces.pawn import Pawn
from pieces.rook import Rook
class Board:
    def __init__(self):
        self.board = self._create_board()
        self.pieces = { # لحتى نعمل رمز لاسم الكلاس بنفس الحرف الموجود
            'p':Pawn,
            'r':Rook
        }
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
    def display(self, flip=False):
        """عرض البورد. flip=True لللاعب الأسود."""
        print("\n    a b c d e f g h")
        print("  +-----------------+")

        rows = self.board[::-1] if flip else self.board  # فقط عكس الصفوف
        for i, row in enumerate(rows):
            row_str = " ".join(row)
            row_num = 8 - i if not flip else i + 1  # عكس أرقام الصفوف فقط
            print(f"{row_num} | {row_str} | {row_num}")

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
        col_map = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        while True:
            start = input("Enter the starting position: ").lower()
            end = input("Enter the ending position: ").lower()

            # تحقق من صحة الطول والمدخلات
            if len(start) != 2 or len(end) != 2:
                print("Invalid input format! Use e.g. 'e2'")
                continue

            if start[0] not in col_map or end[0] not in col_map:
                print("Invalid column! Must be a-h")
                continue

            if not start[1].isdigit() or not end[1].isdigit():
                print("Invalid row! Must be 1-8")
                continue

            start_col = col_map[start[0]]
            start_row = 8 - int(start[1])
            end_col = col_map[end[0]]
            end_row = 8 - int(end[1])

            if not self.check_move_for_board(start_row, start_col, end_row, end_col):
                print("Invalid Move")
                continue

            piece = self.board[start_row][start_col] # متغير اسمه piece بنحط فيه الرمز المطلوب تحريكه
            piece_type = piece.lower() # بنسستم الرمز
            if piece_type in self.pieces: # لو الرمز المطلوب تحريكه موجود بالسيستم
                color = "white" if piece.isupper() else "black" # نعرف اللون لحتى نمرره للاوبجكت
                piece_obj =  self.pieces[piece_type](color) # نعمل الاوبجكت عن طريق القاموس الي فوق

                if not piece_obj.is_valid(self.board, start_row, start_col, end_row, end_col): # نحلبس
                    print("Invalid Move for this piece")
                    continue
            # تحريك القطعة
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = "."
            break


board = Board()
while True:
    board.display()
    board.move()
    board.display(True)
    board.move()

print("New Line")