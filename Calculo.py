
def despejar_si_punto2(m, punto1, punto2):
    
    if punto2 > 0:  #Si el punto y1 es positivo
        print("La fórmula para hallar la ecuación es: y -", punto2, " = ", m, "( x - ", punto1, ")")
        print("Despejando: " + "y - ", punto2, " = ", m, "x", " - ", m*punto1)
        print("La ecuación de la recta es: " + "f(x) = ", m, "x", "-", (m*punto1)-punto2)
    if punto2 < 0:  #Si el punto y1 es negativo
        print("La fórmula para hallar la ecuación es: y - (", punto2, ")", " = ", m, "( x - ", punto1, ")")
        print("Despejando: ", "y +", abs(punto2), " = ", m, "x", " - ", m*punto1)
        print("La ecuación de la recta es: ", "f(x) = ", m, "x", "-", (m*punto1)-punto2)
    return None

def despejar_si_punto1(m, punto1, punto2):
    if punto1 > 0:   #Si la pendiente es positiva
        print("La fórmula para hallar la ecuación es: y -", punto2, " = ", m, "( x - ", punto1, ")")
        print("Despejando: " + "y - ", punto2, " = ", m, "x", " - ", m*punto1)
        print("La ecuación de la recta es: " + "f(x) = ", m, "x", "-", (m*punto1)-punto2)
    if punto1 < 0:   #Si la pendiente es negativa
        print("La fórmula para hallar la ecuación es: y -", punto2, " = ", m, "( x - ", punto1, ")")
        print("Despejando: " + "y - ", punto2, " = ", m, "x", " + ", abs(m*(punto1)))
        print("La ecuación de la recta es: " + "f(x) = ", m, "x", "+", abs((m*punto1)-punto2))
    return None

def despejar_si_pendiente(m, punto1, punto2):
    if m > 0:   #Si la pendiente es positiva
        print("La fórmula para hallar la ecuación es: y -", punto2, " = ", m, "( x - ", punto1, ")")
        print("Despejando: " + "y - ", punto2, " = ", m, "x", " - ", m*punto1)
        print("La ecuación de la recta es: " + "f(x) = ", m, "x", "-", (m*punto1)-punto2)
    if m < 0:   #Si la pendiente es negativa
        print("La fórmula para hallar la ecuación es: y -", punto2, " = ", m, "( x - ", punto1, ")")
        print("Despejando: " + "y - ", punto2, " = ", m, "x", " + ", abs(m*(punto1)))
        print("La ecuación de la recta es: " + "f(x) = ", m, "x", "+", abs((m*punto1)-punto2))
    return None

#Pedir al usuario que ingrese la pendiente de la recta y un punto por donde pase esta (x1, y1)
#A partir de estos datos, generar la ecuación de la recta, nota 4.0
#Adicional, generar la gráfica de la recta, nota 5.0

#Fórmula para hallar la ecuación de la recta: y - y1 = m(x - x1)

m = int(input("Ingrese la pendiente de la recta: "))
punto1 = int(input("Ingrese el punto x1 por el que pasa la recta: "))
punto2 = int(input("Ingrese el punto y1 por el que pasa la recta: "))

#print("La fórmula para hallar la ecuación es: y - ", punto2, " = ", m, "( x - ", punto1, ")")

#if m > 0 and punto1 > 0 and punto2 > 0:

