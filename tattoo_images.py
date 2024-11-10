import random
from PIL import Image 
from image_functions import tigers, women, flowers, all_images



def display_menu():
    print("\nReference Image Picker")
    print("1. All Images")
    print("2. Tigers")
    print("3. Women")
    print("4. Flowers")
    print("9. Exit")


def display_image(image_path):
    if image_path:
        try:
            print("Displaying image:", image_path)
            img = Image.open(image_path)
            img.show()
        except Exception as e:
            print("Error displaying image:", e)
    else:
        print("No image to display.")
    

# MAIN 
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ")

        if choice == '9':
            print("Exiting...")
            break

        elif choice == '1':
            image_path = all_images()
            display_image(image_path)

        elif choice == '2':
            image_path = tigers()
            display_image(image_path)

        elif choice == '3':
            image_path = women()
            display_image(image_path)

        elif choice == '4':
            image_path = flowers()
            display_image(image_path)

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
