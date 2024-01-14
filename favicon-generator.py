import sys
from PIL import Image

def generate_favicons(input_image_path):
    try:
        # Open the input image
        img = Image.open(input_image_path)

        # Favicon.ico (Windows)
        img.save("favicon.ico")

        # Apple Touch Icon (iOS)
        img.save("apple-touch-icon.png")

        # Favicon 16x16 (Most browsers)
        img.save("favicon-16x16.png", size=(16, 16))

        # Favicon 32x32 (Most browsers)
        img.save("favicon-32x32.png", size=(32, 32))

        print("Favicons generated successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_favicons.py input_image.png")
        sys.exit(1)

    input_image_path = sys.argv[1]

    generate_favicons(input_image_path)
