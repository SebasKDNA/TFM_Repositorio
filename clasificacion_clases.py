import os
import shutil
import pandas as pd
from collections import defaultdict

# Rutas
csv_path = "Data_Entry_2017_v2020.csv"
output_dir = "clasificacion_imgs"

# Diccionario de reemplazo de etiquetas al español
reemplazos = {
    'No Finding': 'Normal',
    'Cardiomegaly': 'Cardiomegalia',
    'Pneumothorax': 'Neumotorax',
    'Nodule': 'Nodulo_Pulmonar',
    'Pleural_Thickening': 'Engrosamiento_Pleural'
}

# Lista de etiquetas seleccionadas (en español)
etiquetas_objetivo = list(reemplazos.values()) + ['Normal']

# Crear carpetas por cada etiqueta
for etiqueta in etiquetas_objetivo:
    os.makedirs(os.path.join(output_dir, etiqueta), exist_ok=True)

# Cargar CSV
df = pd.read_csv(csv_path)

# Reemplazar etiquetas
def reemplazar_etiquetas(etiquetas_str):
    etiquetas = etiquetas_str.split('|')
    etiquetas_mod = [reemplazos.get(e, e) for e in etiquetas]
    return etiquetas_mod

df['Labels'] = df['Finding Labels'].apply(reemplazar_etiquetas)

# Función para encontrar una imagen en subcarpetas images_001 a images_012
def buscar_imagen(nombre_imagen):
    for i in range(1, 13):
        subdir = f"images_{i:03d}"
        ruta = os.path.join(subdir, nombre_imagen)
        if os.path.exists(ruta):
            return ruta
    return None

conteo = defaultdict(int)

for _, row in df.iterrows():
    nombre_imagen = row['Image Index']
    etiquetas = row['Labels']

    if len(etiquetas) == 1 and etiquetas[0] in etiquetas_objetivo:
        clase = etiquetas[0]
        destino = os.path.join(output_dir, clase, nombre_imagen)

        origen = buscar_imagen(nombre_imagen)
        if origen and not os.path.exists(destino):
            shutil.copy2(origen, destino)
            conteo[clase] += 1


print("Total Imágenes:")
for clase in etiquetas_objetivo:
    print(f"- {clase}: {conteo[clase]} imágenes")
