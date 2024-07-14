import matplotlib.pyplot as plt
import numpy as np

def draw_pythagorean_tree(ax, x, y, angle, size, level):
    if level == 0:
        return

    # Calculate the coordinates of the square
    x0 = x + size * np.cos(angle)
    y0 = y + size * np.sin(angle)
    x1 = x + size * np.cos(angle + np.pi / 2)
    y1 = y + size * np.sin(angle + np.pi / 2)
    x2 = x1 + size * np.cos(angle)
    y2 = y1 + size * np.sin(angle)

    # Draw the square
    ax.plot([x, x0], [y, y0], color='brown')
    ax.plot([x, x1], [y, y1], color='brown')
    ax.plot([x0, x2], [y0, y2], color='brown')
    ax.plot([x1, x2], [y1, y2], color='brown')

    # Calculate the new size and position for the next squares
    new_size = size * np.sqrt(2) / 2
    x_new = x2
    y_new = y2
    left_angle = angle + np.pi / 4
    right_angle = angle - np.pi / 4

    # Draw the left and right sub-trees
    draw_pythagorean_tree(ax, x1, y1, left_angle, new_size, level - 1)
    draw_pythagorean_tree(ax, x0, y0, right_angle, new_size, level - 1)

def main():
    # User input for recursion level
    recursion_level = int(input("Enter the recursion level: "))

    # Create a plot
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')

    # Initial size and position
    size = 1
    x = 0
    y = 0
    angle = np.pi / 2  # 90 degrees in radians

    # Draw the Pythagorean Tree
    draw_pythagorean_tree(ax, x, y, angle, size, recursion_level)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
