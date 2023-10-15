<h1 align="center">ColorCompass</h1>

<p align="center">
  <img src="logo.png" alt="Color Compass Logo" width="200" height="200"/>
</p>

---

### Overview

ColorCompass is a Python library designed to efficiently find the closest named color to a given RGB value by using an efficient Euclidean distance calculation across a range of predefined colors.

### How it Works

#### The Euclidean Distance Calculation

The crux of ColorCompass lies in utilizing the Euclidean Distance formula to find the closest matching color name for a given RGB input. Given an RGB value, the Euclidean Distance between two points (color values, in our context) in a three-dimensional space (R, G, B) is calculated as:

Distance = √(R_2 - R_1)^2 + (G_2 - G_1)^2 + (B_2 - B_1)^2

Here,
- (R_1, G_1, B_1) and (R_2, G_2, B_2) are the RGB values of the two colors being compared.
- The formula basically measures the straight-line distance between two points in a 3D space (your two colors, in the RGB color space).

#### The Algorithmic Approach

1. **Input Color Value**: A user inputs an RGB color value that they'd like to map to a named color.
   
2. **Distance Calculation**: For the input color, ColorCompass calculates the Euclidean Distance between the input RGB value and all stored RGB values in the library's color database, effectively identifying which stored color is closest (has the minimal Euclidean Distance) to the provided input.
   
3. **Return Closest Color**: The algorithm identifies the color name associated with the RGB value in the database that has the smallest Euclidean Distance to the input color. This color name is returned to the user as the closest match.

## 🚀 Installation

You can install ColorCompass using pip:

```sh
pip install color-compass
```

## 🎨 Basic Usage

To find the closest color name for a given RGB value, simply use the `find_closest_color` function as follows:

```python
from colorcompass import find_closest_color

# Define your target color as an RGB list
target_color = [152, 251, 152]

# Use the function to find the closest color name
closest_color_name = find_closest_color(target_color)

# Print the found color name
print(closest_color_name)
```

### Full Example

```python
from colorcompass import find_closest_color

def main():
    # Define some target colors
    target_colors = [
        [152, 251, 152],
        [70, 130, 180],
        [255, 0, 0]
    ]
    
    # Find and print the closest color name for each target color
    for color in target_colors:
        print(f"Closest color to RGB{tuple(color)} is {find_closest_color(color)}")

if __name__ == "__main__":
    main()
```

## 📄 License

ColorCompass is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for more details.

## 🙌 Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) file for details on our code of conduct and the process for submitting pull requests.

## 📞 Contact

If you have questions or issues, please [open an issue](https://github.com/NicolasAguirreCampi/ColorCompass/issues/new).