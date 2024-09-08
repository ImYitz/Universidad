import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import pretty
import tkinter as tk
from tkinter import simpledialog, messagebox

# Función que recibe una ecuación en forma de string y grafica la recta
def graficar_recta_desde_ecuacion(ecuacion_str, x_min=-10, x_max=10):
    # Definir x como una variable simbólica
    x = sp.symbols('x')
    
    # Convertir la ecuación de string a expresión simbólica
    ecuacion = sp.sympify(ecuacion_str)
    
    # Extraer los coeficientes de la pendiente (m) y la intersección (b)
    m = ecuacion.coeff(x)  # Coeficiente de x (pendiente)
    b = ecuacion.subs(x, 0)  # Valor de f(x) cuando x = 0 (intersección)

    # Convertir los coeficientes a flotantes en caso de ser racionales
    m = float(m)
    b = float(b)

    # Crear el rango de valores de x
    x_vals = np.linspace(x_min, x_max, 400)
    
    # Calcular los valores de f(x) = mx + b
    y_vals = m * x_vals + b
    
    # Crear la gráfica
    plt.figure(figsize=(6, 6))
    plt.plot(x_vals, y_vals, label=f'y = {ecuacion_str}', color='blue')
    
    # Ajustar el aspecto de la gráfica para que no sea tan ancha
    plt.gca().set_aspect('auto', adjustable='box')
    
    # Etiquetas y título
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.title('Gráfico de la recta')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    
    # Mostrar cuadrícula
    plt.grid(True)
    
    # Mostrar leyenda
    plt.legend()
    
    # Mostrar gráfica
    plt.show()

# Crear una ventana principal
root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

# Definir las variables simbólicas
y, x = sp.symbols('y x')

# Asignar los valores específicos a z, m y w
# Pedir tres números al usuario
z = simpledialog.askfloat("Input", "Ingresa el valor de y1: ")
m = simpledialog.askfloat("Input", "Ingresa el valor de la pendiente: ")
w = simpledialog.askfloat("Input", "Ingresa el valor de x1: ")

# Definir la ecuación con los valores dados
ecuacion = sp.Eq(y - z, m * (x - w))

# Despejar la ecuación para y
solucion_y = sp.solve(ecuacion, y)[0]

# Simplificar la expresión
solucion_simplificada = sp.simplify(solucion_y)

# Mostrar la solución en el formato deseado
messagebox.showinfo("Resultado", f"f(x) = {pretty(solucion_simplificada, use_unicode=True)}")

# Ejemplo de uso, ecuación de la recta
graficar_recta_desde_ecuacion(solucion_simplificada)