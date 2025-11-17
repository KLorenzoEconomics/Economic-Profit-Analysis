# AC–MC Cost Convergence Simulation

---

## 📌 Project Objectives

- Model the dynamic behavior of **Average Cost (AC)** and **Marginal Cost (MC)**.  
- Illustrate the convergence **AC → MC** as output expands.  
- Provide a reproducible, input-driven script for academic or applied use.  

---

## 🔍 Economic Background

### Average Cost (AC)  
```math
AC = \frac{FC + UVC \cdot Q}{Q}
Marginal Cost (MC)
𝑀
𝐶
=
𝑈
𝑉
𝐶
MC=UVC
As output (Q) increases, fixed costs are spread over more units, causing AC to approach MC. This script computes AC iteratively and reports when AC is sufficiently close to MC.

Note: If your GitHub preview does not render math blocks, the formulas remain readable as plain text.

📂 File Structure
bash
Copiar código
ac_mc_cost_convergence.py   # Main simulation script
README.md                   # This document
LICENSE                     # MIT License
.gitignore                  # Python ignore rules
▶️ How to Run
Install Python 3.8+.

From the repository root:

bash
Copiar código
python ac_mc_cost_convergence.py
Enter inputs when prompted:

Total Fixed Cost (FC)

Unit Variable Cost (UVC)

The script iterates up to 25 quantities and prints AC and MC for each Q; it stops early if AC ≈ MC (difference < 0.01).

📊 Example Output
markdown
Copiar código
Q   |     AC      |     MC
----------------------------------------------
  1 |  55.0000    |  10.0000
  2 |  32.5000    |  10.0000
  3 |  25.0000    |  10.0000
  4 |  21.2500    |  10.0000
  ...
🔹 AC has approached MC (difference < 0.01).
🧠 Economic Interpretation
Initial units bear a large share of fixed cost; thus AC > MC.

As Q grows, AC declines toward MC because fixed cost is diluted.

Under constant UVC, AC converges to MC — a fundamental result in microeconomics.

🛠 Technical Notes & Extensions
Tech: Python 3 (no external dependencies).
Possible enhancements:

Vectorized scenarios with numpy and CSV outputs.

AC vs MC plot using matplotlib.

Parameterized CLI or config-file mode for batch runs.

📜 License
This repository is released under the MIT License. See LICENSE for details.

👤 Author
Kevin Adolfo Lorenzo Condor
Economist in training — Applied Microeconomics & Python
GitHub: KLorenzoEconomics
