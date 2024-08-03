import cv2
import numpy as np
import os
from math import sqrt, ceil, floor

def create_collage(image_paths, hidden_paths):
    images = []
    for path in image_paths:
        image = cv2.imread(path)
        images.append(image)

    hidden_image = cv2.imread(hidden_paths[0])  # Assuming all hidden images are the same
    num_images = len(images)
    num_cols = floor(sqrt(num_images))  # Количество картинок по горизонтали
    num_rows = ceil(num_images / num_cols)  # Количество картинок по вертикали
    
    # Создание пустого коллажа
    collage = np.zeros((num_rows * hidden_image.shape[0], num_cols * hidden_image.shape[1], 3), dtype=np.uint8)
    
    # Размещение изображений на коллаже
    for i in range(num_images):
        row = i // num_cols
        col = i % num_cols
        if i < len(image_paths):
            collage[row * images[0].shape[0]:(row + 1) * images[0].shape[0], col * images[0].shape[1]:(col + 1) * images[0].shape[1], :] = images[i]
        else:
            collage[row * hidden_image.shape[0]:(row + 1) * hidden_image.shape[0], col * hidden_image.shape[1]:(col + 1) * hidden_image.shape[1], :] = hidden_image
    
    return collage
