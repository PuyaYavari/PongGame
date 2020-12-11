import Ball
import Board
import InputHandler
import Stick

import os
import threading
import time


def run(board, inputHandler):
    inputHandler.evaluate()
    os.system('cls')
    if board.evaluate():
        board.render()
        threading.Timer(0.001, run,[board, inputHandler]).start()
    else:
        print("Game Over")

if __name__ == "__main__":
    board = Board.Board(50, 20, Ball.Ball([10.0,10.0],[1,1]), \
                Stick.Stick(5, 8, 2, {"min":0, "max":20}))
    inputHandler = InputHandler.InputHandler(board)
    run(board, inputHandler)
