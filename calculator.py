import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.result_var = tk.StringVar()

        self.entry = tk.Entry(master, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            if button == '=':
                btn = tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18), command=self.calculate)
            else:
                btn = tk.Button(self.master, text=button, padx=20, pady=20, font=('Arial', 18), command=lambda b=button: self.append_to_expression(b))
            btn.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        clear_button = tk.Button(self.master, text='C', padx=20, pady=20, font=('Arial', 18), command=self.clear)
        clear_button.grid(row=row_val, column=0, columnspan=4)

    def append_to_expression(self, value):
        current_expression = self.result_var.get()
        new_expression = current_expression + str(value)
        self.result_var.set(new_expression)

    def calculate(self):
        try:
            result = eval(self.result_var.get())
            self.result_var.set(result)
        except Exception as e:
            self.result_var.set("Error")

    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
