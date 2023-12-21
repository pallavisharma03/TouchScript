import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from PIL import Image, ImageDraw
from PIL import Image, ImageOps
import numpy as np
import sys

# Create a Tkinter window
root = tk.Tk()
root.title("Text and Image Processing")

# Function to get text input and display output
def process_text():
    text = text_entry.get("1.0", tk.END).strip() 

    # Braille patterns for each letter in a 2x3 grid
    braille_dict = {
        'A': [1,0,0,0,0,0],
        'B': [1,0,1,0,0,0],
        'C': [1,1,0,0,0,0],
        'D': [1,1,0,1,0,0],
        'E': [1,0,0,1,0,0],
        'F': [1,1,1,0,0,0],
        'G': [1,1,1,1,0,0],
        'H': [1,0,1,1,0,0],
        'I': [0,1,1,0,0,0],
        'J': [0,1,1,1,0,0],
        'K': [1,0,0,0,1,0],
        'L': [1,0,1,0,1,0],
        'M': [1,1,0,0,1,0],
        'N': [1,1,0,1,1,0],
        'O': [1,0,0,1,1,0],
        'P': [1,1,1,0,1,0],
        'Q': [1,1,1,1,1,0],
        'R': [1,0,1,1,1,0],
        'S': [0,1,1,0,1,0],
        'T': [0,1,1,1,1,0],
        'U': [1,0,0,0,1,1],
        'V': [1,0,1,0,1,1],
        'W': [0,1,1,1,0,1],
        'X': [1,1,0,0,1,1],
        'Y': [1,1,0,1,1,1],
        'Z': [1,0,0,1,1,1],

        ' ': [0,0,0,0,0,0],

        '#': [0,1,0,1,1,1],  # Number indicator
        '1': [1,0,0,0,0,0],
        '2': [1,0,1,0,0,0],
        '3': [1,1,0,0,0,0],
        '4': [1,1,0,1,0,0],
        '5': [1,0,0,1,0,0],
        '6': [1,1,1,0,0,0],
        '7': [1,1,1,1,0,0],
        '8': [1,0,1,1,0,0],
        '9': [0,1,1,0,0,0],
        '0': [0,1,1,1,0,0],

        ',': [0,0,1,0,0,0],  # Comma
        ';': [0,0,1,0,1,0],  # Semicolon
        ':': [0,0,1,1,0,0],  # Colon
        '.': [0,0,1,1,0,1],  # Period
        '?': [0,0,1,0,1,1],  # Question mark
        '!': [0,0,1,1,1,0],  # Exclamation mark
        '-': [0,0,0,0,1,1]   # Hyphen
    }

    # Constants for the display
    num_rows = 10
    num_columns = 20
    num_dots = num_rows * num_columns
    dot_states = [0] * num_dots  # Initialize all dots as lowered

    def render_braille_string(user_input):
        rows = [''] * 3  # Initialize rows for 3 Braille rows
        display = []  # Initialize the display grid
        row_count = 0  # Track the row count
        columns = 0
        for char in user_input:
            if row_count >= num_rows:
                break  # Break if the text exceeds the display height
            if char.upper() in braille_dict:
                pattern = braille_dict[char.upper()]
                for i in range(3):
                    for j in range(2):
                        if pattern[i * 2 + j] == 1:
                            rows[i] += '◉ '
                        else:
                            rows[i] += '◌ '  # Use '◌ ' for empty spaces
                        columns += 2  # Increment by 2 for each character printed
                if len(rows[0]) > num_columns * 2:  # Update the condition for columns
                    display.extend(rows)  # Add the rows to the display grid
                    rows = [''] * 3  # Reset rows for the next set of characters
                    row_count += 3  # Move to the next row
        if any(rows):
            display.extend(rows)  # Add the last set of characters if any remain
        # Ensure the display doesn't exceed the defined grid size
        display = display[:num_rows]
        # Fill any remaining space in the rows with '◌ '
        for i in range(len(display)):
            while len(display[i]) < num_columns * 2:  # Update to match the number of columns
                display[i] += '◌ '
        while len(display) < num_rows:  # Ensure all 10 rows exist
            display.append('◌ ' * num_columns * 2)  # Add '◌ ' for empty rows
        # Print the display grid
        for row in display:
            print(row[:num_columns * 2])  # Trim to fit within the defined columns

    modified_string = ''
    for char in text:
        if char.isdigit():
            modified_string += '#' + char
        else:
            modified_string += char

    if len(modified_string) < 30:
      render_braille_string(modified_string)
    else:
      print("Enter a string less than length 30")



