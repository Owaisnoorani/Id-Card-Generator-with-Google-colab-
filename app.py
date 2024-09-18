from PIL import Image, ImageDraw, ImageFont
from google.colab import files
from IPython.display import display
from io import BytesIO
import requests

# Function to generate ID card
def generate_id_card(photo, name, roll_no, city, center, campus, day_time, batch):
    # Create a blank white ID card
    card_width = 500
    card_height = 300
    card = Image.new('RGB', (card_width, card_height), color='white')
    draw = ImageDraw.Draw(card)
    
    # Load the user's photo and resize it
    photo = Image.open(BytesIO(photo))
    photo = photo.resize((100, 100))  # Resize photo to fit on the card
    card.paste(photo, (350, 30))  # Paste photo on the card
    
    # Load a bold, simple font
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    except IOError:
        # Fallback to default font if the specified font is not available
        font = ImageFont.load_default()  # Using default font as a fallback
    
    # Add ID Card Text
    draw.text((20, 30), f"Name: {name}", font=font, fill="black")
    draw.text((20, 70), f"Roll No: {roll_no}", font=font, fill="black")
    draw.text((20, 110), f"City: {city}", font=font, fill="black")
    draw.text((20, 150), f"Center: {center}", font=font, fill="black")
    draw.text((20, 190), f"Campus: {campus}", font=font, fill="black")
    draw.text((20, 230), f"Days / Time: {day_time}", font=font, fill="black")
    draw.text((20, 270), f"Batch: {batch}", font=font, fill="black")
    
    # Add border to the card
    draw.rectangle([(10, 10), (card_width-10, card_height-10)], outline="black", width=3)

    # Save ID card
    card.save('/content/id_card_generated.png')
    return '/content/id_card_generated.png'

# Function to display input form
def input_details():
    name = input("Enter your name: ")
    roll_no = input("Enter your Roll No: ")
    city = input("Enter your City: ")
    center = input("Enter your Center: ")
    campus = input("Enter your Campus: ")
    day_time = input("Enter Day/Time: ")
    batch = input("Enter your Batch: ")
    
    return name, roll_no, city, center, campus, day_time, batch

# Collect user input
name, roll_no, city, center, campus, day_time, batch = input_details()

# Upload the photo
print("Please upload a photo for the ID card.")
uploaded = files.upload()

# Get the photo file from the uploaded files
photo = next(iter(uploaded.values()))  # Get the first uploaded file content

# Generate the ID card
id_card_path = generate_id_card(photo, name, roll_no, city, center, campus, day_time, batch)

# Display the generated ID card
display(Image.open(id_card_path))

# Provide download link for the ID card
files.download(id_card_path)
