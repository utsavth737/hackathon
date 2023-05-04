from PIL import Image
import math

def compare_jpeg_files(file1_path, file2_path):
    img1 = Image.open(file1_path)
    img2 = Image.open(file2_path)

    if img1.size != img2.size or img1.mode != img2.mode:
        return 0.0

    # Get the pixels of both images
    pixels1 = img1.load()
    pixels2 = img2.load()

    # Calculate the Root Mean Square Error
    sum_of_squares = 0.0
    for x in range(img1.width):
        for y in range(img1.height):
            r1, g1, b1 = pixels1[x, y]
            r2, g2, b2 = pixels2[x, y]
            sum_of_squares += (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2
    rms = math.sqrt(sum_of_squares / (img1.width * img1.height * 3))

    # Calculate the percentage of similarity
    max_pixel_value = 255.0
    similarity_percentage = (max_pixel_value - rms) / max_pixel_value * 100.0

    return similarity_percentage

sp=compare_jpeg_files(input("enter image 1: "),input("enter image 2: "))
print("the given two images are",sp,"% similar")
