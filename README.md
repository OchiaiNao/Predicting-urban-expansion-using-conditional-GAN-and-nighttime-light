# Predicting-urban-expansion-using-conditional-GAN-and-nighttime-light

## Codes Overall README:

### ConditionalGAN.ipynb
Our base model to predict urban NTL expansion. The model is trained, just load the generator and discriminator under ./model_params folder.

### covert_to_mask.py
Use the saved 'animation.gif' to generate binary masks for each pixel.

### combine_masks.py
Use the binary masks to add predictions on the original image.

### [Extracting Motion and Appearance via Inter-Frame Attention for Efficient Video Frame Interpolation] (https://github.com/MCG-NJU/EMA-VFI)
Use the pre-trained model from Zhang, et al.'s research to generate predictions within some time intervals.
