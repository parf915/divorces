import os
import openai
import csv
import time

# Securely store and access the API key using environment variables or other secure means
api_key = ''
client = openai.OpenAI(api_key=api_key)

# Instructions for the GPT model to follow when analyzing the text
content_instrucciones = """
Analiza el acta de divorcio/separacion y resume la información clave en el formato
NUMERO DE PARTIDA|OFICINA REGISTRAL|NOMBRE1|DNI1|NOMBRE2|DNI2|FECHA.
Identifica nombres de los involucrados, sus DNI, la fecha, y la oficina registral.
Usa * para campos faltantes. Solo incluye nombres de las partes que se divorcian,
excluyendo otros como notarios, abogados etc. Si el documento no es un acta de divorcio,
retorna NO ES DIVORCIO.
"""

# Directory containing the text files from the divorce documents
directorio = '/Users/renzo/Downloads/divorcios_txt'

# CSV file to save the summarized information
archivo_csv = '/Users/renzo/Downloads/divorcios_txt/resultado_divorcios_separacion.csv'

# List all files in the directory and filter only files (excluding directories)
archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
tiempo_inicio = time.time()

# Open a CSV file for writing the results
with open(archivo_csv, mode='w', newline='', encoding='utf-8') as file:
    escritor_csv = csv.writer(file, delimiter='|')
    
    for archivo in archivos:
        ruta_completa = os.path.join(directorio, archivo)
        
        # Process only text files
        if ruta_completa.endswith('.txt'):
            # Read the content of the text file
            with open(ruta_completa, 'r', encoding='utf-8') as file:
                contenido_archivo = file.read()
            
            # Request a completion from the model using the OpenAI API
            completion = client.chat.completions.create(
                model="ft:gpt-3.5-turbo-1106:infocore::8px4nkMh",
                messages=[
                    {"role": "system", "content": content_instrucciones},
                    {"role": "user", "content": contenido_archivo}
                ]
            )
            
            # Split the response by new lines and write each to the CSV
            lineas = completion.choices[0].message.content.split('\n')
            for linea in lineas:
                escritor_csv.writerow([archivo , linea])

# Calculate and print the total time taken for the process
tiempo_fin = time.time()
print(f"Total time taken: {tiempo_fin - tiempo_inicio} seconds.")
