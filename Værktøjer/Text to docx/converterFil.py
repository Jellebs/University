from pdf2docx import Converter
from PIL import Image
import pytesseract
import os

# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

dir = "Text to docx"

myconfig = r"--psm 11 --oem 3"

from PIL import Image

# Open the image file
image = Image.open(f'{dir}/picture3.png')

# Perform OCR using PyTesseract
text = pytesseract.image_to_string(image, config = myconfig, lang='eng')
# text = pytesseract.image_to_string(cropped_img_loc, config=myconfig, lang='eng')
# Print the extracted text
print(text)

