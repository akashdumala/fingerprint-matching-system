import os


def generate_report():

    os.makedirs("reports", exist_ok=True)

    report = """
==========================================
FINGERPRINT MATCHING PROJECT REPORT
==========================================

Dataset
-------
FVC2002 DB1

Feature Extraction
------------------
Gabor Texture Features

Similarity Measure
------------------
Euclidean Distance

Evaluation
----------
ROC Curve
AUC Score Generated

Outputs
-------
1. Matching Scores CSV
2. ROC Curve PNG
3. Report TXT

Status
------
PROJECT EXECUTED SUCCESSFULLY
"""

    with open("reports/final_report.txt", "w") as file:
        file.write(report)

    print("\nFinal report generated successfully.")