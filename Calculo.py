import sympy as sp
from sympy import pretty
import tkinter as tk
from tkinter import simpledialog, messagebox

# Crear una ventana principal
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

# Definir las variables simbólicas
y, x = sp.symbols('y x')

# Asignar los valores específicos a z, m y w
# Pedir tres números al usuario
z = simpledialog.askinteger("Input", "Ingresa el valor de y1: ")
m = simpledialog.askinteger("Input", "Ingresa el valor de la pendiente: ")
w = simpledialog.askinteger("Input", "Ingresa el valor de x1: ")

# Definir la ecuación con los valores dados
ecuacion = sp.Eq(y - z, m * (x - w))

# Despejar la ecuación para y
solucion_y = sp.solve(ecuacion, y)[0]

# Simplificar la expresión
solucion_simplificada = sp.simplify(solucion_y)

# Mostrar la solución en el formato deseado
#print("La solución de la ecuación es:")
#print(f"f(x) = {pretty(solucion_simplificada, use_unicode=True)}")
messagebox.showinfo("Resultado", f"f(x) = {pretty(solucion_simplificada, use_unicode=True)}")
