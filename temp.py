import cv2
import numpy as np

def compare_images(image1_path, image2_path):
    # Load the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Convert the images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate the SSIM between the two images
    ssim = cv2.compare_ssim(gray1, gray2)

    # Return the similarity percentage (SSIM ranges from -1 to 1)
    similarity_percentage = (ssim + 1) / 2 * 100
    return similarity_percentage

# Example usage:
image1_path = 'a.png'
image2_path = 'b.png'
similarity_percentage = compare_images(image1_path, image2_path)
print(f'The similarity between the images is {similarity_percentage:.2f}%')
