import os
import re

# Ruta del archivo de entrada
ruta_entrada = r"C:\Users\JFROJAS\Desktop\Merit\Project\PDF\output\texto.txt"

# Ruta del archivo de salida
ruta_salida = r"C:\Users\JFROJAS\Desktop\Merit\Project\PDF\output\texto_modificado.txt"

# Verificar si la carpeta de salida existe, si no, crearla
if not os.path.exists(os.path.dirname(ruta_salida)):
    os.makedirs(os.path.dirname(ruta_salida))

with open(ruta_entrada, 'r') as f:
    # cargar el contenido del archivo en una variable
    content = f.readlines()

# crear una lista con cada línea del archivo
lines = [line.strip() for line in content]

# eliminar las líneas vacías
lines = [line for line in lines if line]

# reemplazar "-SF-" por "-5F-"
lines = [line.replace("-SF-", "-5F-") for line in lines]
lines = [line.replace("5N", "SN") for line in lines]
lines = [line.replace("1Q", "IQ") for line in lines]
lines = [line.replace("FASS", "FAS5") for line in lines]
lines = [line.replace("ONE ", "ONE") for line in lines]
lines = [line.replace("141W", "T41W") for line in lines]
lines = [line.replace("ARI", "AR1") for line in lines]
lines = [line.replace("PS1-", "PSI-") for line in lines]
lines = [line.replace("26013", "260J3") for line in lines]

# Eliminar números de 8 dígitos con guión antes
lines = [re.sub(r'\b\d{6}-\d{8}\b', '', line) for line in lines]
lines = [re.sub(r'\b\d{6}[-\s]\d{8}\b', '', line) for line in lines]
lines = [re.sub(r'(?<=-)\s?\d{8}\b', '', line) for line in lines]
lines = [re.sub(r'\b1(\d{7})\b', r'I\1', line) for line in lines]

# escribir el contenido modificado en un nuevo archivo
with open(ruta_salida, 'w') as f:
    f.write('\n'.join(lines))
