import tkinter as tk
import re
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Pro Calculator")
        master.geometry("360x500")
        master.resizable(False, False)
        master.configure(bg="#4b7fa4")

        self.equation = ""

        # Screen
        self.entry = tk.Entry(master, font=("Times", 20),
                              bg="#fcfcec", fg="black",
                              justify="right", bd=10)
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # Buttons
        buttons = [
            '7','8','9','÷',
            '4','5','6','×',
            '1','2','3','-',
            '0','.','=','+',
            'C'
        ]

        frame = tk.Frame(master, bg="#4b7fa4")
        frame.pack()

        row = 0
        col = 0

        for btn in buttons:
            tk.Button(frame, text=btn,
                      font=("Times", 20),
                      width=5, height=2,
                      bg="#2c3e50", fg="white",
                      command=lambda b=btn: self.click(b)).grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, value):
        if value == "C":
            self.equation = ""
            self.entry.delete(0, tk.END)

        elif value == "=":
            try:
                # FIX: re import required (NOW ADDED ABOVE)
                self.equation = self.entry.get()

                self.equation = self.equation.replace("×", "*")
                self.equation = self.equation.replace("÷", "/")

                result = eval(self.equation)

                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
                self.equation = str(result)

            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                self.equation = ""

        else:
            self.equation += str(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.equation)


# Run app
root = tk.Tk()
calc = Calculator(root)
root.mainloop()