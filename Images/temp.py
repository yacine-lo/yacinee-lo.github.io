from PIL import Image
import numpy as np
import cv2

# Load the image
image_path = "/mnt/data/photo_prof.png"
image = cv2.imread(image_path)

# Convert to grayscale and create a mask
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 1, 255, cv2.THRESH_BINARY)

# Apply the mask to remove the background
background_removed = cv2.bitwise_and(image, image, mask=mask)

# Save the resulting image
output_path = "/mnt/data/photo_no_background.png"
cv2.imwrite(output_path, background_removed)

output_path