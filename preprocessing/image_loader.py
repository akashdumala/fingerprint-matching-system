import cv2
import os


def load_image(image_path):
    """
    Loads a fingerprint image from disk.

    Parameters:
        image_path (str): Path to the fingerprint image.

    Returns:
        image: Loaded grayscale image.
    """

    # Check whether the file exists
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Read the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Verify the image loaded correctly
    if image is None:
        raise ValueError(f"Unable to load image: {image_path}")

    return image