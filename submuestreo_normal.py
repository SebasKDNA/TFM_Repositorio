import os
import random
import shutil

# Ruta origen y destino
origen = 'clasificacion_imgs_224/NormalV1'
destino = 'clasificacion_imgs_224/Normal'
cantidad = 10000

# Crear carpeta destino si no existe
os.makedirs(destino, exist_ok=True)

# Obtener lista de imágenes (extensiones comunes)
imagenes = [f for f in os.listdir(origen)
            if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Validar cantidad
if len(imagenes) < cantidad:
    raise ValueError(f"Solo hay {len(imagenes)} imágenes, no se pueden seleccionar {cantidad}.")

# Seleccionar aleatoriamente 10k
seleccionadas = random.sample(imagenes, cantidad)

# Copiar imágenes
for nombre in seleccionadas:
    origen_path = os.path.join(origen, nombre)
    destino_path = os.path.join(destino, nombre)
    shutil.copy2(origen_path, destino_path)

print(f"✅ Se copiaron {cantidad} imágenes a '{destino}' correctamente.")
