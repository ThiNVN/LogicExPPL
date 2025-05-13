import tkinter as tk
from tkinter import ttk, messagebox
from backend import check_grammar, generate_truth_table

class LogicExpressionCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Logic Expression Calculator")
        self.root.geometry("800x600")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Expression input
        ttk.Label(main_frame, text="Enter Logic Expression:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.expression_var = tk.StringVar()
        self.expression_entry = ttk.Entry(main_frame, textvariable=self.expression_var, width=50)
        self.expression_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Check Grammar", command=self.check_grammar).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Calculate", command=self.calculate).pack(side=tk.LEFT, padx=5)
        
        # Truth table
        ttk.Label(main_frame, text="Truth Table:").grid(row=3, column=0, sticky=tk.W, pady=5)
        
        # Create Treeview for truth table
        self.tree = ttk.Treeview(main_frame, columns=(), show='headings')
        self.tree.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.grid(row=4, column=2, sticky=(tk.N, tk.S))
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
    def check_grammar(self):
        expression = self.expression_var.get()
        if not expression:
            messagebox.showwarning("Warning", "Please enter an expression")
            return
            
        is_valid, message = check_grammar(expression)
        if is_valid:
            messagebox.showinfo("Grammar Check", message)
            self.status_var.set("Expression is valid")
        else:
            messagebox.showerror("Grammar Error", message)
            self.status_var.set("Invalid expression")
    
    def calculate(self):
        expression = self.expression_var.get()
        if not expression:
            messagebox.showwarning("Warning", "Please enter an expression")
            return
            
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Get truth table
        variables, results = generate_truth_table(expression)
        
        if not variables:
            messagebox.showerror("Error", "Invalid expression or no variables found")
            self.status_var.set("Calculation failed")
            return
            
        # Configure columns
        self.tree['columns'] = variables + ['Result']
        for col in self.tree['columns']:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor=tk.CENTER)
            
        # Insert data
        for row in results:
            self.tree.insert('', tk.END, values=row)
            
        self.status_var.set("Calculation completed")

def main():
    root = tk.Tk()
    app = LogicExpressionCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 