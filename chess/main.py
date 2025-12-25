from board import Board
b = Board()
while True:
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
        b.display(True)
        b.move("black")
        continue