# Import modules
from PIL import Image
import pytesseract
 
# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
 
# Create an image object of PIL library
image = Image.open('F:/imagess.jpg')
 
# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')
 
# Print the text
print(image_to_text)
