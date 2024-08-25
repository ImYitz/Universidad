
#Pedir al usuario que ingrese la pendiente de la recta y un punto por donde pase esta (x1, y1)
#A partir de estos datos, generar la ecuación de la recta, nota 4.0
#Adicional, generar la gráfica de la recta, nota 5.0

#Fórmula para hallar la ecuación de la recta: y - y1 = m(x - x1)

m = int(input("Ingrese la pendiente de la recta: "))
punto1 = int(input("Ingrese el punto x1 por el que pasa la recta: "))
punto2 = int(input("Ingrese el punto y1 por el que pasa la recta: "))

print("La fórmula para hallar la ecuación es: y - ", punto2, " = ", m, "( x - ", punto1, ")")


