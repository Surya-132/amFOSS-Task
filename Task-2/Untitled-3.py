import pytesseract
from PIL import Image

# Set the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
#Since I originally did this in windows, this was needed but it's not needed in Ubuntu when using a virtual environment.

# Path to your image file
image_path = '/home/krishna-surya/Desktop/Tasks/Task-2/math_expression.png'

# Open the image and extract text
image = Image.open(image_path)
extracted_text = pytesseract.image_to_string(image)

print("Extracted Text:", extracted_text)
print("Answer = ",eval(extracted_text))
