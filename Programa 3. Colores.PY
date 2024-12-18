import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carga de la imagen
imagen = cv2.imread('C:/Users/Miriam R/Pictures/guacamaya.jpg')

# Conversión de color adecuada para una imagen en color
color = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # Cambia a RGB en lugar de Bayer

#
bordes = cv2.Canny(color, 100, 200)

# Mostrar las imágenes
cv2.imshow('Imagen original', imagen)
cv2.imshow('Imagen en RGB', color)
cv2.imshow('Imagen gris bordes', bordes)

cv2.waitKey(0)
cv2.destroyAllWindows()
