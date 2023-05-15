import os
from pdf2image import convert_from_path

# Agrega la ruta de Poppler a la variable de entorno PATH en tiempo de ejecución
poppler_path = r'C:/Users/JFROJAS/Downloads/poppler-0.68.0_x86/poppler-0.68.0/bin'
os.environ['PATH'] += os.pathsep + poppler_path

# Indica la ruta de la carpeta que contiene los archivos PDF
folder_path = r'C:\Users\JFROJAS\Desktop\Merit\Project\PDF'

# Crea la carpeta "output" si no existe
output_folder = os.path.join(folder_path, 'output')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Obtén la lista de archivos en la carpeta
files = os.listdir(folder_path)

# Filtra la lista para obtener solo los archivos PDF
pdf_files = [file for file in files if file.endswith('.pdf')]

# Convierte cada archivo PDF en imágenes
for i, pdf_file in enumerate(pdf_files):
    pdf_path = os.path.join(folder_path, pdf_file)
    pages = convert_from_path(pdf_path)
    for j, page in enumerate(pages):
        output_file = os.path.join(output_folder, f'pagina_{i}_{j}.jpg')
        page.save(output_file, 'JPEG')
