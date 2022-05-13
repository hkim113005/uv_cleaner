import os

import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_images(img_dir, resize=None, color_convert=None):
    images = []
    labels = []
    classes = []
    for label in os.listdir(img_dir):
        if not os.path.isdir(os.path.join(img_dir, label)):
            continue
            
        classes.append(label)
        
        for img in os.listdir(os.path.join(img_dir, label)):
            if not img.endswith(".png"):
                continue
                
            f = os.path.join(img_dir, label, img)

            if resize:
                image = np.asarray(cv2.resize(cv2.imread(f), resize))
            if color_convert:
                image = cv2.cvtColor(image, color_convert)

            images.append(image)
            labels.append(label)

    return (images, labels, classes)


def plot_image_histogram(img):
    plt.figure()
    plt.imshow(img)
    plt.colorbar()
    plt.grid(False)
    plt.show()


def plot_images_grid(images, labels, classes, rows=5, cols=5):
    plt.figure(figsize=(10, 10))
    for i in range(rows * cols):
        plt.subplot(rows, cols, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        # noinspection PyUnresolvedReferences
        plt.imshow(images[i], cmap=plt.cm.binary)
        plt.xlabel(classes[labels[i]])

    plt.show()
