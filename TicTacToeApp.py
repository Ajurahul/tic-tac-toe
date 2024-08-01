import tkinter as tk
from tkinter import messagebox


class TicTacToeApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.buttons = [[_ for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text=' ', font=('Arial', 40), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)

    def on_button_click(self, row, col):
        if self.buttons[row][col] == ' ':
            self.buttons[row][col] = self.current_player
            if self.check_win(self.current_player):
                messagebox.showinfo("Game over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Game over", f"Its a draw")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col]['text'] = ' '
                self.current_player = 'X'

    def check_win(self, player):
        for i in range(3):
            if all(self.buttons[i][j]['text'] == player for j in range(3)) or all(
                    self.buttons[i][j]['text'] == player for j in range(3)):
                return True
        if all(self.buttons[i][i]['text'] == player for i in range(3)) or all(
                self.buttons[i][2 - i]['text'] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(self.buttons[i][j]['text'] != ' ' for i in range(3) for j in range(3))


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeApp(root)
    root.mainloop()
