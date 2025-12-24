from board import Board
b = Board()
while True:
    b.display()
    b.move("white")
    b.display(True)
    b.move("black")