import cv2
import numpy as np

def create_passport_photo(image_path):
    # Load the image
    img = cv2.imread(image_path)
    
    # Set the desired dimensions for the passport-size photo
    width, height = 2, 2  # In inches (you can adjust these values)
    dpi = 300  # Dots per inch (you can adjust this value)
    
    # Calculate the dimensions in pixels
    width_px = int(width * dpi)
    height_px = int(height * dpi)
    
    # Resize the image while maintaining the aspect ratio
    aspect_ratio = img.shape[1] / img.shape[0]
    if width_px / height_px > aspect_ratio:
        new_width_px = int(height_px * aspect_ratio)
        new_height_px = height_px
    else:
        new_width_px = width_px
        new_height_px = int(width_px / aspect_ratio)
    
    img_resized = cv2.resize(img, (new_width_px, new_height_px))
    
    # Create the violet-white background
    background_color = (238, 130, 238)  # Violet color in BGR format
    background = np.full((height_px, width_px, 3), background_color, dtype=np.uint8)
    
    # Calculate the position to place the resized image at the center
    x_offset = (width_px - img_resized.shape[1]) // 2
    y_offset = (height_px - img_resized.shape[0]) // 2
    
    # Paste the resized image onto the background
    background[y_offset:y_offset + img_resized.shape[0], x_offset:x_offset + img_resized.shape[1]] = img_resized
    
    # Save the resulting passport-size photo
    output_path = "passport_photo.jpg"  # Output file path
    cv2.imwrite(output_path, background)
    
    print("Passport-size photo created successfully!")

# Usage example
image_path = "/Users/andygu/Desktop/preply_umair/Problem Solving/Actually problems/Seventh part/yay.jpeg"  # Replace with your input photo path
create_passport_photo(image_path)
