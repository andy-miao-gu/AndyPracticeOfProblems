import cv2
import numpy as np

# Load the Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image file paths
image_paths = [ 'ho.jpg']  # Add your image paths here

# Load the glasses image
glasses_image = cv2.imread('glasses.png', -1)  # Add the path to the glasses image

for image_path in image_paths:
    # Read the input image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Resize the glasses image to fit the face width
        resized_glasses = cv2.resize(glasses_image, (w, int(0.5 * h)))

        # Calculate the position to place the glasses
        x1 = x
        x2 = x + w
        y1 = y + int(0.35 * h)
        y2 = y1 + int(0.5 * h)

        # Ensure the glasses fit within the image dimensions
        if x1 >= 0 and x2 <= image.shape[1] and y1 >= 0 and y2 <= image.shape[0]:
            # Create a mask for the glasses
            glasses_mask = resized_glasses[:, :, 3]

            # Invert the glasses mask
            glasses_mask_inv = cv2.bitwise_not(glasses_mask)

            # Extract the region of interest (ROI) for the glasses from the input image
            roi = image[y1:y2, x1:x2]

            # Mask out the region of interest
            roi_bg = cv2.bitwise_and(roi, roi, mask=glasses_mask_inv)

            # Take only the region of interest from the glasses image
            roi_fg = cv2.bitwise_and(resized_glasses[:, :, :3], resized_glasses[:, :, :3], mask=glasses_mask)

            # Combine the background and foreground of the ROI
            dst = cv2.add(roi_bg, roi_fg)

            # Place the modified ROI back into the original image
            image[y1:y2, x1:x2] = dst

    # Display the result
    cv2.imshow('Glasses', image)
    cv2.waitKey(0)

# Close the windows
cv2.destroyAllWindows()
