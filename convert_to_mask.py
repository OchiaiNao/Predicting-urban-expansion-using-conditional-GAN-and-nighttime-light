from PIL import Image, ImageOps
import numpy as np
import os

def gif_to_frames(gif_path, output_folder, threshold=128):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    gif = Image.open(gif_path)
    frame_num = 0
    while gif:
        frame = gif.copy()
        frame.save(os.path.join(output_folder, f'./frames/frame{frame_num:03d}.png'))

        frame_array = np.array(frame)
        binary_mask = np.where(frame_array > threshold, 255, 0).astype(np.uint8)
        binary_mask_image = Image.fromarray(binary_mask)
        binary_mask_image.save(os.path.join(output_folder, f'./binary_masks/binary_mask{frame_num:03d}.png'))

        frame_num += 1
        try:
            gif.seek(gif.tell() + 1)
        except EOFError:
            break

# Replace 'input.gif' with the path to your input GIF file
# Replace 'output' with the path to your desired output folder
gif_to_frames('90_class9.gif', 'mask_coversion')
