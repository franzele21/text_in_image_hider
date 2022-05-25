from PIL import Image


def get_last_character(pixel):
    return str(pixel[0])[-1] + str(pixel[1])[-1] + str(pixel[2])[-1]

image = Image.open("output.png")
pixels = list(image.getdata())

first_pixel = pixels[0]
if str(first_pixel[0])[-1] == str(first_pixel[1])[-1] \
        and str(first_pixel[0])[-1] == str(first_pixel[2])[-1]:
    second_pixel = pixels[1]
    
    word_distance = get_last_character(second_pixel)
    word_distance = int(word_distance)

    text = ""
    for index, pixel in enumerate(pixels):
        if index%word_distance == 0 \
                and index != 0:
            text += chr(int(get_last_character(pixel)))
            if get_last_character(pixel) == "003":
                break
print(text)