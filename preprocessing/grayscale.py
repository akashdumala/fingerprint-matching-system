import cv2

def convert_to_grayscale(image):
    """
    Ensures the image is in grayscale.
    """

    if len(image.shape) == 2:
        return image

    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)