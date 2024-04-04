# Divorce Document Analysis with GPT-3

## Overview

This repository contains Python scripts designed to process and analyze text from divorce documents using OpenAI's GPT-3. The scripts convert PDF documents to text, prepare the data for fine-tuning, initiate the fine-tuning process with OpenAI, and analyze the text to extract specific information using a fine-tuned GPT-3 model.

## Contents

- `pdf_a_txt.py`: Converts PDF documents into text files.
- `prepare_fine_tune.py`: Uploads training data for fine-tuning.
- `fine_tuning.py`: Initiates the fine-tuning process with OpenAI.
- `model_gpt_divorcios.py`: Analyzes divorce document text to extract structured information.

## Usage

1. Ensure all dependencies are installed by running `pip install -r requirements.txt`.
2. Place the divorce PDFs in the specified directory.
3. Follow the sequence of script execution as listed above.
4. The results will be outputted in a CSV file.

## Fine-Tuning Process

To fine-tune the GPT model with your dataset, ensure your JSON Lines file meets the following criteria:
- Contains a minimum of 10 examples for effective learning.
- Does not exceed 100 examples to prevent overfitting.
- For data privacy, fictitious examples have been used in this documentation and should be utilized in your datasets where sensitive information is involved.

### Example JSON Lines Data

Below is an example of the structure for a single JSON Line entry used for fine-tuning, including fictitious data for privacy protection:

```json
{"messages": [
  {"role": "user", "content": "Registro Civil - Oficina Registral de Imaginaria | Acta N°: 87654321 | Divorcio Registrado: En la municipalidad de Imaginaria, en fecha 20/07/2024, se ha formalizado el divorcio entre CARLOS SANTANA QUIROGA y ANA MENDOZA BERMUDEZ... Presentación electrónica por el sistema de Registro Civil en línea."},
  {"role": "assistant", "content": "87654321|OFICINA REGISTRAL IMAGINARIA|CARLOS SANTANA QUIROGA|12345678|ANA MENDOZA BERMUDEZ|87654321|20/07/2024"}
]}
