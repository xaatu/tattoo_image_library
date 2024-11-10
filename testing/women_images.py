import glob
import random
import os

def women():

    path = "/Users/sandyquigley/tattoo_image_library/images/women"   

    all_png = glob.glob(os.path.join(path, "*.png"))
    all_jpg = glob.glob(os.path.join(path, "*.jpg"))
    all_jpeg = glob.glob(os.path.join(path, "*.jpeg"))

    all_images = all_jpg + all_png + all_jpeg

    if all_images:
        rand_image = random.choice(all_images)
        print(rand_image)
    else:
        print("No images found in the specified directory.")

