from matcher.matcher_engine import match_images
from evaluation.roc_curve import plot_roc
from evaluation.save_results import save_scores
from reports.generate_report import generate_report

from evaluation.pair_generator import (
    get_image_paths,
    generate_genuine_pairs,
    generate_imposter_pairs,
)

from evaluation.metrics import calculate_statistics


def main():

    folder = "dataset/raw/FVC2002_DB1/fingerprints/DB1_B"

    images = get_image_paths(folder)

    genuine_pairs = generate_genuine_pairs(images)

    imposter_pairs = generate_imposter_pairs(images)

    genuine_scores = []

    imposter_scores = []

    print("Matching Genuine Pairs...")

    for img1, img2 in genuine_pairs:

        score = match_images(img1, img2)

        genuine_scores.append(score)

    print("Matching Imposter Pairs...")

    for img1, img2 in imposter_pairs:

        score = match_images(img1, img2)

        imposter_scores.append(score)

    calculate_statistics(
        genuine_scores,
        imposter_scores,
    )
    plot_roc(
    genuine_scores,
    imposter_scores,
)
    save_scores(
    genuine_scores,
    imposter_scores
)
    generate_report()


if __name__ == "__main__":
    main()