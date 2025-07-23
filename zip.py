import os
import shutil
from zipfile import ZipFile

base_dir = os.path.dirname(os.path.abspath(__file__))
output_zip = os.path.join(base_dir, 'clasificacion_imgs_224.zip')

# Rutas origen
clases = ['Cardiomegalia', 'Neumotorax', 'Nodulo_Pulmonar', 'Engrosamiento_Pleural']
normal_v1 = os.path.join(base_dir, 'clasificacion_imgs_224', 'NormalV1')
otros = [os.path.join(base_dir, 'clasificacion_imgs_224', clase) for clase in clases]

print("Compresión ZIP...")

with ZipFile(output_zip, 'w') as zipf:
    # Agregar NormalV1 como 'Normal'
    for file in os.listdir(normal_v1):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            ruta_absoluta = os.path.join(normal_v1, file)
            ruta_en_zip = os.path.join('Normal', file)
            zipf.write(ruta_absoluta, ruta_en_zip)

    # Agregar otras clases
    for carpeta in otros:
        clase = os.path.basename(carpeta)
        for file in os.listdir(carpeta):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                ruta_absoluta = os.path.join(carpeta, file)
                ruta_en_zip = os.path.join(clase, file)
                zipf.write(ruta_absoluta, ruta_en_zip)

print(f"ZIP generado exitosamente en: {output_zip}")
