import numpy as np


def euclidean_distance(feature1, feature2):
    """
    Compute Euclidean distance between two feature vectors.
    """
    return np.linalg.norm(feature1 - feature2)


def similarity_score(distance):
    """
    Convert distance to similarity score (0-1).
    Higher score means more similar.
    """
    return 1 / (1 + distance)