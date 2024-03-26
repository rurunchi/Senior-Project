import pandas as pd
from PIL import Image
import numpy as np

def get_colors(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Convert the image to RGB mode
    image = image.convert('RGB')

    # Resize the image for faster processing (optional)
    width, height = image.size
    aspect_ratio = width / height
    new_height = 100
    new_width = int(new_height * aspect_ratio)
    image = image.resize((new_width, new_height))

    # Convert the image to a NumPy array
    image_array = np.array(image)

    # Reshape the array to a 2D array of pixels
    pixels = image_array.reshape(-1, 3)

    # Get unique colors
    unique_colors = np.unique(pixels, axis=0)

    return unique_colors

def rgb_to_html(rgb):
    # Convert RGB values to hexadecimal format
    hex_color = '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    return hex_color

def main():
    # Prompt user to enter the path to the image file
    image_path = input("Please enter the path to the image file: ")

    # Get colors from the image
    colors = get_colors(image_path)

    # Create a DataFrame to store the colors
    color_data = []
    for color in colors:
        html_color = rgb_to_html(color)
        color_data.append({'RGB': color, 'HTML': html_color})
    df = pd.DataFrame(color_data)

    # Write the data to an Excel file
    excel_file = 'colors.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"Color data saved to {excel_file}")

if __name__ == "__main__":
    main()
