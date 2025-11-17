# **Break-Even Profit Analysis — Microeconomic Simulation in Python**

A computational microeconomic engine that models how a competitive firm transitions from loss to profitability.  
This project simulates economic profit dynamically across output levels, identifying the exact break-even quantity where π = 0 and profitability emerges.  
Designed for economists, analysts, and students who want clean, reproducible, and theory-consistent results.

---

## 🚀 **Project Purpose**
This simulation is built to:

- Compute economic profit (π) across increasing output levels Q.  
- Identify the **break-even point (Qe)** through iterative evaluation.  
- Provide a transparent and mathematically rigorous model of firm behavior under perfect competition.  
- Serve as a ready-to-run tool for **teaching, research, or applied economic analysis**.

---

## 📘 **Economic Foundations**

### **Profit Function (π):**  
```math
\pi(Q) = P \cdot Q - [CF + CV_u \cdot Q]
Where:

P → Unit price

CF → Total fixed cost

CVu → Unit variable cost

Q → Output

A firm in perfect competition faces a constant price and produces until losses vanish and profit begins to rise.
This script reveals that transition step-by-step.

🧮 How the Simulation Works
The program:

Requests key economic inputs:

Unit price (P)

Total fixed cost (CF)

Unit variable cost (CVu)

Iteratively increases output Q = 1, 2, 3…

Calculates:

Total revenue

Total cost

Economic profit (π)

Stops once:

𝜋
(
𝑄
)
≥
0
π(Q)≥0
Prints the exact break-even quantity (Qe).

📊 Sample Output
java
Copiar código
Q =   1 → Economic Profit (π) = -45.00
Q =   2 → Economic Profit (π) = -15.00
Q =   3 → Economic Profit (π) =   5.00

🔹 Break-even reached.
🔸 Break-even quantity (Qe): 3
🔸 Profit at Qe: 5.00
🧠 Interpretation
As output increases, the firm spreads fixed costs over more units, shrinking initial losses.
Once marginal revenue equals marginal cost and fixed costs are covered, the firm reaches break-even—the threshold between loss and profitability.

This model illustrates:

Cost dilution

Profit transition

Competitive firm behavior

Fundamental microeconomic dynamics

▶️ How to Run
Install Python 3.8+

Run the script:

bash
Copiar código
python break_even_profit_analysis.py
Enter the requested economic parameters.

Observe the real-time profit evolution.

🛠️ Technologies
Python 3

Fundamental arithmetic modeling

Input-based parameterization

Iterative computation

📄 License
This project is under the MIT License.
Feel free to use, modify, or extend it with attribution.

👤 Author
Kevin Adolfo Lorenzo Condor
Economist in Training | Applied Microeconomics & Python
GitHub: KLorenzoEconomics
