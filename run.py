import sys, os
import subprocess
import tkinter as tk
from tkinter import ttk
import backend

# Define your variables
DIR = os.path.dirname(__file__)
ANTLR_JAR = 'C:/JavaLib/antlr4-4.9.2-complete.jar'
CPL_Dest = 'CompiledFiles'
SRC = 'PropositionalLogic.g4'

class PropositionalLogicEvaluator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Propositional Logic Evaluator")
        self.window.geometry("900x700")
        self.window.resizable(False, False)

        main_frame = ttk.Frame(self.window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Expression input row
        input_row = ttk.Frame(main_frame)
        input_row.pack(anchor=tk.W, pady=(0, 10))
        ttk.Label(input_row, text="Expression:").pack(side=tk.LEFT)
        self.expr_entry = ttk.Entry(input_row, width=50, font=("Consolas", 14))
        self.expr_entry.pack(side=tk.LEFT, padx=(10, 0))

        # Checkbox row
        self.calc_forms_var = tk.BooleanVar()
        forms_row = ttk.Frame(main_frame)
        forms_row.pack(anchor=tk.W, pady=(0, 10))
        self.forms_checkbox = ttk.Checkbutton(forms_row, text="Calculate the forms?", variable=self.calc_forms_var)
        self.forms_checkbox.pack(side=tk.LEFT)

        # Operator buttons grid
        op_frame = ttk.Frame(main_frame)
        op_frame.pack(pady=(0, 10))
        op_buttons = [
            ("~, not", "~"), ("&, and", "&"), ("|, or", "|"), ("^, nand", "^"), ("*, nor", "*")
        ]
        for i, (label, symbol) in enumerate(op_buttons):
            btn = tk.Button(op_frame, text=label, width=10, bg='#b3e0ff', fg='black', activebackground='#99d6ff', command=lambda s=symbol: self.insert_operator(s))
            btn.grid(row=0, column=i, padx=2, pady=2)

        # Calculate, Check Grammar, and Clear All buttons
        btn_row = ttk.Frame(main_frame)
        btn_row.pack(pady=(0, 10))
        tk.Button(btn_row, text="CALCULATE", command=self.evaluate_expression, width=20, bg='#4CAF50', fg='white', activebackground='#45a049').pack(side=tk.LEFT, padx=10)
        tk.Button(btn_row, text="CHECK GRAMMAR", command=self.check_grammar, width=20, bg='#2196F3', fg='white', activebackground='#1976D2').pack(side=tk.LEFT, padx=10)
        tk.Button(btn_row, text="CLEAR ALL", command=self.clear_all, width=20, bg='#f44336', fg='white', activebackground='#da190b').pack(side=tk.LEFT, padx=10)

        # Result/Truth Table area
        ttk.Label(main_frame, text="ANSWER", font=("Arial", 16, "bold"), foreground="#2a7f62").pack(pady=(10, 0))
        self.table_frame = ttk.Frame(main_frame)
        self.table_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        self.table = None

    def insert_operator(self, symbol):
        self.expr_entry.insert(tk.INSERT, symbol)

    def clear_all(self):
        self.expr_entry.delete(0, tk.END)
        for widget in self.table_frame.winfo_children():
            widget.destroy()

    def evaluate_expression(self):
        expr = self.expr_entry.get().strip()
        if not expr:
            self.show_message("Please enter an expression")
            return
        try:
            variables, results = backend.generate_truth_table(expr)
        except Exception as e:
            self.show_message(f"Error: {e}")
            return
        self.display_table(variables, results, expr)

    def check_grammar(self):
        expr = self.expr_entry.get().strip()
        if not expr:
            self.show_message("Please enter an expression")
            return
        is_valid, error = backend.check_grammar(expr)
        if is_valid:
            self.show_message("Grammar is valid!", color="green")
        else:
            self.show_message("Grammar is invalid!")

    def show_message(self, msg, color="red"):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        label = ttk.Label(self.table_frame, text=msg, foreground=color, font=("Arial", 12))
        label.pack()

    def display_table(self, variables, results, expr):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        columns = variables + [expr]
        n_rows = len(results) + 1
        n_cols = len(columns)
        cell_font = ("Arial", 12)
        header_font = ("Arial", 12, "bold")
        # Create header row
        for j, col in enumerate(columns):
            bg = '#ffe066' if j < len(variables) else '#b6fcd5'
            label = tk.Label(self.table_frame, text=col, bg=bg, fg='black', font=header_font, width=7, height=1, borderwidth=1, relief="solid", anchor='center')
            label.grid(row=0, column=j, sticky='nsew', padx=0, pady=0)
        # Create data rows
        for i, row in enumerate(results):
            for j, val in enumerate(row):
                bg = 'white'
                label = tk.Label(self.table_frame, text=val, bg=bg, fg='black', font=cell_font, width=7, height=1, borderwidth=1, relief="solid", anchor='center')
                label.grid(row=i+1, column=j, sticky='nsew', padx=0, pady=0)
        # Make columns expand equally
        for j in range(n_cols):
            self.table_frame.grid_columnconfigure(j, weight=1)
        for i in range(n_rows):
            self.table_frame.grid_rowconfigure(i, weight=1)

    def run(self):
        self.window.mainloop()

def generateAntlr2Python():
    print('Antlr4 is running...')
    subprocess.run(['java', '-jar', ANTLR_JAR, '-o', CPL_Dest, '-no-listener', '-Dlanguage=Python3', SRC])
    print('Generate successfully')

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))    
    
    if len(argv) < 1:
        print("Usage: python run.py [gen|run]")
    elif argv[0] == 'gen':
        generateAntlr2Python()    
    elif argv[0] == 'run':       
        evaluator = PropositionalLogicEvaluator()
        evaluator.run()
    else:
        print("Usage: python run.py [gen|run]")

if __name__ == '__main__':
    main(sys.argv[1:])     
    
    