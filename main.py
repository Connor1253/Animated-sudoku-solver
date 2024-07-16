import tkinter as tk
board = [[0] * 9 for i in range(9)]
def is_valid(board, row, column, k):
    valid_row = k not in board[row]
    valid_col = k not in [board[i][column] for i in range(9)]
    valid_subgrid = k not in [board[i][j] for i in range(row//3*3, row//3*3 + 3) for j in range(column//3*3, column//3*3 + 3)]
    return valid_row and valid_col and valid_subgrid
def solver(board, row=0, column=0):
    if row == 9:
        return board
    elif column == 9:
        return solver(board, row + 1, 0)
    elif board[row][column] != 0:
        return solver(board, row, column + 1)
    else:
        for k in range(1, 10):
            if is_valid(board, row, column, k):
                board[row][column] = k
                if solver(board, row, column + 1):
                    return board
                board[row][column] = 0
        return False
solution = solver(board)

root = tk.Tk()
board = tk.Frame(root, bg='white')
board.pack()
blocks = []
for r in range(3):
    row = []
    for c in range(3):
        frame = tk.Frame(board, bd=1, highlightbackground='light blue',
                         highlightcolor='light blue',
                         highlightthickness=1)
        frame.grid(row=r, column=c, sticky='nsew')
        row.append(frame)
    blocks.append(row)
btn_cells = [[None for x in range(9)] for x in range(9)]
for i in range(9):
    for j in range(9):
        frm_cell = tk.Frame(blocks[i // 3][j // 3])
        frm_cell.grid(row=(i % 3), column=(j % 3), sticky='nsew')
        frm_cell.rowconfigure(0, minsize=50, weight=1)
        frm_cell.columnconfigure(0, minsize=50, weight=1)
        var = tk.StringVar()
        btn_cells[i][j] = tk.Button(frm_cell, relief='ridge', bg='white', textvariable=var)
        btn_cells[i][j].grid(sticky='nsew')
        for s in solution:
            var.set(solution[i][j])

root.mainloop()