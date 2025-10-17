
# MindArena: AI Model Showdown — GPT-4o-mini vs Gemini-1.5-flash

[![](https://img.shields.io/badge/license-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![](https://img.shields.io/badge/python-3.10+-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/badge/UI-Tkinter-00599C.svg?style=for-the-badge&logo=windowsterminal&logoColor=white)](#)
[![](https://img.shields.io/badge/AI_Models-GPT4o__mini_&_Gemini__1.5__flash-ff6f00.svg?style=for-the-badge&logo=googlecloud&logoColor=white)](#)
[![](https://img.shields.io/badge/threading-real_time_moves-00B8A9.svg?style=for-the-badge)](#)

---

## AI Battle Visualization


<img alt="AI Battle Visualization" src="battle.gif"></img>

---

## Project Insight

**MindArena** is a real-time AI-versus-AI simulation where **GPT-4o-mini** and **Gemini-1.5-flash** compete in a logic-driven Tic-Tac-Toe battle.
The project explores **model reasoning, speed, and tactical awareness** under identical prompt conditions, offering a transparent look into LLM strategic behavior.

---

## Why This Project Exists

The idea behind MindArena was to move beyond text generation and visualize **strategic decision-making in constrained environments**.
Tic-Tac-Toe provides a clean, interpretable framework to study **how models reason, adapt, and optimize** within deterministic rules.

---

## Architecture & Technologies

| Component    | Technology           | Purpose                                           |
| ------------ | -------------------- | ------------------------------------------------- |
| GUI          | Tkinter              | Displays the interactive board and move tracking. |
| Logic Engine | Custom Python Module | Enforces rules and evaluates outcomes.            |
| AI Bridge    | `ai_brain.py`        | Handles model requests and response parsing.      |
| Concurrency  | Threading            | Simulates simultaneous AI decisions.              |
| Environment  | Python 3.10+         | Core runtime for the experiment.                  |

---

## Run It Locally

Clone and start the project in your environment:

```bash
git clone https://github.com/YourUsername/MindArena.git
cd MindArena
python3 main.py
```

If using API-based models, configure credentials inside `config.py`.

---

## Key Takeaways

* Real-time, neutral AI competition with equal prompts.
* Visual demonstration of reasoning speed and move quality.
* Simple framework for benchmarking conversational or logic-based AI models.

Initial experiments showed **GPT-4o-mini** achieving higher consistency in tactical responses compared to **Gemini-1.5-flash**.

---

## Roadmap

* Web dashboard for model analytics and replay visualization.
* Support for additional strategy games (e.g., Connect-Four, Gomoku).
* API layer for automated AI tournaments and benchmarking.

---

**Keywords:** AI Benchmarking, Model Evaluation, GPT-4o-mini, Gemini-1.5-flash, Python, Threading, Tkinter, LLM Strategy, Real-time Simulation
