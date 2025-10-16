# app/ai_brain.py
import random
from llm_agent import LLMHelper
from config import MODEL_AGENT_X, MODEL_AGENT_O


class AIBrain:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

        self.model = MODEL_AGENT_X if symbol == "X" else MODEL_AGENT_O
        self.llm = LLMHelper(self.model)

    def get_move(self, board_state):
        prompt = f"""
        You are player '{self.symbol}' in Tic-Tac-Toe.
        The board is represented as a list of 9 cells: {board_state}
        Choose your next move wisely (0–8).
        Respond with ONLY the number of the cell you want to play.
        """

        response = self.llm.generate_text(prompt)
        try:
            move = int(''.join(filter(str.isdigit, response)))
            if move in range(9) and board_state[move] == "":
                return move
        except:
            pass

        # fallback in case model output is invalid
        empty_cells = [i for i, v in enumerate(board_state) if v == ""]
        return random.choice(empty_cells) if empty_cells else None
