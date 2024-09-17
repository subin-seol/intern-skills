import os
import random
from PIL import Image, ImageDraw

# Helper function to draw a triangle
def draw_triangle(draw, bbox, color):
    x, y, w, h = bbox
    points = [(x + w // 2, y), (x, y + h), (x + w, y + h)]
    draw.polygon(points, fill=color)

# Helper function to draw a circle
def draw_circle(draw, bbox, color):
    x, y, w, h = bbox
    draw.ellipse([x, y, x + w, y + h], fill=color)

# Helper function to draw a diamond
def draw_diamond(draw, bbox, color):
    x, y, w, h = bbox
    points = [(x + w // 2, y), (x, y + h // 2), (x + w // 2, y + h), (x + w, y + h // 2)]
    draw.polygon(points, fill=color)

# Function to generate the classification dataset
def generate_classification_dataset(output_dir, num_images=100, img_size=(256, 256)):
    shapes = ['circle', 'triangle', 'diamond']
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create subdirectories for each class
    for shape in shapes:
        shape_dir = os.path.join(output_dir, shape)
        if not os.path.exists(shape_dir):
            os.makedirs(shape_dir)

    for i in range(num_images):
        # Randomly select a shape
        shape_type = random.choice(shapes)

        # Create a blank white image
        img = Image.new('L', img_size, color=255)
        draw = ImageDraw.Draw(img)

        # Randomize the size and position of the shape
        w = random.randint(30, img_size[0] // 2)
        h = random.randint(30, img_size[1] // 2)
        x = random.randint(0, img_size[0] - w)
        y = random.randint(0, img_size[1] - h)
        bbox = (x, y, w, h)

        # Draw the shape on the image
        if shape_type == 'circle':
            draw_circle(draw, bbox, color=0)
        elif shape_type == 'triangle':
            draw_triangle(draw, bbox, color=0)
        elif shape_type == 'diamond':
            draw_diamond(draw, bbox, color=0)

        # Save the image in the corresponding class folder
        image_filename = f"{shape_type}_{i+1}.png"
        image_path = os.path.join(output_dir, shape_type, image_filename)
        img.save(image_path)

    print(f"Dataset generated successfully! Images saved to '{output_dir}'.")

generate_classification_dataset("datasets/train", num_images=700)
generate_classification_dataset("datasets/test", num_images=300)

