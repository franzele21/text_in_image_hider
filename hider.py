from PIL import Image
from unidecode import unidecode
import math
import sys

OUTPUT_FILE_NAME = "outfile.png"

def change_last_digit(number: int, last_digit: int|str) -> int:
    """
This function changes the last digit of a number, and keep it less 
than 255

Parameters
----------
number : int
    The original number, from which the last digit needs to the 
changed
last_digit : int
    The digit that will replace the last digit from number

Returns
-------
int
    The number with the last digit replaced
    """
    new_number = int(str(number)[:-1] + str(last_digit))
    new_number = new_number if new_number <= 255 else new_number-10
    return new_number

def add_zeros(number: int, limit: int=3) -> str:
    """
Add zeros to the left side

Parameters
----------
number : int
    Number on which the zeros will be added
limit : int
    Limit of the size of the final number

Returns
-------
str
    Number with zeros on the left side, smaller than limit
    """
    number = str(number)
    while len(number)<limit:
        number = "0" + number

    return number

def create_image(filename: str, text: str) -> None:
    image = Image.open(filename)
    pixels = list(image.getdata())
    width, height = image.size

    if len(pixels)-3 > len(text)*3:
        first_pixel = pixels[0]
        verif_value = first_pixel[0]%10

        new_first_pixel = []
        for color in first_pixel:
            new_color = change_last_digit(color, verif_value)
            new_first_pixel.append(new_color)
        pixels[0] = tuple(new_first_pixel)

        word_distance = len(pixels) / len(text)
        word_distance = math.floor(word_distance)
        word_distance = min(999, word_distance)
        word_distance = add_zeros(word_distance)
        print(word_distance)

        second_pixel = pixels[1]
        
        new_second_pixel = []
        for index, color in enumerate(second_pixel):
            new_color = change_last_digit(color, int(word_distance[index]))
            new_second_pixel.append(new_color)
        pixels[1] = tuple(new_second_pixel)

        text = iter(text)

        etf = False
        new_pixels = []
        for index, pixel in enumerate(pixels):
            if index%int(word_distance) == 0 and not etf and index > 2:
                try:
                    letter = next(text)
                    letter_id = ord(letter)
                    if letter_id > 999:
                        letter_id = ord(unidecode.unidecode(letter))
                    letter_id = add_zeros(letter_id)

                    pixel = (
                        change_last_digit(pixel[0], letter_id[0]),
                        change_last_digit(pixel[1], letter_id[1]),
                        change_last_digit(pixel[2], letter_id[2])
                    )
                    
                except StopIteration:
                    etf_unicode_id = "003"
                    pixel = (
                        change_last_digit(pixel[0], etf_unicode_id[0]),
                        change_last_digit(pixel[1], etf_unicode_id[1]),
                        change_last_digit(pixel[2], etf_unicode_id[2])
                    )
                    etf = True
            new_pixels.append(pixel)
        
        new_image = Image.new("RGB", (width, height))
        new_image.putdata(new_pixels)
        print(new_pixels[0])
        new_image.save(OUTPUT_FILE_NAME)

if __name__ == '__main__':
    image_file = sys.argv[1]
    text = sys.argv[2]
    create_image(image_file, text)