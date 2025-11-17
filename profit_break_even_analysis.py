"""
Análisis de Beneficio y Punto de Equilibrio
-------------------------------------------
Este script permite calcular el beneficio económico de una firma competitiva 
según distintas cantidades producidas, identificando el punto de equilibrio 
(Qe) donde el beneficio total es igual a cero o comienza a ser positivo.

Autor: Kevin Adolfo Lorenzo Condor  
Formación: Economista en desarrollo | Análisis aplicado & Python  
Repositorio: https://github.com/KevinLorenzoEconomy
"""

# ============================================================
# 1️⃣ Inputs Económicos
# ============================================================

precio_unitario = float(input("Precio unitario del bien o servicio: "))
cf = float(input("Costo fijo total (CF): "))
cv_unitario = float(input("Costo variable unitario (CVu): "))

# ============================================================
# 2️⃣ Definición de la Función de Beneficio Económico
# ============================================================

def calcular_beneficio(precio_unitario: float, cf: float, cv_unitario: float, q: float) -> float:
    """
    Calcula el beneficio económico total de la firma.

    Parámetros:
        precio_unitario (float): Precio por unidad del bien o servicio.
        cf (float): Costo fijo total.
        cv_unitario (float): Costo variable unitario.
        q (float): Cantidad producida.

    Retorna:
        float: Beneficio económico total (π).
    """
    ingreso_total = precio_unitario * q
    costo_total = cf + (cv_unitario * q)
    beneficio = ingreso_total - costo_total
    return beneficio

# ============================================================
# 3️⃣ Análisis Iterativo: Cálculo hasta el Punto de Equilibrio
# ============================================================

print("\n==============================================")
print("        ANÁLISIS ECONÓMICO SEGÚN CANTIDAD")
print("==============================================\n")

q = 1  # cantidad inicial

while True:
    beneficio = calcular_beneficio(precio_unitario, cf, cv_unitario, q)
    print(f"Q = {q:3d} → Beneficio Económico (π) = {beneficio:,.2f}")

    # Condición de equilibrio o superávit
    if beneficio >= 0:
        print("\n🔹 Punto de equilibrio alcanzado o superado.")
        print(f"🔸 Cantidad de equilibrio (Qe) ≈ {q}")
        print(f"🔸 Beneficio en equilibrio: {beneficio:,.2f}")
        break

    q += 1  # incrementa la cantidad en una unidad
    print("----------------------------------------------")

# ============================================================
# 4️⃣ Interpretación Económica Final
# ============================================================

print("\n----------------------------------------------")
print("INTERPRETACIÓN ECONÓMICA:")
print("----------------------------------------------")
print(f"A medida que la cantidad (Q) aumenta, el beneficio tiende a reducir "
      f"las pérdidas iniciales hasta alcanzar el punto de equilibrio (Qe = {q}).")
print("A partir de dicho punto, la empresa comienza a generar beneficio económico positivo.")
