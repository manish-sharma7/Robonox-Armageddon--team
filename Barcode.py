
import cv2
import numpy as np
import matplotlib.pyplot as plt

from pyzbar.pyzbar import decode


def barcode(imgPath):
    """

    Arguments: path of image
    Returns: string corresponding to the barcode

    """

    image = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE) # Enter the file Path to make the output
    ones = np.full(image.shape, 25, np.uint8)

    image = cv2.subtract(image, ones) # decreasing the brightness to make the black color more prominent

    kernel = np.array([
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ])

    sharpen = cv2.filter2D(image, -1, kernel) # If image is too blur use this else not


    detect = decode(image) # can detect multiple bar codes
    return detect[0].data # This i.data prints the value of the bar code



