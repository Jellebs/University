from pathlib import Path
from PIL import Image, ImageGrab
import pytesseract
import sys, os, time
import subprocess
import Quartz.CoreGraphics as cg
from tempfile import NamedTemporaryFile
from AppKit import NSImage, NSPasteboard, NSColor, NSImageRep
import pyperclip
from pypdf import PdfReader
from pix2tex.cli import LatexOCR


arbejdsmappe = "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/Formelsamling/Tekstudtræk/"
billednavn = "MidlertidigtBillede.png"
fil = arbejdsmappe + billednavn
text = ""
        
        
            
def klippetIndhold_gem():
    """Retrieves the copied file path from the macOS clipboard."""
    try:
        # Get the clipboard pasteboard
        img = ImageGrab.grabclipboard()
        img.save(fil)
        return fil 
        
    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        sys.exit(1)

    
def klippetIndhold_udtræk(metode = "Tekst"):
    """Extracts text (including LaTeX) from the given image."""
    try:
        img = Image.open(fil)
        global text
        
        match metode:
            case "Tekst":
                # Metode 1. 
                text = pytesseract.image_to_string(img) 
                 
            case "Latex": 
                # Metode 2.
                model = LatexOCR()
                text = model(img)
                
            case _: 
                # Metode 1. 
                text = pytesseract.image_to_string(img) 
            
        
        # print("\nExtracted Text:\n", text)
        
        # Metode 2.
        # import Formelsamling.Tekstudtræk.Tekstudtræk as tu
        # temp_pdf_path = convert_image_to_pdf(image_path)
        # pdf = PdfReader(temp_pdf_path)
        # text = pdf.pages[0].extract_text()
        # print(pdf.pages[0].extract_text())
        
        
        
    except Exception as e:
        print(f"Error processing image: {e}")

def klippetIndhold_kopier():
    print(text)
    data = text
    subprocess.run("pbcopy", text=True, input=data) 
    pyperclip.copy(str(text))
    spam = pyperclip.paste()

if __name__ == "__main__":
    klippetIndhold_gem()
    klippetIndhold_udtræk(sys.argv[1] if len(sys.argv) > 1 else "Tekst" )
    klippetIndhold_kopier()
    
    




def find_latex_in_image(image_path):
    """Finds LaTeX equations in the given image."""
    try:
        # Convert the image to a PDF
        temp_pdf_path = convert_image_to_pdf(image_path)
        
        # Extract text from the PDF
        text = extract_text_from_pdf(temp_pdf_path)
        
        # Find LaTeX equations in the text
        equations = find_equations_in_text(text)
        
        # Clean up temporary files
        os.remove(temp_pdf_path)
        
        return equations
    
    except Exception as e:
        print(f"Error processing image: {e}")
        sys.exit(1)