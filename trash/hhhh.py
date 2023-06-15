# Import necessary libraries
import pytesseract
from PIL import Image

# Open the image file using PIL's Image class
img = Image.open("C:\\Users\\anura\\Documents\\Project_image\\image.png")

# Convert the image to grayscale
img = img.convert('L')

# Use Pytesseract to extract text from the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print(text)
