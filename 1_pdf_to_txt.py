import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import re

# Setting the path for the tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

def contiene_palabra(texto, palabra):
    """
    Check if the exact word (palabra) exists in the given text (texto),
    ignoring case sensitivity.
    """
    return re.search(r'\b' + re.escape(palabra) + r'\b', texto, re.IGNORECASE) is not None

def extraer_texto_de_pagina(pagina):
    """
    Extract text from a given page object (pagina).
    If no text is found, attempt OCR on the page images.
    """
    texto_pagina = pagina.get_text()
    if texto_pagina.strip():
        return texto_pagina
    else:
        texto_imagen = ""
        for img_index, img in enumerate(pagina.get_images(full=True)):
            xref = img[0]
            pix = fitz.Pixmap(pagina.parent, xref)
            if pix.n - pix.alpha < 4:  # This condition checks if the image is not CMYK or does not have an alpha channel.
                try:
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    imagen = Image.frombytes("RGB", [pix1.width, pix1.height], pix1.samples)
                    texto_imagen += pytesseract.image_to_string(imagen)
                finally:
                    pix1 = None  # Release resources of the pixmap
            pix = None  # Release resources of the pixmap
        return texto_imagen

def procesar_pdfs_en_carpeta(carpeta_pdf, carpeta_destino, palabra_clave):
    """
    Process all PDF files within a given directory (carpeta_pdf), 
    extract text from each page, and write the text to new files 
    in the destination directory (carpeta_destino).
    """
    for archivo in os.listdir(carpeta_pdf):
        if archivo.lower().endswith(".pdf"):
            ruta_pdf = os.path.join(carpeta_pdf, archivo)
            texto_acumulado = ""

            with fitz.open(ruta_pdf) as doc:
                for pagina in doc:
                    texto_pagina = extraer_texto_de_pagina(pagina)
                    texto_acumulado += texto_pagina

            # Define the text file name using the PDF's base name
            nombre_archivo_texto = f"{os.path.splitext(archivo)[0]}.txt"
            ruta_archivo_texto = os.path.join(carpeta_destino, nombre_archivo_texto)
            
            # Write the accumulated text to a file in the destination directory
            with open(ruta_archivo_texto, 'w') as archivo_texto:
                archivo_texto.write(texto_acumulado)
            print(f"Texto completo guardado en {ruta_archivo_texto}")

# Paths to the directories containing the PDFs and destination for text files
carpeta_pdf = '/Users/renzo/Downloads/divorcios'
carpeta_destino = '/Users/renzo/Downloads/divorcios_txt'

# The keyword to search for within the PDFs is not used in this script and could be removed
palabra_clave = ' '

# Processing the PDFs by calling the function with specified directories
procesar_pdfs_en_carpeta(carpeta_pdf, carpeta_destino, palabra_clave)
