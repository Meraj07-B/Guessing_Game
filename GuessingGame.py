import tkinter as tk
from tkinter import ttk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Guessing Game")
        master.geometry("400x350")
        master.configure(bg="#e6f7ff")

        self.random_number = random.randint(1, 10)
        self.attempts = 0

        # Style
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12, "bold"), padding=10)
        style.map("TButton", foreground=[('active', '#0059b3')], background=[('active', '#66b3ff')])

        # Title
        self.title_label = tk.Label(master, text="🎯 Guess the Number!", font=("Helvetica", 18, "bold"), bg="#e6f7ff", fg="#0059b3")
        self.title_label.pack(pady=20)

        # Instructions Label
        self.instructions_label = tk.Label(master, text="I'm thinking of a number between 1 and 10.\nCan you guess it?", font=("Helvetica", 12), bg="#e6f7ff", fg="#0059b3")
        self.instructions_label.pack(pady=10)

        # Entry Frame for corners
        self.entry_frame = tk.Frame(master, bg="#e6f7ff", padx=5, pady=5)
        self.entry_frame.pack(pady=10)

        # Entry for Guess
        self.guess_entry = tk.Entry(self.entry_frame, font=("Helvetica", 14), width=10, justify='center', bd=2, relief="groove")
        self.guess_entry.pack(ipady=5)

        # Submit Button
        self.submit_button = ttk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack(pady=10)

        # Feedback Label
        self.feedback_label = tk.Label(master, text="", font=("Helvetica", 12), bg="#e6f7ff")
        self.feedback_label.pack(pady=10)

        # Attempts Label
        self.attempts_label = tk.Label(master, text="Attempts: 0", font=("Helvetica", 12), bg="#e6f7ff", fg="#0059b3")
        self.attempts_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!", fg="red")
            return

        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        if guess < self.random_number:
            self.feedback_label.config(text="Too low! Try again.", fg="#ff6666")
        elif guess > self.random_number:
            self.feedback_label.config(text="Too high! Try again.", fg="#ff6666")
        else:
            self.feedback_label.config(text=f"🎉 Congratulations! You guessed it in {self.attempts} attempts!", fg="#33cc33")
            self.submit_button.config(state="disabled")


root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
