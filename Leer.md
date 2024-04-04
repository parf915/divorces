# Análisis de Documentos de Divorcio con GPT-3

## Descripción General

Este repositorio contiene scripts en Python diseñados para procesar y analizar texto de documentos de divorcio utilizando GPT-3 de OpenAI. Los scripts convierten documentos PDF en texto, preparan los datos para el afinado fino (fine-tuning), inician el proceso de afinado fino con OpenAI y analizan el texto para extraer información específica utilizando un modelo GPT-3 afinado.

## Contenidos

- `pdf_a_txt.py`: Convierte documentos PDF en archivos de texto.
- `prepare_fine_tune.py`: Sube los datos de entrenamiento para el afinado fino.
- `fine_tuning.py`: Inicia el proceso de afinado fino con OpenAI.
- `model_gpt_divorcios.py`: Analiza el texto de los documentos de divorcio para extraer información estructurada.

## Uso

1. Asegúrese de que todas las dependencias estén instaladas ejecutando `pip install -r requirements.txt`.
2. Coloque los PDFs de divorcio en el directorio especificado.
3. Siga la secuencia de ejecución de los scripts según se indica arriba.
4. Los resultados se mostrarán en un archivo CSV.

## Proceso de Fine-Tuning

Para realizar el afinado fino del modelo GPT con su conjunto de datos, asegúrese de que su archivo en formato JSON Lines cumpla con los siguientes criterios:
- Contiene un mínimo de 10 ejemplos para un aprendizaje efectivo.
- No excede de 100 ejemplos para evitar el sobreajuste.
- Por razones de protección de datos, se han utilizado ejemplos ficticios en esta documentación y se deben utilizar en sus conjuntos de datos donde esté involucrada información sensible.

### Ejemplo de Datos en JSON Lines

A continuación, se muestra un ejemplo de la estructura para una entrada única en JSON Lines utilizada para el afinado fino, incluyendo datos ficticios por motivos de protección de la privacidad:

```json
{"messages": [
  {"role": "user", "content": "Registro Civil - Oficina Registral de Imaginaria | Acta N°: 87654321 | Divorcio Registrado: En la municipalidad de Imaginaria, en fecha 20/07/2024, se ha formalizado el divorcio entre CARLOS SANTANA QUIROGA y ANA MENDOZA BERMUDEZ... Presentación electrónica por el sistema de Registro Civil en línea."},
  {"role": "assistant", "content": "87654321|OFICINA REGISTRAL IMAGINARIA|CARLOS SANTANA QUIROGA|12345678|ANA MENDOZA BERMUDEZ|87654321|20/07/2024"}
]}
