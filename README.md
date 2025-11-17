# AC–MC Cost Convergence Simulation

A clean and compact Python simulation that demonstrates how **Average Cost (AC)** converges to **Marginal Cost (MC)** as output increases under constant unit variable costs. Ideal for academic use, applied economics, and portfolio projects.

---

## 📌 Project Objectives

- Model the behavior of **Average Cost** and **Marginal Cost** dynamically.  
- Illustrate the convergence **AC → MC** as output expands.  
- Provide a reproducible Python implementation for learning or applied research.

---

## 🔍 Economic Background

### **Average Cost (AC)**  
AC = (Fixed Cost + Variable Cost per unit × Q) / Q  
AC = (FC + UVC × Q) / Q  

### **Marginal Cost (MC)**  
MC = Variable Cost per unit  
MC = UVC  

As production increases, the fixed cost is spread across more units, causing AC to get closer and closer to MC.  
This script simulates that convergence step by step.

---

## 📂 File Structure

ac_mc_cost_convergence.py # Main simulation script
README.md # Documentation
LICENSE # MIT License
.gitignore # Python ignore rules

yaml
Copiar código

---

## ▶️ How to Run the Script

1. Install **Python 3.8+**  
2. Run the script:

```bash
python ac_mc_cost_convergence.py
Enter the requested inputs:

Total Fixed Cost (FC)

Unit Variable Cost (UVC)

The program will compute AC for increasing values of Q and detect when AC becomes very close to MC (difference < 0.01).

📊 Sample Output
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
🧠 Interpretation
AC starts higher because fixed costs heavily impact low production levels.

As Q rises, AC declines and gets closer to MC.

Under constant marginal cost technologies, AC always converges to MC in the long run — a fundamental microeconomic insight.

🛠 Technologies Used
Python 3

Fundamental microeconomic cost modeling

Iterative computation and console-based reporting

📜 License
Released under the MIT License.
You may use, modify, and distribute the code with attribution.

👤 Author
Kevin Adolfo Lorenzo Condor
Economist in training | Applied Microeconomics & Python
GitHub: KLorenzoEconomics
