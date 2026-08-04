import os
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc


def plot_roc(genuine_scores, imposter_scores):

    os.makedirs("output", exist_ok=True)

    labels = [1] * len(genuine_scores) + [0] * len(imposter_scores)
    scores = genuine_scores + imposter_scores

    fpr, tpr, thresholds = roc_curve(labels, scores)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, linewidth=2, label=f"AUC = {roc_auc:.4f}")
    plt.plot([0, 1], [0, 1], linestyle="--")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.grid(True)
    plt.legend()

    plt.savefig("output/roc_curve.png")

    print("\nROC Curve saved successfully.")
    print("AUC =", round(roc_auc, 4))

    plt.show()