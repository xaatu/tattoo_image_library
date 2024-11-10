import os
import random

def all_images():
    folder_path = "/Users/sandyquigley/tattoo_image_library/images/all_images"
    return pick_random_image(folder_path)

def tigers():
    folder_path = "/Users/sandyquigley/tattoo_image_library/images/tigers"
    return pick_random_image(folder_path)

def women():
    folder_path = "/Users/sandyquigley/tattoo_image_library/images/women"
    return pick_random_image(folder_path)

def flowers():
    folder_path = "/Users/sandyquigley/tattoo_image_library/images/flowers"
    return pick_random_image(folder_path)

# PICK RANDOM IMAGE FUNCTION
def pick_random_image(folder_path):
    try:
        image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
        if not image_files:
            print(f"No images found in {folder_path}")
            return None
        random_image = random.choice(image_files)
        full_path = os.path.join(folder_path, random_image)
        print("Random image selected:", full_path)
        return full_path
    except FileNotFoundError:
        print(f"Folder {folder_path} not found.")
        return None

