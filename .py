import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(img_w=800, img_h=600, center_x=-0.5, center_y=0.0,
               scale=3.0, max_iter=200):
    # Rango en el plano complejo
    real_min = center_x - scale / 2
    real_max = center_x + scale / 2
    imag_span = scale * (img_h / img_w)
    imag_min = center_y - imag_span / 2
    imag_max = center_y + imag_span / 2

    # Crear grilla de coordenadas complejas
    real = np.linspace(real_min, real_max, img_w)
    imag = np.linspace(imag_max, imag_min, img_h)  # eje y invertido
    Re, Im = np.meshgrid(real, imag)
    C = Re + 1j * Im

    # Iteraciones de Mandelbrot
    Z = np.zeros_like(C, dtype=np.complex128)
    div_time = np.zeros(C.shape, dtype=int)  # número de iteraciones hasta escapar

    mask = np.ones(C.shape, dtype=bool)  # quién sigue dentro
    for i in range(max_iter):
        Z[mask] = Z[mask]**2 + C[mask]
        mask_new = np.abs(Z) <= 2.0
        div_time[mask & ~mask_new] = i  # guardar dónde escapó
        mask = mask_new

    div_time[div_time == 0] = max_iter  # los que nunca escaparon = interior
    return div_time

# Generar fractal
img = mandelbrot(img_w=1000, img_h=800, max_iter=500)

# Mostrar con colormap
plt.figure(figsize=(10, 8))
plt.imshow(img, cmap="inferno", extent=(-2, 1, -1.5, 1.5))
plt.colorbar(label="Iteraciones hasta escapar")
plt.title("Conjunto de Mandelbrot")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()