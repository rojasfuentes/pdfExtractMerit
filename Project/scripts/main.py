import re
import pandas as pd

# Cargamos el archivo de texto y lo leemos
with open(r'C:\Users\JFROJAS\Desktop\Merit\Project\PDF\output\texto_modificado.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Buscamos las palabras que estén antes de un patrón de CP- seguido de 6 números
desc_1 = r'(\w+)\s+CP-\d{6}'
desc_2 = r'\b\d{3}[A-Z]{2}-[A-Z]{2}\b'
desc_3 = r'\b\d{2}[A-Z]{2}\d{5}[A-Z]{2}\b'
desc_4 = r'\b\d{6}[A-Z]{2}\d\-[A-Z]\b'
desc_5 = r'\b\d{6}[A-Z]{4}-[A-Z]\b'
desc_6 = r'\b\d{7}\b' 
desc_7 = r'\b\d{6}[A-Z]{3}\b'
desc_8 = r'\b\d{4}-\d{2}\b'
desc_9 = r'\b\d{5}[A-Z]{2}\d\-[A-Z]\b'  #Se parece a la 4
desc_10 = r'\b\d{5}[A-Z]{3}\-[A-Z]\b'  #Se parece a la 4
desc_11 = r'\b\d{5}[A-Z]{3}\b'  #Se parece a la 4
desc_35 = r'\b[A-Z]{2}\d{2}[A-Z]{1}\d{2}[A-Z]{1}\b'  #Se parece a la 4
desc_12 = r'\b[A-Z]{2}\d{5}[A-Z]{1}\b'  #Se parece a la 4
desc_13 = r'\b[A-Z]{3}\d{4}[A-Z]{2}\d{1}\b'
desc_14 = r'\b[A-Z]{2}\d{4}\b'
desc_15 = r'\b[A-Z]{3}\d{3}\b'
desc_16 = r'\b[A-Z]{5}\d{5}[A-Z]{2}\b'
desc_17 = r'\b[A-Z]{3}\d{1}[A-Z]{1}\d{5}[A-Z]{2}\b' 
desc_18 = r'\b[A-Z]{3}-\d{1}[A-Z]{1}-\d{2}-\d{3}\b' #PSI-6F-11-038  #PSI-6F-11-038
desc_19 = r'\b[A-Z]{3}-[A-Z]{2}-\d{2}-\d{3}\b' #PSI-SF-11-018
desc_20 = r'\b[A-Z]{5}-[A-Z]{2}-\d{2}-[A-Z]{3}\b' #RLCMB-NV-12-REV 
desc_21 = r'\b[A-Z]{5}-[A-Z]{2}-\d{1}-[A-Z]{3}\b' #RLCMB-NV-8-REV 
desc_22 = r'\b[A-Z]{2}\d{3}\b' #RR811
desc_23 = r'\b[A-Z]{3}\d{4}\b'
desc_24 = r'\b[A-Z]{2}\d{4}\b'
desc_25 = r'\b[A-Z]{3}\d{4}\b'
desc_26 = r'\b[A-Z]{3}\d{3}\b[A-Z]{1}\b'
desc_27 = r'\b[A-Z]{3}-[A-Z]{2}-\d{3}\b'#MAK-NV-002
desc_28 = r'\b[A-Z]{3}-\d{1}[A-Z]{1}-\d{2}[A-Z]{1}\b' #OSC-4F-10L
desc_29 = r'\b[A-Z]{3}-[A-Z]{2}-\d{2}[A-Z]{1}\b' #osc-Sf-10L 
desc_38 = r'\b[A-Z]{3}-[A-Z]{2}-\d{1}[A-Z]{1}\b' #osc-Sf-7L 
desc_30 = r'\b[A-Z]{3}-\d{4}' #pls-1007
desc_31 = r'\b[A-Z]{4}-\d{4}' #plsx-1008
desc_32 = r'\b[A-Z]{2}\d{2}[A-Z]{1}\d{3}[A-Z]{1}\d{1}' #IQ35F26013
desc_33 = r'\b[A-Z]{6}\d{5}[A-Z]{2}' #LWSTDA25260EX
desc_34 = r'\b[A-Z]{5}\d{6}' #LWSTD535150
desc_36 = r'\b\d{3}-[A-Z]{2}' #550-lb
desc_37 = r'\b[A-Z]{3}\d{3}[A-Z]{1}' #HPC200E
desc_39 = r'\b[A-Z]{6}\d{5}' #LWSTDS35150
desc_40 = r'\b[A-Z]{3}-\d{1}[A-Z]{1}-\d{1}[A-Z]{1}' # OSC-5F-7L
desc_41 = r'\b\d{6}[A-Z]{3}\d{1}-[A-Z]{1}' # 510038SIM1-H
desc_42 = r'\b\d{5}[A-Z]{2}\d{1}' # 56538CB1
desc_43 = r'\b[A-Z]{3}\d{4}[A-Z]{2}\d{1}' # CGC6100AR1/A
desc_44 = r'\b[A-Z]{5}-[A-Z]{2}-\d{2}-' # RLCMB-NV-12-
desc_45 = r'\b[A-Z]{5}-[A-Z]{2}-\d{2}-[A-Z]{3}' # RLCMB-NV-8-REV


exl = 'FZ624'
desc = f'({desc_6})|({desc_2})|({desc_3})|({desc_4})|({desc_5})|({desc_1})|({desc_7})|({desc_8})|({desc_9})|({desc_10})|({desc_11})|({desc_12})|({desc_13})|({desc_14})|({desc_15})|({desc_16})|({desc_17})|({desc_18})|({desc_19})|({desc_20})|({desc_21})|({desc_22})|({desc_23})|({desc_24})|({desc_25})|({desc_26})|({desc_27})|({desc_28})|({desc_29})|({desc_30})|({desc_31})|({desc_32})|({desc_33})|({desc_34})|({desc_35})|({desc_36})|({desc_37})|({desc_38})|({desc_39})|({desc_40})|({desc_41})|({desc_42})|({desc_43})|({desc_44})|({desc_45})'

lote_1 = r'\b[A-Za-z]\d{7}\b'
lote_2 = r'\b[A-Z]\d{6}\b'
lote = f'({lote_1})|({lote_2})'

cant_1 = r'(\w+)\s+EA'
cant_2 = r'EA\s+(\w+)'
cant = f'({cant_1})|({cant_2})'

matches_desc = re.findall(desc, text)
matches_lote = re.findall(lote, text)
matches_cant = re.findall(cant, text)

results = [tupla[i] for tupla in matches_desc if any(tupla) for i in range(len(tupla)) if tupla[i]]
lote_results = [tupla[i] for tupla in matches_lote if any(tupla) for i in range(len(tupla)) if tupla[i]]
cant_results = [tupla[i] for tupla in matches_cant if any(tupla) for i in range(len(tupla)) if tupla[i]]


results_fin = [palabra for palabra in results if palabra != exl]

matches_lote = [x.strip() for x, _ in matches_lote]




# Función lambda para filtrar elementos
filtro = lambda x: not x.isalpha() and len(x) <= 3 and x[0] != '0'

# Aplicar el filtro a la lista
lista_filtrada = list(filter(filtro, cant_results))


#print(results_fin)
print('total de resultados: ', len(results_fin))
print('total de lotes: ', len(matches_lote))
print('total de cantidades: ', len(matches_cant))


# Creamos un dataframe con pandas
df = pd.DataFrame({
    'Descripción': results_fin,
    'Lote': matches_lote,
    #'Cantidad': matches_cant
})

print(df)

# Guardamos el dataframe en un archivo Excel
df.to_excel(r'C:\Users\JFROJAS\Desktop\Merit\Project\resultados.xlsx', index=False)
