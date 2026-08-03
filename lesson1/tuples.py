red_color = (23, 21, 56)
print(f"R: {red_color[0]}")
print(f"G: {red_color[1]}")
print(f"B: {red_color[2]}")

# Tuples do not support assignment operations (they are immutable)
# red_color[0] = 34  # This would raise a TypeError

r, g, b = red_color
print(f"Unpacked R value: {r}")