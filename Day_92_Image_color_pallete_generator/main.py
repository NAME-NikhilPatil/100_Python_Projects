import numpy as np
from sklearn.cluster import KMeans
from PIL import Image
import matplotlib.pyplot as plt


def generate_color_palette(image_path, num_colors=5):
    # Open the image and convert it to RGB mode
    image = Image.open(image_path)
    image = image.convert('RGB')
    image = image.resize((image.width // 2, image.height // 2))  # Resize for faster processing

    # Convert the image into a NumPy array
    image_array = np.array(image)
    image_array = image_array.reshape((-1, 3))  # Reshape to a list of RGB colors

    # Use KMeans clustering to find the most common colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(image_array)

    # Get the colors from the cluster centers
    colors = kmeans.cluster_centers_.astype(int)

    # Plot the color palette
    plt.figure(figsize=(8, 2))
    plt.title(f'Top {num_colors} Colors in Image')
    plt.imshow([colors], aspect='auto')
    plt.axis('off')
    plt.show()

    # Return the RGB values of the colors
    return colors


# Usage example
image_path = 'img.png'  # Replace with the path to your image
palette = generate_color_palette(image_path, num_colors=5)

print("Top colors (RGB):")
for idx, color in enumerate(palette):
    print(f"Color {idx + 1}: {color}")
