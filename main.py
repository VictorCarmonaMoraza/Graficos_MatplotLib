import matplotlib.pyplot as plt  # Importamos la librería matplotlib.pyplot, usada para crear gráficos en Python

# -------------------------------
# Datos del gráfico
# -------------------------------
x = [1, 2, 3, 4, 5]               # Lista con los valores del eje X (variable independiente)
y = [2.5, 3.7, 4.6, 8.0, 10.5]    # Lista con los valores del eje Y (variable dependiente)

# -------------------------------
# Creación del gráfico de dispersión
# -------------------------------
plt.scatter(x, y, color="red")    # Dibuja un gráfico de dispersión con puntos (x, y)
                                  # 'color' define el color de los puntos

# -------------------------------
# Personalización del gráfico
# -------------------------------
plt.title("Scatter Plot")         # Título del gráfico
plt.xlabel("Eje X")               # Etiqueta para el eje X
plt.ylabel("Eje Y")               # Etiqueta para el eje Y

# -------------------------------
# Mostrar el gráfico en pantalla
# -------------------------------
plt.show()                        # Muestra la ventana con el gráfico generado
