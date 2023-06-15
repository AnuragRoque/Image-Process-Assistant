# Import necessary libraries
import cv2
import numpy as np
from PIL import Image
import ocrolib

# Load the image
img = cv2.imread('image.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to obtain a binary image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Invert the binary image
thresh = cv2.bitwise_not(thresh)

# Convert the binary image to a PIL image
pil_img = Image.fromarray(thresh)

# Use OCRopus to extract text from the image
text = ocrolib.recognize(pil_img)

# Print the extracted text
print(text)
