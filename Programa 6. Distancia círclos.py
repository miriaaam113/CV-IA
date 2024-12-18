import cv2
import numpy as np

# Ruta completa de la imagen
ruta_imagen = "distancia.jpg"

# Cargar la imagen
imagen = cv2.imread(ruta_imagen)
if imagen is None:
    print(f"Error: No se pudo cargar la imagen desde '{ruta_imagen}'.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar círculos usando HoughCircles
circulos = cv2.HoughCircles(
    gris, cv2.HOUGH_GRADIENT, dp=1.2, minDist=30,
    param1=50, param2=30, minRadius=10, maxRadius=50
)

# Verificar si se detectaron círculos
if circulos is not None:
    # Convertir los valores a enteros
    circulos = np.round(circulos[0, :]).astype("int")
    referencia_circulo = circulos[0]  # Tomar el primer círculo como referencia
    escala_referencia = 20.0  # Escala en mm

    for (x, y, r) in circulos:
        # Dibujar el círculo detectado
        cv2.circle(imagen, (x, y), r, (0, 255, 0), 2)
        # Dibujar el centro del círculo
        cv2.circle(imagen, (x, y), 2, (0, 0, 255), 3)
        
        # Calcular la distancia en píxeles
        pixel_distancia = np.sqrt(
            (x - referencia_circulo[0])**2 + (y - referencia_circulo[1])**2
        )
        
        # Convertir la distancia a unidades reales (mm)
        escala = escala_referencia / referencia_circulo[2]
        real_distancia = pixel_distancia * escala
        
        # Dibujar la línea entre el círculo actual y el de referencia
        cv2.line(imagen, (referencia_circulo[0], referencia_circulo[1]), (x, y), (255, 0, 0), 1)
        # Mostrar la distancia sobre la línea
        cv2.putText(
            imagen, f"{real_distancia:.2f} mm", (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2
        )

    # Dibujar el círculo de referencia
    cv2.circle(imagen, (referencia_circulo[0], referencia_circulo[1]), referencia_circulo[2], (255, 0, 0), 2)
    cv2.putText(
        imagen, "Referencia",
        (referencia_circulo[0] - 40, referencia_circulo[1] - referencia_circulo[2] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2
    )

# Mostrar la imagen final
cv2.imshow("Distancia entre círculos", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
