from PIL import Image

# ASCII characters in increasing order of intensity
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)
    return characters

def main():
    path = input("Enter image path: ")
    try:
        image = Image.open(path)
    except:
        print("Image not found.")
        return
    
    image = resize_image(image)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)
    img_width = image.width
    
    ascii_str_len = len(ascii_str)
    ascii_img = "\n".join(ascii_str[i:(i+img_width)] for i in range(0, ascii_str_len, img_width))
    
    print(ascii_img)
    
    # Save to file
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_img)
    print("✅ ASCII art saved as ascii_image.txt")

main()
