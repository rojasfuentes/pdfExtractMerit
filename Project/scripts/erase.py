import os
import glob

# Indica la ruta de la carpeta que contiene los archivos y carpetas a eliminar
folder_path = r'C:\Users\JFROJAS\Desktop\Merit\Project\PDF'

# Borra la carpeta "output" si existe
output_folder = os.path.join(folder_path, 'output')
if os.path.exists(output_folder):
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    os.rmdir(output_folder)
    print(f'La carpeta {output_folder} ha sido borrada.')

print('Operación de borrado completada.')

