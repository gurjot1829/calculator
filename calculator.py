import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Calculator")

        self.entry = tk.Entry(master, width=20, font=("Arial", 16), bd=5)
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row_index = 1
        col_index = 0

        for button in buttons:
            tk.Button(master, text=button, width=5, height=2, font=("Arial", 16),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_index, column=col_index)
            col_index += 1
            if col_index > 3:
                col_index = 0
                row_index += 1

    def on_button_click(self, text):
        if text == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, text)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
