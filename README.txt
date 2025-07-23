README

Si únicamente se desea trabajar con la información y datos ya seleccionados se debe descargar del repositorio el comprimido "clasificacion_imgs_224.zip", cargar en Colab apartado Files dentro de la ruta /content/ el CSV "Data_Entry_2017_v2020.csv", luego ejecutar todo el notebook de Google Colab y en la sección: 
"Preprocesamiento Google Colab > Apartado 1 - Subida de ZIP"
se solicitará cargar el zip del repositorio previamente descargado.


Si se desea replicar de 0 el trabajo se requiere que se descargue los 12 archivos comprimidos con las imágenes
https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/37178474737

Después se descomprime en una carpeta de trabajo para las carpetas. se requiere tener instalado Python y descargado el CSV del repositorio llamado "Data_Entry_2017_v2020.csv", y se ejecutaría en el siguiente orden los scripts:

1. clasificacion_clases.py
2. images_to_224.py
3. submuestreo_normal.py
4. zip.py

Posterior a la ejecución de zip se creara el comprimido para trabajar en colab llamado "clasificacion_imgs_224.zip", en este punto se tiene que replicar lo anterior, cargar el CSV a Colab en el apartado Files, dentro de la carpeta /content/, se ejecuta todo el notebook y se solicitará cargar el nuevo ZIP en la sección:
"Preprocesamiento Google Colab > Apartado 1 - Subida de ZIP"