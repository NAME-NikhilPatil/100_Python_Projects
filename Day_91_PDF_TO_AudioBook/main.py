from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pdfplumber
from gtts import gTTS
import PyPDF2
import os

Tk().withdraw()  # Hide the main tkinter window
filelocation = askopenfilename()  # Open file dialog to choose the PDF

if not filelocation:  # If no file is selected, exit
    print("No file selected.")
    exit()

# Extract the original file name without the extension
file_name = os.path.basename(filelocation)
name_of_file = os.path.splitext(file_name)[0]  # Get the name only

# Open the PDF file
pdfFileObj = open(filelocation, 'rb')

# Create a PDF reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Get the number of pages
pages = len(pdfReader.pages)

# Extract text from the PDF
with pdfplumber.open(filelocation) as pdf:
    string_of_text = ''
    for i in range(pages):
        page = pdf.pages[i]
        text = page.extract_text()
        if text:  # Ensure text is not None
            string_of_text += text

# Check if any text was extracted
if not string_of_text.strip():
    print("No text could be extracted from the PDF.")
    exit()

# Convert the extracted text to speech
final_file = gTTS(text=string_of_text, lang='en')

# Save the audio file
output_filename = f"(Audio){name_of_file}.mp3"
final_file.save(output_filename)

print(f"Audio file saved as {output_filename}")
