from tkinter import *
import time as t

def nxt_move(row,column):
    global player

    if tiles[row][column]["text"] == "" and win_detect() is False:
        if player == players[0]:
            tiles[row][column]["text"] = player

            if win_detect() is False:
                player = players[1]
                label.config(text=(players[1]+"'s turn"))

            elif win_detect() is True:
                label.config(text=(players[0]+" wins"))

            elif win_detect() == "draw":
                label.config(text="Tied!")

        else:
            tiles[row][column]["text"] = player

            if win_detect() is False:
                player = players[0]
                label.config(text=(players[0]+"'s turn"))

            elif win_detect() is True:
                label.config(text=(players[1]+" wins"))

            elif win_detect() == "draw":
                label.config(text="Tied!")

    player1 = 0
    player1_score = player1
    player2 = 0
    player2_score = player2

#for player 1 score
    for row in range(3):
        for column in range(3):
            if tiles[row][column]["text"] == "X":
                player1 += 1
                player1_score = 20 - (player1*2)
    print(f"score for x: {player1_score}")

#for player 2 score
    for row in range(3):
        for column in range(3):
            if tiles[row][column]["text"] == "O":
                player2 += 1
                player2_score = 20 - (player2*2)
    print(f"score for o: {player2_score}")

    if win_detect() is True:
        
        if player1 >= player2:
            score_display.config(text=(player1,"|", player1_score),padx=15)
        elif player2 >= player1:
            score_display.config(text=(player2,"|", player2_score),padx=15)
        else:
            return 0
        player1 -= player1 
        player2 -= player2 
        print(player1, player2)

    elif draw() is False:
        player1 -= player1
        player2 -= player2
        print(player1, player2)
    else:
        return 0

def win_detect():
    global tiles

#VERTICAL CHECKING
    for row in range(3):
        if tiles[row][0]["text"] == tiles[row][1]["text"] == tiles[row][2]["text"] != "":
            tiles[row][0].config(bg="white")
            tiles[row][1].config(bg="white")
            tiles[row][2].config(bg="white")
            return True

#HORIZONTAL CHECKING
    for column in range(3):
        if tiles[0][column]["text"] == tiles[1][column]["text"] == tiles[2][column]["text"] != "":
            tiles[0][column].config(bg="white")
            tiles[1][column].config(bg="white")
            tiles[2][column].config(bg="white")
            return True

#DIAGONAL CHECKING
    if tiles [0][0]["text"] == tiles [1][1]["text"] == tiles [2][2]["text"] != "":
        tiles[0][0].config(bg="white")
        tiles[1][1].config(bg="white")
        tiles[2][2].config(bg="white")
        return True

#DIAGONAL CHECKING (REVERSE)
    elif tiles [2][0]["text"] == tiles [1][1]["text"] == tiles [0][2]["text"] != "":
        tiles[2][0].config(bg="white")
        tiles[1][1].config(bg="white")
        tiles[0][2].config(bg="white")
        return True

    elif draw() is False:
        return "draw"

    else:
        return False

def draw():
    isEmpty = 0

    for row in range(3):
        for column in range(3):
            if tiles [row][column]["text"] != "":
                isEmpty += 1

    if isEmpty == 9:
        tiles[0][0].config(bg="#e84c41")
        tiles[0][1].config(bg="#e84c41")
        tiles[0][2].config(bg="#e84c41")
        tiles[1][0].config(bg="#e84c41")
        tiles[1][1].config(bg="#e84c41")
        tiles[1][2].config(bg="#e84c41")
        tiles[2][0].config(bg="#e84c41")
        tiles[2][1].config(bg="#e84c41")
        tiles[2][2].config(bg="#e84c41")
        return False
    else:
        return True

def restart_game():

    global player
    player = ["O"]
    for row in range (3):
        for column in range (3):
            tiles[row][column].config(text="")
            score_display.config(text="")
    tiles[0][0].config(bg="#86db9d")
    tiles[0][1].config(bg="#86db9d")
    tiles[0][2].config(bg="#86db9d")
    tiles[1][0].config(bg="#86db9d")
    tiles[1][1].config(bg="#86db9d")
    tiles[1][2].config(bg="#86db9d")
    tiles[2][0].config(bg="#86db9d")
    tiles[2][1].config(bg="#86db9d")
    tiles[2][2].config(bg="#86db9d")

    if tiles[row][column]["text"] != "":
        label.config(text="", font=("Arial",15,"bold"))

    else:
        label.config(text="O's Turn", font=("Arial",15,"bold"))
        


window = Tk()
window.geometry("330x390")
window.resizable(0,0)
window.title("SHIT GAME")

players = ["X","O"]
player = "X"

tiles = [[1,2,3],
         [4,5,6],
         [7,8,9]]

label = Label(text="X's Turn", font=("Arial",15,"bold"),padx=20)
label.place(y=350,x=15)

reset_button = Button(text="RESET", font=("Arial",13,"bold"),bg="#789e82",command=restart_game)
reset_button.place(y=350,x=132)

frame = Frame(window)
frame.place(y=10,x=18)

for row in range(3):
    for column in range(3):
        tiles[row][column] = Button(frame, text="",font=('consolas',40), width=3, height=1,command=lambda row=row, column=column: nxt_move(row,column),bd=3,bg="#86db9d")
        tiles [row][column].grid(row=row,column=column)

score_display = Label(text="", font=("Arial",15,"bold"))
score_display.place(y=350,x=220)

window.mainloop()
