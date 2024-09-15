from tkinter import * 
import random
from tkinter import messagebox


class Tik_tak_toe:

    def __init__(self, window2, mode = "multi"):
        self.window = window2
        self.mode = mode 
        self.current_player = "X"
        self.score = {"X":0, "O":0} #this is the dictionary with the key first and then the score
        self.buttons = [[None for i in range(3)]for i in range(3)]
        self.creat_widgets()

    def creat_widgets(self):
        self.score_label = Label(self.window, text = self.get_score(), font = ("times", 20))
        self.score_label.grid(row = 0, column = 0, columnspan = 3, pady = 10)
        for row in range(3):
            for column in range(3):
                button_widget = Button(self.window, text="", font=('normal', 40), width=5, height=2,
                                   command=lambda r=row, c=column: self.on_button_click(r, c))
                button_widget.grid(row=row + 1, column=column)
                self.buttons[row][column] = button_widget
    
    def on_button_click(self, row, column):
        #self.buttons[row][column]["text"] - cheaks if the button text is empty
        #self.check_winner() - cheaks if the current move results in winner
        if self.buttons[row][column]['text'] == "" and not self.check_winner():
            self.buttons[row][column]['text'] = self.current_player
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} won!")
                self.update_score(self.current_player)
                self.reset_game()
            elif self.is_board_full():
                messagebox.showerror("Game over", "It was a tie" )
                self.reset_game()
            else:
                if self.mode == "single" and self.current_player == "X":
                    self.current_player = "O"
                    self.computor_move()
                else:
                    self.current_player = "O" if self.current_player == "X" else "X" #one line if condition is also called terrnary operator
    
    def computor_move(self):
        empty_buttons = [(r,c) for r in range(3) for c in range(3)  if self.buttons[r][c]["text"] == ""]
        if empty_buttons:
            r,c = random.choice(empty_buttons)
            self.buttons[r][c]["text"] = "O"
            if self.check_winner():
                messagebox.showinfo("winner", "Player O won")
                self.update_score("O")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showwarning("Game is over", "Game is over")
                self.reset_game()
            else:
                self.current_player = "X"

    def is_board_full(self):
        return all(self.buttons[row][column]["text"] != "" for row in range(3) for column in range(3))
    
    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]["text"] == self.buttons[row][2]['text']:
                return True
        
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text']:
                return True 
        
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text']:
            return True 
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][1]['text']:
            return True
        
        return False
    
    def update_score(self, player):
        self.score[player]+=1
        
    def update_score_label(self):
        self.score_label.config(text = self.get_score())

    def get_score(self):
        return f"Score: X: {self.score['X']} | O: {self.score['O']}"
    
    def reset_game(self):
        for row in range(3):
            for column in range(3):
                self.buttons[row][column]["text"] = ""
        self.current_player = "X"
        self.update_score_label()


class Menu:
    
    def __init__(self, window1):
        self.window = window1
        self.window.title("Tic Tak Toe starting page")
        self.create_widjts()
        
    def create_widjts(self):
        title = Label(self.window, text = "Select Mode", font = ("normal", 20)).pack(pady = 15, padx = 15)
        button1 = Button(self.window, text = "Single Player", font = ("times", 15), command = self.start_single_player).pack(pady = 15, padx = 15)
        button2 = Button(self.window, text = "Multi Player", font = ("times", 15), command = self.start_multi_player).pack(pady = 15, padx = 15)

    def start_single_player(self):
        self.window.destroy()
        self.start_game("single")

    def start_multi_player(self):
        self.window.destroy()
        self.start_game("multi")

    def start_game(self, mode):
        window2 = Tk()
        Tik_tak_toe(window2, mode)
        window2.mainloop()


if __name__ == "__main__":
    window1 = Tk()
    Menu(window1)


window1.mainloop()
