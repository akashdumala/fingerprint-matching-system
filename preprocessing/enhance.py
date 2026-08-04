import cv2

def enhance_image(image):
    """
    Enhance fingerprint using CLAHE.
    """

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(image)

    return enhanced