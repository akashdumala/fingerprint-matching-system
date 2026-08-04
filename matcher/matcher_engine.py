import os

from preprocessing.image_loader import load_image
from preprocessing.grayscale import convert_to_grayscale
from preprocessing.normalize import normalize_image
from preprocessing.enhance import enhance_image

from feature_extraction.gabor_features import extract_gabor_features

from matcher.euclidean_matcher import (
    euclidean_distance,
    similarity_score,
)


def preprocess(path):

    image = load_image(path)
    image = convert_to_grayscale(image)
    image = normalize_image(image)
    image = enhance_image(image)

    return image


def match_images(image1_path, image2_path):

    image1 = preprocess(image1_path)
    image2 = preprocess(image2_path)

    feature1 = extract_gabor_features(image1)
    feature2 = extract_gabor_features(image2)

    distance = euclidean_distance(feature1, feature2)

    score = similarity_score(distance)

    return score