import tkinter as tk
import time

def update_display(board, btn_cells):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                btn_cells[i][j].config(text=str(board[i][j]))
            else:
                btn_cells[i][j].config(text="")

def is_valid(board, row, column, k):
    valid_row = k not in board[row]
    valid_col = k not in [board[i][column] for i in range(9)]
    valid_subgrid = k not in [board[i][j] for i in range(row//3*3, row//3*3 + 3) for j in range(column//3*3, column//3*3 + 3)]
    return valid_row and valid_col and valid_subgrid

def solver(board, btn_cells, row=0, column=0):
    if row == 9:
        return True
    if column == 9:
        return solver(board, btn_cells, row + 1, 0)
    if board[row][column] != 0:
        return solver(board, btn_cells, row, column + 1)

    for k in range(1, 10):
        if is_valid(board, row, column, k):
            board[row][column] = k
            update_display(board, btn_cells)
            root.update()  # Update the GUI
            time.sleep(0.1)  # Delay for demonstration
            if solver(board, btn_cells, row, column + 1):
                return True
            board[row][column] = 0
            update_display(board, btn_cells)
            root.update()  # Update the GUI
            time.sleep(0.1)  # Delay for demonstration
    return False

def main():
    global root
    root = tk.Tk()
    root.title("Sudoku Solver Animated")

    board_frame = tk.Frame(root, bg='white')
    board_frame.pack(pady=20, padx=20)

    blocks = []
    for r in range(3):
        row = []
        for c in range(3):
            frame = tk.Frame(board_frame, bd=1, highlightbackground='light blue',
                             highlightcolor='light blue', highlightthickness=1)
            frame.grid(row=r, column=c, sticky='nsew')
            row.append(frame)
        blocks.append(row)

    btn_cells = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            frm_cell = tk.Frame(blocks[i // 3][j // 3])
            frm_cell.grid(row=(i % 3), column=(j % 3), sticky='nsew')
            frm_cell.rowconfigure(0, minsize=50, weight=1)
            frm_cell.columnconfigure(0, minsize=50, weight=1)
            btn_cells[i][j] = tk.Button(frm_cell, relief='ridge', bg='white', font=('Helvetica', 16))
            btn_cells[i][j].grid(sticky='nsew')

    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    update_display(board, btn_cells)
    root.after(0, solver, board, btn_cells)
    root.mainloop()

if __name__ == "__main__":
    main()
