import matplotlib.pyplot as plt  # Importamos la librería matplotlib.pyplot, usada para crear gráficos en Python

# Data
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 30]

plt.bar(categories, values,
        color='skyblue',  # Color de relleno
        edgecolor='black',  # Color del borde
        linewidth=1.5)  # Grosor del borde
plt.title("Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
