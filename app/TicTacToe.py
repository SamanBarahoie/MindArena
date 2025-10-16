# app/main.py
import tkinter as tk
from tkinter import messagebox
import threading
import time
from ai_brain import AIBrain  # make sure this exists

# -------------------------
# Main UI class
# -------------------------
class MindArena:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("MindArena - GPT-4 vs Gemini")
        self.window.geometry("420x520")
        self.window.configure(bg="#1E1E2E")

        # Game state
        self.board = [""] * 9
        self.buttons = []
        self.current_player = "X"
        self.running = False

        # Score tracking
        self.scores = {"X": 0, "O": 0, "Ties": 0}

        # AI agents
        self.agent_x = AIBrain("Agent-X (GPT-4o-mini)", "X")
        self.agent_o = AIBrain("Agent-O (Gemini)", "O")

        self.font = ("Segoe UI", 18, "bold")
        self.colors = {
            "X": "#00D1FF",
            "O": "#FFC300",
            "bg": "#1E1E2E",
            "button": "#2A2A3C",
            "highlight": "#80FF80",
            "text": "#E9ECEF"
        }

        self.create_header()
        self.create_board()
        self.create_controls()
        self.create_scoreboard()

    def create_header(self):
        tk.Label(
            self.window,
            text="MindArena: GPT-4 vs Gemini",
            font=("Segoe UI", 16, "bold"),
            fg="#00D1FF",
            bg=self.colors["bg"]
        ).pack(pady=10)

        self.turn_label = tk.Label(
            self.window,
            text="Ready for Battle!",
            font=("Segoe UI", 13),
            fg=self.colors["text"],
            bg=self.colors["bg"]
        )
        self.turn_label.pack(pady=5)

    def create_board(self):
        board_frame = tk.Frame(self.window, bg=self.colors["bg"])
        board_frame.pack(pady=10)

        for i in range(9):
            btn = tk.Button(
                board_frame, text="", font=self.font, width=4, height=2,
                bg=self.colors["button"], fg=self.colors["text"], relief="flat", bd=0, state="disabled"
            )
            btn.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            self.buttons.append(btn)

    def create_controls(self):
        frame = tk.Frame(self.window, bg=self.colors["bg"])
        frame.pack(pady=8)

        tk.Button(
            frame, text="▶ Start Battle", font=("Segoe UI", 11, "bold"),
            bg="#00D1FF", fg="black", activebackground="#0BC0E0",
            command=self.start_battle
        ).grid(row=0, column=0, padx=8)

        tk.Button(
            frame, text="🔄 Reset", font=("Segoe UI", 11, "bold"),
            bg="#FFC300", fg="black", activebackground="#E0B000",
            command=self.reset_game
        ).grid(row=0, column=1, padx=8)

    def create_scoreboard(self):
        self.score_frame = tk.Frame(self.window, bg=self.colors["bg"])
        self.score_frame.pack(pady=8)
        self.update_scoreboard()

    def update_scoreboard(self):
        for widget in self.score_frame.winfo_children():
            widget.destroy()

        tk.Label(self.score_frame, text=f"X: {self.scores['X']}", font=("Segoe UI", 11),
                 fg=self.colors["X"], bg=self.colors["bg"]).grid(row=0, column=0, padx=20)
        tk.Label(self.score_frame, text=f"Ties: {self.scores['Ties']}", font=("Segoe UI", 11),
                 fg="#CED4DA", bg=self.colors["bg"]).grid(row=0, column=1, padx=20)
        tk.Label(self.score_frame, text=f"O: {self.scores['O']}", font=("Segoe UI", 11),
                 fg=self.colors["O"], bg=self.colors["bg"]).grid(row=0, column=2, padx=20)

    def start_battle(self):
        if not self.running:
            for b in self.buttons:
                b.config(state="normal")
            self.running = True
            self.turn_label.config(text="Battle Started ⚔️")
            threading.Thread(target=self.run_game, daemon=True).start()

    def run_game(self):
        while not self.check_winner() and "" in self.board:
            current_agent = self.agent_x if self.current_player == "X" else self.agent_o
            self.turn_label.config(text=f"{current_agent.name}'s Move...")
            self.window.update_idletasks()

            move = current_agent.get_move(self.board)
            if move is not None and self.board[move] == "":
                time.sleep(1.2)
                self.make_move(move, self.current_player)

            if self.check_winner():
                self.turn_label.config(text=f"{current_agent.name} Wins! 🏆")
                self.highlight_winner()
                self.scores[self.current_player] += 1
                break

            if "" not in self.board:
                self.turn_label.config(text="It's a Draw! 🤝")
                self.scores["Ties"] += 1
                break

            self.current_player = "O" if self.current_player == "X" else "X"

        self.running = False
        self.update_scoreboard()

    def make_move(self, index, player):
        self.board[index] = player
        emoji = "❌" if player == "X" else "⭕"
        self.buttons[index].config(text=emoji, font=("Segoe UI", 26), fg=self.colors[player], state="disabled")

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for cond in win_conditions:
            if self.board[cond[0]] == self.board[cond[1]] == self.board[cond[2]] != "":
                self.winning_combo = cond
                return True
        return False

    def highlight_winner(self):
        for i in self.winning_combo:
            self.buttons[i].config(bg=self.colors["highlight"])

    def reset_game(self):
        self.board = [""] * 9
        for b in self.buttons:
            b.config(image="", text="", bg=self.colors["button"], state="disabled")
        self.current_player = "X"
        self.turn_label.config(text="Ready for Battle!")
        self.running = False

    def run(self):
        self.window.mainloop()


# ---- entrypoint
if __name__ == "__main__":
    MindArena().run()
