# Blackjack Game 🎲  

A Python implementation of the classic **Blackjack (21)** card game, built as the **Day 11 Capstone** from Angela Yu’s *100 Days of Code: Python Bootcamp*.  

## 📌 Features  
- Player vs Computer (Dealer) gameplay.  
- Dealer automatically draws until reaching a score of ≥17.  
- Ace (`11`) adjusts to `1` when total score exceeds 21.  
- Detects **Blackjack** (Ace + 10 in the first two cards).  
- ASCII art logo for a polished feel.  
- Replay option to keep playing multiple rounds.  

## 🎮 Game Rules  
1. Both player and dealer start with 2 cards.  
2. Player chooses to **Hit** (draw another card) or **Stand** (end turn).  
3. If the player’s score > 21 → **Bust** (lose immediately).  
4. If the player stands, the dealer draws until their score is ≥ 17.  
5. Closest to 21 without going over wins.  
6. Natural Blackjack (Ace + 10 on first two cards) beats any other 21.  

## ▶️ How to Run  
Clone the repo and run:  
```bash
python main.py
