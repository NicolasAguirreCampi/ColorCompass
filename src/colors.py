from color_dictionary import dictionary

import math

def find_closest_color(target_rgb, color_data):
    min_distance = float('inf')  # Inicializa con infinito para asegurar que cualquier distancia será menor
    closest_color_name = None
    
    # Itera a través de los colores y sus variantes
    for color_name, variants in color_data.items():
        for variant in variants:
            distance = math.sqrt(
                (target_rgb[0] - variant[0])**2 +
                (target_rgb[1] - variant[1])**2 +
                (target_rgb[2] - variant[2])**2
            )
            # Si esta variante es más cercana que la más cercana hasta ahora, actualiza
            if distance < min_distance:
                min_distance = distance
                closest_color_name = color_name
    
    return closest_color_name


print(find_closest_color([98, 156, 90], dictionary))