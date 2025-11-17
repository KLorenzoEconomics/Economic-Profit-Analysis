# **Break-Even Profit Analysis — Microeconomic Simulation in Python**

A computational microeconomic engine that models how a competitive firm transitions from loss to profitability.  
This project simulates economic profit dynamically across output levels, identifying the break-even quantity where π = 0 and profitability emerges.  
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

### **Profit Function (π)**  
```math
\pi(Q) = P \cdot Q - \big[CF + CV_u \cdot Q\big]
Where:

P → Unit price

CF → Total fixed cost

CVu → Unit variable cost

Q → Output

A firm in perfect competition faces a constant price and produces until losses vanish and profit begins to rise. This script reveals that transition step-by-step.

🧮 How the Simulation Works
The program:

Requests key economic inputs:

Unit price (P)

Total fixed cost (CF)

Unit variable cost (CVu)

Iteratively increases output Q = 1, 2, 3 …

Calculates for each Q:

Total revenue: 
𝑇
𝑅
=
𝑃
⋅
𝑄
TR=P⋅Q

Total cost: 
𝑇
𝐶
=
𝐶
𝐹
+
𝐶
𝑉
𝑢
⋅
𝑄
TC=CF+CV 
u
​
 ⋅Q

Economic profit: 
𝜋
(
𝑄
)
=
𝑇
𝑅
−
𝑇
𝐶
π(Q)=TR−TC

Stops once:

𝜋
(
𝑄
)
≥
0
π(Q)≥0
Prints the exact break-even quantity (Qe) and the profit at Qe.

📊 Sample Output
text
Copiar código
Q =   1 → Economic Profit (π) = -45.00
Q =   2 → Economic Profit (π) = -15.00
Q =   3 → Economic Profit (π) =   5.00

🔹 Break-even reached.
🔸 Break-even quantity (Qe): 3
🔸 Profit at Qe: 5.00
▶️ How to Run
Ensure Python 3.8+ is installed.

From the repository root run:

bash
Copiar código
python break_even_profit_analysis.py
Provide the requested parameters when prompted:

Unit price (P)

Total fixed cost (CF)

Unit variable cost (CVu)

Review the stepwise profit evolution and the reported break-even quantity.

🧠 Interpretation
As output increases, the firm spreads fixed costs across more units, reducing initial losses. When cumulative revenue covers fixed and variable costs, the firm reaches break-even—the threshold between loss and positive economic profit.

This model demonstrates:

Cost dilution effects

The profit transition point for a competitive firm

Fundamental microeconomic dynamics in a computationally transparent way

🛠️ Technologies & Design
Python 3 (script style, no external dependencies)

Simple, well-documented functions for profit computation

Deterministic, input-driven iterative evaluation suitable for classroom demos or inclusion in larger toolkits

📂 Recommended File Structure
bash
Copiar código
/repo-root
├─ src/
│  └─ break_even_profit_analysis.py
├─ data/           # (optional) sample parameter files or scenario configs
├─ notebooks/      # (optional) Jupyter explainer notebooks and visualizations
├─ README.md
├─ .gitignore
└─ LICENSE
📜 License
This project is released under the MIT License — free to use, modify, and redistribute with attribution.

👤 Author
Kevin Adolfo Lorenzo Condor
Economist in Training | Applied Microeconomics & Python
GitHub: KLorenzoEconomics