# Function to get image input and display output
def process_image():

    file_path = filedialog.askopenfilename()  # Open a file dialog to select an image
    if file_path:
        image = Image.open(file_path)

    # Convert the image to grayscale
    image_gray = ImageOps.grayscale(image)

    threshold = 100  # Adjust this threshold value if needed
    binary_image = image_gray.point(lambda p: 0 if p < threshold else 255)

    # Find bounding box of the black outlines
    bbox = binary_image.getbbox()

    # Crop the image to the bounding box area
    cropped_image = image.crop(bbox)

    # Define the tactile board dimensions
    tactile_width = 20
    tactile_height = 10

    # Calculate the aspect ratio of the cropped image
    aspect_ratio = cropped_image.width / cropped_image.height

    # Calculate the new dimensions to fit within 20 columns and 10 rows
    new_width = int(tactile_height * aspect_ratio)
    new_height = int(tactile_width / aspect_ratio)

    # Check which dimension (width or height) needs to be reduced to fit within the tactile board
    if new_width > tactile_width:
        resized_width = tactile_width
        resized_height = int(resized_width / aspect_ratio)
    else:
        resized_height = tactile_height
        resized_width = int(resized_height * aspect_ratio)

    # Resize the image while maintaining aspect ratio and fitting within 20 columns and 10 rows
    resized_image = cropped_image.resize((resized_width, resized_height))

    # Display the resized image or perform further processing...
    # You can use this resized_image for creating a tactile representation as shown in previous examples.

    def contrast_stretching(image_array):
        lower_percentile = 5  # Adjust these percentiles for more aggressive contrast enhancement
        upper_percentile = 95

        # Calculate the percentiles
        lower_value = np.percentile(image_array, lower_percentile)
        upper_value = np.percentile(image_array, upper_percentile)

        # Perform contrast stretching
        stretched_image = np.clip((image_array - lower_value) * 255.0 / (upper_value - lower_value), 0, 255).astype(np.uint8)
        return Image.fromarray(stretched_image)

    import numpy as np
    stretched_image = contrast_stretching(resized_image)
    stretched_image.save('stretched_image.png')

    def create_tactile_representation(image):
        tactile_representation = []

        # Define tactile board dimensions
        tactile_width = 20
        tactile_height = 10

        # Calculate the step size for sampling the image
        step_x = max(1, image.width // tactile_width)
        step_y = max(1, image.height // tactile_height)

        for y in range(0, image.height, step_y):
            row = []
            for x in range(0, image.width, step_x):
                # Sample the pixel value based on step size
                pixel_value = image.getpixel((x, y))

                # If the pixel is close to black (border), use a raised dot; otherwise, use a lowered dot
                if isinstance(pixel_value, tuple):  # Check if pixel_value is a tuple
                    pixel_value = pixel_value[0]  # Take the first value if it's a tuple
                if pixel_value < 100:
                    row.append('◉')  # Raised dot representation
                else:
                    row.append('◌')  # Lowered dot representation

            # Ensure the row matches the tactile_width
            while len(row) < tactile_width:
                row.append('◌')  # Add extra spaces for the remaining columns if needed

            tactile_representation.append(row)

            # Ensure the tactile representation matches the tactile_height
            if len(tactile_representation) >= tactile_height:
                break

        # Ensure the tactile representation matches the tactile_height
        tactile_representation = tactile_representation[:tactile_height]

        return tactile_representation

    # Create the tactile representation of the enhanced image
    tactile_image = create_tactile_representation(stretched_image)

    # Display the tactile representation
    for row in tactile_image:
        print(' '.join(row))

def refresh_terminal():
    # Clear the terminal or console screen
    if sys.platform.startswith('win'):
        import subprocess
        subprocess.run("cls", shell=True)  # For Windows
    else:
        print("\033c", end="")  # For Unix/Linux/MacOS

# Text input area
text_entry = tk.Text(root, height=5, width=30)
text_entry.pack()

# Button for text processing
text_button = tk.Button(root, text="Process Text", command=process_text)
text_button.pack()

# Button for image processing
image_button = tk.Button(root, text="Process Image", command=process_image)
image_button.pack()

refresh_button = tk.Button(root, text="Refresh Terminal", command=refresh_terminal)
refresh_button.pack()

# Run the Tkinter main loop
root.mainloop()
