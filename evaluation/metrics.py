import pandas as pd


def calculate_statistics(genuine_scores, imposter_scores):

    print()

    print("=" * 50)

    print("Evaluation")

    print("=" * 50)

    print("Genuine Comparisons :", len(genuine_scores))

    print("Imposter Comparisons :", len(imposter_scores))

    print()

    print("Average Genuine Score :",
          round(sum(genuine_scores) / len(genuine_scores), 4))

    print("Average Imposter Score :",
          round(sum(imposter_scores) / len(imposter_scores), 4))

    threshold = 0.03

    FAR = sum(score >= threshold for score in imposter_scores) / len(imposter_scores)

    FRR = sum(score < threshold for score in genuine_scores) / len(genuine_scores)

    TAR = 1 - FRR

    print()

    print("Threshold :", threshold)

    print("FAR :", round(FAR, 4))

    print("FRR :", round(FRR, 4))

    print("TAR :", round(TAR, 4))

    df = pd.DataFrame({
        "Genuine": genuine_scores + [None] * len(imposter_scores),
        "Imposter": [None] * len(genuine_scores) + imposter_scores
    })

    df.to_csv("output/matching_scores.csv", index=False)