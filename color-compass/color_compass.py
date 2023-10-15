from color_dictionary import dictionary

import math

def get_color_name(target_rgb):
    min_distance = float('inf')  # Begins with infinite to ensure that any distance will be lower
    closest_color_name = None
    
    # Iterates through colors and its variants
    for color_name, variants in dictionary.items():
        for variant in variants:
            distance = math.sqrt(
                (target_rgb[0] - variant[0])**2 +
                (target_rgb[1] - variant[1])**2 +
                (target_rgb[2] - variant[2])**2
            )
            # If this variant is closer to the current closest, update
            if distance < min_distance:
                min_distance = distance
                closest_color_name = color_name
    
    return closest_color_name


# print(get_color_name([152, 251, 152]))