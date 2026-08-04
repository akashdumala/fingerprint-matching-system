import numpy as np


def compare_texture(feature1, feature2):
    """
    Compare two feature vectors using Euclidean distance.
    """

    distance = np.linalg.norm(feature1 - feature2)

    return distance