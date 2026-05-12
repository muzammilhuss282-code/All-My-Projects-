# ================================
# PROFESSIONAL ASCII ART GENERATOR
# ================================

# Install First:
# pip install pyfiglet termcolor

from pyfiglet import Figlet
from termcolor import colored
import os

# Clear Screen
os.system("cls" if os.name == "nt" else "clear")

print("=" * 50)
print("      PROFESSIONAL ASCII ART MAKER")
print("=" * 50)

# User Input
text = input("\nEnter Your Text: ")

# Available Fonts
fonts = [
    "slant",
    "banner3-D",
    "standard",
    "big",
    "doom",
    "digital",
    "isometric1"
]

print("\nAvailable Fonts:")
for i, f in enumerate(fonts, start=1):
    print(f"{i}. {f}")

choice = int(input("\nSelect Font Number: "))

selected_font = fonts[choice - 1]

# Create ASCII Art
ascii_art = Figlet(font=selected_font)

result = ascii_art.renderText(text)

# Colors
colors = ["red", "green", "yellow", "blue", "magenta", "cyan"]

print("\nAvailable Colors:")
for i, c in enumerate(colors, start=1):
    print(f"{i}. {c}")

color_choice = int(input("\nSelect Color Number: "))

selected_color = colors[color_choice - 1]

# Print Colored ASCII Art
print("\n")
print(colored(result, selected_color))

print("=" * 50)
print("        ASCII ART GENERATED")
print("=" * 50)