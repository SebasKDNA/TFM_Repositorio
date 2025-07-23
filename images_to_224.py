import os
from PIL import Image

# Carpeta raíz donde está el script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Carpetas (clases) que contienen las imágenes originales
root_dirs = ['Normal', 'Cardiomegalia', 'Neumotorax', 'Nodulo_Pulmonar', 'Engrosamiento_Pleural']

# Tamaño de redimensionamiento
target_size = (224, 224)

print("Iniciando redimensionamiento a 224x224...\n")

# Procesar cada carpeta de clase
for root in root_dirs:
    input_path = os.path.join(base_dir, "clasificacion_imgs", root)
    output_path = os.path.join(base_dir, "clasificacion_imgs_224", root)
    os.makedirs(output_path, exist_ok=True)

    for file in os.listdir(input_path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            src = os.path.join(input_path, file)
            dst = os.path.join(output_path, file)

            try:
                with Image.open(src) as img:
                    original_size = img.size
                    img = img.convert("RGB")
                    img = img.resize(target_size)
                    img.save(dst)
                    print(f"✅ {file} | {original_size} → {target_size} | Guardado en: {output_path}")
            except Exception as e:
                print(f"❌ Error procesando {src}: {e}")

print("\nRedimensionamiento finalizado con éxito.")
