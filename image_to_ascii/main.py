import sys 
from utils import convert_image_to_ascii

def main(image_path, new_width=100):
    ascii_image = convert_image_to_ascii(image_path, new_width)
    if ascii_image:
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)
        print("ASCII art written to ascii_image.txt")
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <image_path>")
    else:
        image_path = sys.argv[1]
        main(image_path)