# Favicon Generator

This Python script (`favicon-generator.py`) allows you to generate standard favicon images (favicon.ico, apple-touch-icon.png, favicon-16x16.png, favicon-32x32.png) from an input image. It can be helpful for creating favicons for your website or web application.

## Prerequisites

- Python (3.6 or higher)
- `Pillow` library (for image manipulation)

You can install the `Pillow` library using pip:

```shell
pip install Pillow
```

## Usage

1. Place the input image file you want to use for generating favicons in the same directory as the script.

2. Run the `favicon-generator.py` script using Python with the following command:

   ```shell
   python favicon-generator.py input_image.png
   ```

   - `input_image.png`: Path to the input image file.

3. The script will generate the following favicon files in the current directory:
   - `favicon.ico` (for Windows)
   - `apple-touch-icon.png` (for iOS)
   - `favicon-16x16.png` (for most browsers)
   - `favicon-32x32.png` (for most browsers)

## Example

```shell
python favicon-generator.py my_logo.png
```

In this example, the script will create standard favicon files using `my_logo.png` as the input image.

## Supported Image Formats

The script supports various image formats as input, including but not limited to PNG, JPEG, and GIF.
