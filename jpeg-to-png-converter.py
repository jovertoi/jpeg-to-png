from PIL import Image
import os

def read_jpeg_file(file_path):
    try:
        return Image.open(file_path)
    except IOError:
        print(f"Error: Unable to read the file {file_path}")
        return None

def convert_to_png(image):
    try:
        return image.convert("RGB")
    except Exception as e:
        print(f"Error: Unable to convert the image. {str(e)}")
        return None

def save_png_file(image, output_path):
    try:
        image.save(output_path, "PNG")
        print(f"PNG file saved successfully: {output_path}")
        return True
    except Exception as e:
        print(f"Error: Unable to save the PNG file. {str(e)}")
        return False

def main():
    input_file = input("Enter the path to the JPEG file: ")
    
    if not os.path.exists(input_file):
        print("Error: File not found.")
        return

    image = read_jpeg_file(input_file)
    if image is None:
        return

    png_image = convert_to_png(image)
    if png_image is None:
        return

    output_file = os.path.splitext(input_file)[0] + ".png"
    if save_png_file(png_image, output_file):
        print("Conversion completed successfully.")
    else:
        print("Conversion failed.")

if __name__ == "__main__":
    main()
