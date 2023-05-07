from PIL import Image
import numpy as np

def add_white_pixels(image_path, mask_path, output_path):
    image = Image.open(image_path)
    mask = Image.open(mask_path)

    if image.size != mask.size:
        raise ValueError("Image and mask must have the same dimensions")

    image_array = np.array(image)
    mask_array = np.array(mask)

    # Set image pixels to white (255, 255, 255) where the mask is white (255)
    combined_array = np.where(mask_array == 255, 255, image_array)

    combined_image = Image.fromarray(combined_array).convert('L')
    combined_image.save(output_path)

# Replace 'image.png', 'mask.png', and 'output.png' with the paths to your input image,
# binary mask, and desired output file, respectively.

# image.png, mask.png, output.png
add_white_pixels('./output/night_time_1.jpg', './mask_conversion/binary_masks/binary_mask077.png', './combined_prediction/label9_predict.png')
