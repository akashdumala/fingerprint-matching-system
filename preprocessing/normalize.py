import cv2

def normalize_image(image):
    """
    Normalize pixel values to improve contrast.
    """

    normalized = cv2.normalize(
        image,
        None,
        alpha=0,
        beta=255,
        norm_type=cv2.NORM_MINMAX
    )

    return normalized