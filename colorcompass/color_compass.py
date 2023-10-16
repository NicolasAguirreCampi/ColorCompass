from .color_dictionary import dictionary

import re
import math

def get_color_name(color):
    """
    Gets the color name of a given color code.

    Parameters:
    - color: A string or tuple representing a color in hexadecimal or RGB format.

    Returns:
    - str: A string indicating the detected color.
    """
    format = detect_color_format(color)

    # Always work with rgb
    if format == "hexadecimal":
        color = translate_hex_to_rgb(color)

    min_distance = float('inf')  # Begins with infinite to ensure that any calculated distance will be lower.
    color_name = None
    
    # Iterates through colors and its variants
    for name, variants in dictionary.items():
        for variant in variants:
            distance = math.sqrt(
                (color[0] - variant[0])**2 +
                (color[1] - variant[1])**2 +
                (color[2] - variant[2])**2
            )
            # If this variant is closer to the current closest, update
            if distance < min_distance:
                min_distance = distance
                color_name = name
    
    return color_name

def translate_hex_to_rgb(hexadecimal):
    """
    Convert a hexadecimal color string to an RGB tuple.

    Parameters:
    - hexadecimal (str): A string representing a color in hexadecimal format. 
      It should start with '#' and be followed by 6 hexadecimal digits.

    Returns:
    - tuple: An (r, g, b) tuple with the decimal values of the RGB components.
    """

    # Remove '#' char
    hexadecimal = hexadecimal.lstrip('#')
    
    # If the longitud is 3, convert it from short hexadecimal #RGB into a normal hexadecimal #RRGGBB
    if len(hexadecimal) == 3:
        hexadecimal = ''.join([char*2 for char in hexadecimal])
    
    # Translation to RGB
    print(f"hexadecimal: {hexadecimal} ~ rgb: {tuple(int(hexadecimal[i:i+2], 16) for i in (0, 2, 4))}")
    return tuple(int(hexadecimal[i:i+2], 16) for i in (0, 2, 4))

def detect_color_format(color):
    """
    Detects the format of a given color representation.

    Parameters:
    - color: A string or tuple representing a color in hexadecimal or RGB format.

    Returns:
    - str: A string indicating the detected format ("hex" or "rgb"), or None if the format could not be determined.
    """
    # Hexadecimal case
    if isinstance(color, str):
        hex_pattern = re.compile(r'^#([0-9a-fA-F]{3}){1,2}$')
        if hex_pattern.match(color):
            return "hexadecimal"
    
    # RGB case
    elif isinstance(color, (tuple, list)) and len(color) == 3:
        if all(isinstance(value, int) and 0 <= value <= 255 for value in color):
            return "rgb"
    
    # Rise an error if is none of the above
    raise ValueError("Input should be a hexadecimal string in the format '#RRGGBB' or an rgb tuple in the format [R,G,B]")