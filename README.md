# Profit Analysis and Break-Even Simulation

A Python-based microeconomic tool that computes a firm's **economic profit** across increasing output levels and identifies the **break-even point (Qe)** where profit becomes zero or positive. Designed for applied economics, academic work, and quantitative modeling.

---

## 📌 Project Overview

This simulation allows you to:

- Evaluate economic profit for a competitive firm.  
- Identify the exact break-even output level.  
- Observe how losses decrease as production rises.  
- Understand core microeconomic logic through computation.  

Ideal for students, researchers, and anyone building an economics portfolio.

---

## 🔍 Economic Background

### **Total Revenue (TR)**  
TR = Price × Quantity  

### **Total Cost (TC)**  
TC = Fixed Cost + (Unit Variable Cost × Quantity)  

### **Profit Function (π)**  
π = TR − TC  

The break-even point occurs when:  
**π = 0**, meaning revenue exactly covers total cost.

This script iterates over increasing quantities until the condition is met, making the concept highly intuitive.

---

## 📂 File Structure

profit_breakeven_analysis.py # Main simulation script
README.md # Documentation
LICENSE # MIT License
.gitignore # Python ignore rules

yaml
Copiar código

---

## ▶️ How to Run the Script

1. Install **Python 3.8+**  
2. Run:

```bash
python profit_breakeven_analysis.py
Enter the required inputs:

Unit price

Total fixed cost (FC)

Unit variable cost (UVC)

The program will automatically evaluate profit from Q = 1 upward until the break-even point is reached.

📊 Sample Output
markdown
Copiar código
Q =   1 → Economic Profit (π) = -45.00
----------------------------------------------
Q =   2 → Economic Profit (π) = -30.00
----------------------------------------------
Q =   3 → Economic Profit (π) = -15.00
----------------------------------------------
Q =   4 → Economic Profit (π) =   0.00

🔹 Break-even point reached or exceeded.
🔸 Break-even quantity (Qe) ≈ 4
🔸 Profit at break-even: 0.00
🧠 Interpretation
When output is low, fixed costs dominate, leading to economic losses.

As Q increases, losses shrink until hitting Qe, where the firm breaks even.

Any output level above Qe generates positive economic profit.

This mirrors the real behavior of firms operating under competitive market conditions.

🛠 Technologies Used
Python 3

Iterative computation

Microeconomic modeling

Console-based economic diagnostics

📜 License
This project is distributed under the MIT License.
You are free to use, modify, and distribute it with proper attribution.

👤 Author
Kevin Adolfo Lorenzo Condor
Economist in training | Applied Microeconomics & Python
GitHub: KLorenzoEconomics

