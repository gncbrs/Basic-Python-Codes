import tkinter as tk
import random
import time

def roll_dice():
    roll_button.config(state="disabled")
    result_label.config(text="Rolling...")

    def update_roll():
        end_time = time.time() + 3  
        def rolling():
            if time.time() < end_time:
                number = random.randint(1, 6)
                result_label.config(text=f"The number: {number}")
                root.after(100, rolling)
            else:
                final_number = random.randint(1, 6)
                result_label.config(text=f"The number: {final_number}")
                roll_button.config(state="normal")
        
        rolling()

    root.after(100, update_roll)

def exit_program():
    root.destroy()

root = tk.Tk()
root.title("Dice Roller Simulator")
root.geometry("300x250")
root.resizable(False, False)

title_label = tk.Label(root, text="🎲 Dice Roller 🎲", font=("Arial", 16))
title_label.pack(pady=10)

result_label = tk.Label(root, text="Press Roll!", font=("Arial", 14))
result_label.pack(pady=10)

roll_button = tk.Button(root, text="Roll Dice", command=roll_dice, font=("Arial", 12))
roll_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_program, font=("Arial", 12))
exit_button.pack(pady=5)

root.mainloop()
