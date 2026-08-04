import cv2
import numpy as np


def extract_gabor_features(image):
    """
    Extract Gabor filter responses from a fingerprint image.
    """

    kernels = []

    for theta in np.arange(0, np.pi, np.pi / 8):
        kernel = cv2.getGaborKernel(
            (21, 21),
            sigma=5,
            theta=theta,
            lambd=10,
            gamma=0.5,
            psi=0,
            ktype=cv2.CV_32F
        )
        kernels.append(kernel)

    responses = []

    for kernel in kernels:
        filtered = cv2.filter2D(image, cv2.CV_8UC3, kernel)
        responses.append(filtered)

    feature_vector = []

    for response in responses:
        feature_vector.append(np.mean(response))
        feature_vector.append(np.std(response))

    return np.array(feature_vector)