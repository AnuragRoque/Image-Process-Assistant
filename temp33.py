from PIL import Image, ImageDraw, ImageFont
import random

# Set image size and background color
width, height = 600, 300
background_color = (255, 255, 255)

# Set font and text
font_size = 50
text = "Hello, world!"
font = ImageFont.truetype("arial.ttf", font_size)

# Create image and draw object
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Set random pen color
pen_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.text((50, 100), text, font=font, fill=pen_color)

# Save image
image.save("handwritten_text.png")
