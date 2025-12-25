from board import Board
b = Board()
while True:
    if b.is_check("white"):
        b.display()
        print("⚠ White king is in check ⚠")
    else:
        b.display()
    b.move("white")
    if b.check_mate("black"):
        b.display(True)
        print("White Win..CheckMate")
        break
    elif b.check_mate("white"):
        b.display()
        print("Black Win..CheckMate")
        break
    else:
        if b.is_check("black"):
            b.display(True)
            print("⚠ Black king is in check ⚠")
        else:
            b.display(True)
        b.move("black")
        continue