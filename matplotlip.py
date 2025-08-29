#Solucion
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Configuración inicial
x = [0]
y = [0]

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(bottom=0.2)
(linea,) = ax.plot(x, y, marker='o', markersize=3, linewidth=1)
ax.set_title("Paseo aleatorio en 2D (haz click en el botón)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)
ax.axis("equal")

# --- Función para dar un paso ---
def dar_paso(event):
    direccion = np.random.choice(['x', 'y'])  # eje
    paso = np.random.choice([-1, 1])          # dirección

    if direccion == 'x':
        x.append(x[-1] + paso)
        y.append(y[-1])
    else:
        x.append(x[-1])
        y.append(y[-1] + paso)

    linea.set_xdata(x)
    linea.set_ydata(y)
    ax.relim()
    ax.autoscale_view()
    plt.draw()

# --- Crear botón ---
ax_boton = plt.axes([0.4, 0.05, 0.2, 0.075])  # posición del botón
boton = Button(ax_boton, 'Dar un paso')
boton.on_clicked(dar_paso)

plt.show()