import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("450x500")  

        self.result_var = tk.StringVar()

        self.configure(bg="#f0f0f0")  # Set background color for the window

        self.create_widgets()

    def create_widgets(self):
        
        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, bg="#fff", fg="#333")  # Set background and foreground colors for the entry
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10) 

       
        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("+", 4, 2),
            ("=", 4, 3),
            ("C", 5, 0),   
            ("<-", 5, 1)   
        ]

        for (text, row, col) in buttons:
            if text.isdigit():
                bg_color = "grey" 
            elif text in "+-*/.":
                bg_color = "green" 
            else:
                bg_color = "red"  
                
            button = tk.Button(self, text=text, font=("Arial", 18), width=5, height=2, command=lambda t=text: self.on_button_click(t), bg=bg_color, fg="#333", activebackground="#ccc", activeforeground="#000")  # Set background, foreground, and active colors for the button
            button.grid(row=row, column=col, padx=5, pady=5)  

    def on_button_click(self, text):
        if text == "=":
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif text == "C":
            self.result_var.set("")
        elif text == "<-":
            current_text = self.result_var.get()
            new_text = current_text[:-1]
            self.result_var.set(new_text)
        else:
            current_text = self.result_var.get()
            new_text = current_text + text
            self.result_var.set(new_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
