
# MindArena: AI Tic-Tac-Toe Battle

[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![](https://img.shields.io/github/v/release/SamanBarahoie/MindArena?color=green)](https://github.com/SamanBarahoie/MindArena/releases)
[![](https://img.shields.io/github/actions/workflow/status/SamanBarahoie/MindArena/ci.yml?branch=main)](https://github.com/SamanBarahoie/MindArena/actions)
[![](https://img.shields.io/badge/python-3.10+-yellow.svg)](https://www.python.org/downloads/)
[![](https://img.shields.io/badge/AI-Model_Comparison-orange.svg)](https://yourprojectdomain.com/docs)

## Screenshot


<image-card alt="AI Battle Screenshot" src="battle.gif"></image-card>


Optional badges below the screenshot (customize URLs as needed): <img src="https://img.shields.io/badge/demo-live-blueviolet.svg" alt=""> <img src="https://img.shields.io/badge/docs-Overview-orange.svg" alt=""> <img src="https://img.shields.io/github/stars/YourUsername/MindArena?style=social" alt="">

---

## Overview

**MindArena** is an AI-driven Tic-Tac-Toe arena designed to benchmark and visualize real-time decision-making between two leading models — **GPT-4o-mini** and **Gemini-1.5-flash**.
The system provides an interactive interface that highlights model reasoning speed, move precision, and strategic behavior in a controlled environment.

---

## Motivation

The project was built to explore how modern large language models handle **symbolic reasoning and deterministic games**.
By creating a neutral and repeatable environment, MindArena demonstrates the competitive and analytical capabilities of AI models in lightweight, interpretable settings.

---

## Architecture & Technologies

The system employs a simple but modular design to allow model substitution and scalable comparison.

| Component  | Technology                | Purpose                                                         |
| ---------- | ------------------------- | --------------------------------------------------------------- |
| Interface  | Tkinter                   | Visualizes the game and player turns.                           |
| AI Engine  | Python Threads            | Manages real-time model decisions.                              |
| AI Bridge  | `ai_brain.py`             | Unifies communication between GPT-4o-mini and Gemini-1.5-flash. |
| Logic Core | Custom Tic-Tac-Toe Engine | Ensures fairness and deterministic rule enforcement.            |

---

## Installation & Usage

Clone and set up the project locally:

```bash
git clone https://github.com/YourUsername/MindArena.git
cd MindArena
python3 Tic-Tac-Toe.py
```

Ensure you have valid API keys (if applicable) for both models defined in `config.py`.

---

## Outcomes & Impact

MindArena highlights:

* Consistent model benchmarking under equal prompt conditions.
* Real-time move tracking with live win/draw statistics.
* A reproducible setup for small-scale AI competition experiments.

The results showed **GPT-4o-mini** performing with greater consistency and tactical efficiency compared to Gemini-1.5-flash.

---

## Future Enhancements

Planned improvements include:

* Web-based dashboard for multi-model comparison.
* Support for turn-based strategy games beyond Tic-Tac-Toe.
* Integration with OpenAI and Google API monitoring for deeper metrics.

---

**Keywords:** AI, Model Evaluation, GPT-4o-mini, Gemini-1.5-flash, Python, Tic-Tac-Toe, Benchmarking, Strategy Simulation
