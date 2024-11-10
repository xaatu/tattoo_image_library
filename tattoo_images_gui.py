import random
import os
from tkinter import Tk, Label, Button, Frame
from PIL import Image, ImageTk
from image_functions import tigers, women, flowers, all_images

def pick_random_image(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    if image_files:
        return os.path.join(folder_path, random.choice(image_files))
    else:
        print("No images found in the folder.")
        return None
    



def display_image(image_path):
    if image_path:
        try:
            img = Image.open(image_path)
            img = img.resize((400, 400), Image.LANCZOS)
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk
        except Exception as e:
            print("Error displaying image:", e)
    else:
        print("No image to display.")

def load_all_images():
    image_path = all_images()
    display_image(image_path)

def load_tigers():
    image_path = tigers()
    display_image(image_path)

def load_women():
    image_path = women()
    display_image(image_path)

def load_flowers():
    image_path = flowers()
    display_image(image_path)

# TKINTER
root = Tk()
root.title("Caitlin's Reference Helper")
root.geometry("700x700")
root.configure(bg="black")

# DEFAULT IMAGE
default_image_path = "/Users/sandyquigley/tattoo_image_library/tigerlady.png"
default_image = Image.open(default_image_path)
default_image = default_image.resize((400,400), Image.LANCZOS)
default_image_tk = ImageTk.PhotoImage(default_image)

# IMAGE LABEL
image_label = Label(root, image=default_image_tk)
image_label.image = default_image_tk
image_label.pack(pady=30)

# FRAME FOR CATEGORY BUTTONS
button_frame = Frame(root, bg="black")
button_frame.pack(pady=20)

# CATEGORY BUTTONS
Button(button_frame, text="TIGERS", font=('Mono', 14, "bold"), bg='black', fg='black', relief="raised", pady=1, padx=1, borderwidth=0, highlightthickness=0, command=load_tigers).pack(side="left", padx=10)
Button(button_frame, text="WOMEN", font=('Mono', 14, "bold"), bg='black', fg='black', relief="raised", pady=1, padx=1, borderwidth=0, highlightthickness=0, command=load_women).pack(side="left", padx=10)
Button(button_frame, text="FLOWERS", font=('Mono', 14, "bold"), bg='black', fg='black', relief="raised", pady=1, padx=1, borderwidth=0, highlightthickness=0, command=load_flowers).pack(side="left", padx=10)

# ALL IMAGES & EXIT
Button(root, text="ALL IMAGES", font=('Mono', 14, "bold"), bg='black', fg='black', relief="raised", pady=1, padx=1, borderwidth=0, highlightthickness=0, command=load_all_images).pack(side="bottom", pady=10)
Button(root, text="EXIT", font=('Mono', 14, "bold"), bg='black', fg='black', relief="raised", pady=1, padx=1, borderwidth=0, highlightthickness=0, command=root.quit).pack(side="bottom", pady=10)

root.mainloop()
