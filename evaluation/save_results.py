import csv
import os


def save_scores(genuine_scores, imposter_scores):

    os.makedirs("output", exist_ok=True)

    with open("output/matching_scores.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Type", "Score"])

        for score in genuine_scores:
            writer.writerow(["Genuine", score])

        for score in imposter_scores:
            writer.writerow(["Imposter", score])

    print("\nMatching scores saved.")