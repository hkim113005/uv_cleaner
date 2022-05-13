import json
import os

import numpy as np
import matplotlib.pyplot as plt


def plot_image_and_predictions(i, predictions, classes, true_label, img):
    predictions, true_label, img = predictions[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    # noinspection PyUnresolvedReferences
    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = int(np.argmax(predictions))
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(classes[predicted_label],
                                         100 * np.max(predictions),
                                         classes[int(true_label)]), color=color)


def plot_value_array(i, predictions, true_label):
    predictions, true_label = predictions[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(len(predictions)), predictions, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')


# Plot the first X test images, their predicted label, and the true label
# Color correct predictions in blue, incorrect predictions in red
def plot_results(images, labels, predictions, classes, rows, cols):
    n_images = rows * cols
    plt.figure(figsize=(2 * 2 * cols, 2 * rows))

    for i in range(n_images):
        plt.subplot(rows, 2 * cols, 2 * i + 1)
        plot_image_and_predictions(i, predictions, classes, labels, images)
        plt.subplot(rows, 2 * cols, 2 * i + 2)
        plot_value_array(i, predictions, labels)

    plt.show()


def get_predicted_label(image, classes, model):
    predictions = model.predict(np.asarray([image]))
    predicted_label = np.argmax(predictions)
    return classes[predicted_label]


def predict(model, img, properties_file=None, resize=None, classes=None, color_convert=None):
    import cv2

    if isinstance(img, str):
        img = cv2.imread(img)

    if properties_file:
        with open(properties_file) as f:
            properties = json.load(f)

        resize = properties.get('input_size', resize)
        classes = properties.get('classes', classes)
        color_convert = properties.get('color_convert', color_convert)

    if color_convert:
        if isinstance(color_convert, str):
            color_convert = getattr(cv2, color_convert)

        img = cv2.cvtColor(img, color_convert)

    if resize:
        img = cv2.dnn.blobFromImage(img, size=tuple(resize), mean=0.5)
    else:
        img = cv2.dnn.blobFromImage(img, mean=0.5)

    model.setInput(img)
    output = model.forward()
    prediction = int(np.argmax(output))

    if classes:
        prediction = classes[prediction]

    return prediction
