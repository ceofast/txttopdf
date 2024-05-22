# txttopdf
A script to convert WhatsApp chat history to a PDF document, including text and images.

# WhatsApp Chat to PDF Converter

This script converts a WhatsApp chat history from a text file to a PDF document. It includes support for embedding images referenced in the chat.

## Features
- Parses WhatsApp chat history from a text file
- Converts chat history to a PDF document
- Supports embedding images referenced in the chat

## Requirements
- Python 3.x
- fpdf2 library

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/whatsapp-chat-to-pdf.git
    ```
2. Navigate to the project directory:
    ```bash
    cd whatsapp-chat-to-pdf
    ```
3. Install the required libraries:
    ```bash
    pip install fpdf2
   

## Usage
Run the script with the following command:
```bash
python script_name.py path/to/input.txt path/to/images path/to/output.pdf
 ```

## Arguments
**input_file:** Path to the input text file containing WhatsApp chat.
**image_base_path:** Base path for images referenced in the chat.
**output_file:** Path to the output PDF file.
