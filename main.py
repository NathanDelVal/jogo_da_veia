import tkinter as tk
import tkinter.messagebox as messagebox


class Player:
    def __init__(self, symbol, color, name):
        self.name = name
        self.symbol = symbol
        self.color = color

player1 = Player('X','red', 'Jogador 1')
player2 = Player('O','blue', 'Jogador 2')

class TicTacToe:
    def switch_player(self):
        if self.player == player1:
            self.player = player2
        else:
            self.player = player1

    def click(self, event):
        label = event.widget
        label.config(text=self.player.symbol,fg=self.player.color)
        label.unbind('<Button-1>')
        self.check_winner()
        self.switch_player()

    def check_winner(self):
        for x in range(len(self.labels)):
            global x_win, y_win, diag_win, rev_diag_win
            x_win = y_win = diag_win = rev_diag_win = True
            for y in range(len(self.labels[0])):
                if self.labels[x][y]['text'] != self.player.symbol:
                    x_win = False
                if self.labels[y][x]['text'] != self.player.symbol:
                    y_win = False
                for [w,z] in ([0,0],[1,1],[2,2]):
                    if self.labels[w][z]['text'] != self.player.symbol:
                        diag_win = False
                for [w,z] in ([0,2],[1,1],[2,0]):
                    if self.labels[w][z]['text'] != self.player.symbol:
                        rev_diag_win = False
            if x_win == True or y_win == True or diag_win == True or rev_diag_win == True:
                messagebox.showinfo("WINNER", f"{self.player.name} WINS!")
                self.clear()
                self.executar()

    def clear(self):
        for x in self.labels:
            for y in x:
                y.destroy()
            
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Jogo da véia')
        self.executar()

    def executar(self):
        self.player = player1
        self.labels = []

        for x in range(3):
            temp_arr = []
            for y in range(3):
                temp = tk.Label(self.root, text=" ", padx=20, pady=10, relief=tk.SOLID, borderwidth=1)
                temp.grid(row=x,column=y)
                temp.bind('<Button-1>', self.click)
                temp_arr.append(temp)
            self.labels.append(temp_arr)
        
        self.root.mainloop()

    def switch_player(self):
        if self.player == player1:
            self.player = player2
        else:
            self.player = player1


ttt = TicTacToe()