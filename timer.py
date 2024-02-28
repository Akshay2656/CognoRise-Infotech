import tkinter as tk
from tkinter import messagebox
import time
import random

class CountdownApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")
        self.master.geometry("500x500")
        
        self.master.configure(bg="black")
    
        self.frame = tk.Frame(master, bg="#FF0000")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.label_instruction = tk.Label(self.frame, text="Enter the time:", font=("Helvetica", 16), bg="#FF0000", fg="white")
        self.label_instruction.grid(row=0, column=0, pady=10)
        
        self.frame_time_input = tk.Frame(self.frame, bg="#FF0000")
        self.frame_time_input.grid(row=1, column=0)
        
        self.label_hours = tk.Label(self.frame_time_input, text="Hours:", font=("Helvetica", 14), bg="#FF0000", fg="white")
        self.label_hours.grid(row=0, column=0, padx=5, pady=5)
        self.entry_hours = tk.Entry(self.frame_time_input, font=("Helvetica", 14))
        self.entry_hours.grid(row=0, column=1, padx=5, pady=5)
        
        self.label_minutes = tk.Label(self.frame_time_input, text="Minutes:", font=("Helvetica", 14), bg="#FF0000", fg="white")
        self.label_minutes.grid(row=1, column=0, padx=5, pady=5)
        self.entry_minutes = tk.Entry(self.frame_time_input, font=("Helvetica", 14))
        self.entry_minutes.grid(row=1, column=1, padx=5, pady=5)
        
        self.label_seconds = tk.Label(self.frame_time_input, text="Seconds:", font=("Helvetica", 14), bg="#FF0000", fg="white")
        self.label_seconds.grid(row=2, column=0, padx=5, pady=5)
        self.entry_seconds = tk.Entry(self.frame_time_input, font=("Helvetica", 14))
        self.entry_seconds.grid(row=2, column=1, padx=5, pady=5)
        
        self.button_start = tk.Button(self.frame, text="Start", font=("Helvetica", 16), bg="#4CAF50", fg="white", command=self.start_countdown)
        self.button_start.grid(row=2, column=0, pady=20)
        
        self.label_timer = tk.Label(self.frame, text="", font=("Helvetica", 48), bg="#FF0000", fg="white")
        self.label_timer.grid(row=3, column=0)
       
        self.change_label_color()
    
    def start_countdown(self):
        try:
            hours = int(self.entry_hours.get())
            minutes = int(self.entry_minutes.get())
            seconds = int(self.entry_seconds.get())
            total_seconds = hours * 3600 + minutes * 60 + seconds
            if total_seconds <= 0:
                raise ValueError("Please enter a positive time.")
            
            self.run_countdown(total_seconds)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def run_countdown(self, countdown_t):
        if countdown_t >= 0:
            hours, remainder = divmod(countdown_t, 3600)
            minutes, seconds = divmod(remainder, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
            self.label_timer.config(text=timer)
            self.master.update()
            self.master.after(1000, lambda: self.run_countdown(countdown_t - 1))
        else:
            messagebox.showinfo("Countdown Complete", "Done!")
    
    def change_label_color(self):
        colors = ['#FF0000', '#FF7F00', '#FFFF00', '#00FF00', '#0000FF', '#4B0082', '#9400D3']
        random.shuffle(colors)
        for color in colors:
            self.label_timer.config(fg=color)
            self.master.update()
            time.sleep(1)

def main():
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
