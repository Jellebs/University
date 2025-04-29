from pathlib import Path
from PIL import Image
import pytesseract
import sys
import subprocess

def get_clipboard_path():
    """Retrieves the copied file path from the macOS clipboard."""
    try:
        # Run AppleScript to get the copied file path
        clipboard_content = subprocess.run(
            ["osascript", "-e", 'try\ntell application "Finder" to get POSIX path of (selection as alias)\non error\nend try'],
            capture_output=True,
            text=True
        ).stdout.strip()

        if clipboard_content and Path(clipboard_content).exists():
            return clipboard_content
        else:
            print("No valid file found in clipboard.")
            sys.exit(1)

    except Exception as e:
        print(f"Error accessing clipboard: {e}")
        sys.exit(1)

def extract_text_from_image(image_path):
    """Extracts text (including LaTeX) from the given image."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print("\nExtracted Text:\n", text)
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    file_path = get_clipboard_path()
    print(f"Processing file: {file_path}")
    extract_text_from_image(file_path)