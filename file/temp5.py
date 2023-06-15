# Import the following modules
import pytesseract
from PIL import Image
import os
import pywhatkit
pywhatkit.start_server()

# Change the directory to the
# location where image is present
os.chdir(r"C:\Users\anura\Pictures")

# Set the Path of Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\anura\Documents\Project_image\Tesseract-OCR\tesseract.exe"

# Load the Image
img = Image.open("VID_20210504_030225.mp4_snapshot_13.28.312.png")

# Convert Image to Text
text = pytesseract.image_to_string(img)

# Convert Text to Hand Written Text
pywhatkit.text_to_handwriting(text, rgb=[0, 0, 250])
