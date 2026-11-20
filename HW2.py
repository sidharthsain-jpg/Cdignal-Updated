"""A simple Rock–Paper–Scissors game built with Tkinter."""

import random
import tkinter as tk
from tkinter import ttk


CHOICES = ("Rock", "Paper", "Scissors")


class RockPaperScissors:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.root.resizable(False, False)
        self.root.configure(bg="#f3f5f9")

        self.player_score = 0
        self.computer_score = 0
        self.ties = 0

        style = ttk.Style()
        style.configure("Title.TLabel", font=("TkDefaultFont", 20, "bold"))
        style.configure("Result.TLabel", font=("TkDefaultFont", 13))
        style.configure("Score.TLabel", font=("TkDefaultFont", 12, "bold"))
        style.configure("Choice.TButton", font=("TkDefaultFont", 12), padding=10)

        frame = ttk.Frame(root, padding=24)
        frame.grid()

        ttk.Label(frame, text="Rock Paper Scissors", style="Title.TLabel").grid(
            row=0, column=0, columnspan=3, pady=(0, 8)
        )
        ttk.Label(frame, text="Choose your move:", style="Result.TLabel").grid(
            row=1, column=0, columnspan=3, pady=(0, 12)
        )

        for column, choice in enumerate(CHOICES):
            ttk.Button(
                frame,
                text=choice,
                style="Choice.TButton",
                command=lambda move=choice: self.play(move),
            ).grid(row=2, column=column, padx=5)

        self.result_label = ttk.Label(
            frame,
            text="Your move and the computer's move will appear here.",
            style="Result.TLabel",
            justify="center",
            wraplength=360,
        )
        self.result_label.grid(row=3, column=0, columnspan=3, pady=20)

        self.score_label = ttk.Label(frame, style="Score.TLabel")
        self.score_label.grid(row=4, column=0, columnspan=3, pady=(0, 16))
        self.update_score()

        ttk.Button(frame, text="Reset score", command=self.reset).grid(
            row=5, column=0, columnspan=3
        )

    def play(self, player_move: str) -> None:
        computer_move = random.choice(CHOICES)

        if player_move == computer_move:
            outcome = "It's a tie!"
            self.ties += 1
        elif (
            (player_move == "Rock" and computer_move == "Scissors")
            or (player_move == "Paper" and computer_move == "Rock")
            or (player_move == "Scissors" and computer_move == "Paper")
        ):
            outcome = "You win this round!"
            self.player_score += 1
        else:
            outcome = "The computer wins this round."
            self.computer_score += 1

        self.result_label.config(
            text=f"You chose {player_move}. The computer chose {computer_move}.\n{outcome}"
        )
        self.update_score()

    def update_score(self) -> None:
        self.score_label.config(
            text=(
                f"You: {self.player_score}     "
                f"Computer: {self.computer_score}     "
                f"Ties: {self.ties}"
            )
        )

    def reset(self) -> None:
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.result_label.config(text="Score reset. Choose your next move!")
        self.update_score()


def main() -> None:
    root = tk.Tk()
    RockPaperScissors(root)
    root.mainloop()


if __name__ == "__main__":
    main()