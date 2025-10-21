import matplotlib.pyplot as plt  # Importamos la librería matplotlib.pyplot, usada para crear gráficos en Python

# -------------------------------
# Datos del gráfico
# -------------------------------
x = [1, 2, 3, 4, 5]  # Lista con los valores del eje X (independiente)
y = [2, 4, 6, 8, 10] # Lista con los valores del eje Y (dependiente)

# -------------------------------
# Creación del gráfico de líneas
# -------------------------------
plt.plot(x, y, label="line")  # Crea una línea conectando los puntos (x, y)
                              # El parámetro 'label' asigna un nombre a la línea para la leyenda

# -------------------------------
# Personalización del gráfico
# -------------------------------
plt.title("Gráfica de líneas")   # Establece el título del gráfico
plt.xlabel("Eje X")              # Nombre del eje X
plt.ylabel("Eje Y")              # Nombre del eje Y
plt.legend()                     # Muestra la leyenda con el texto definido en 'label'

# -------------------------------
# Mostrar el gráfico en pantalla
# -------------------------------
plt.show()  # Renderiza y muestra la gráfica en una ventana
