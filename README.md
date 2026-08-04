# Fingerprint Matching System

## Project Overview

This project implements a fingerprint matching system using image processing and feature extraction techniques. It compares two fingerprint images by extracting Gabor texture features and measuring similarity using Euclidean Distance. The system also evaluates performance using ROC Curve analysis.

---

## Features

- Load fingerprint images
- Image preprocessing
- Grayscale conversion
- Image normalization
- Image enhancement
- Gabor feature extraction
- Euclidean distance matching
- Genuine vs Imposter comparison
- ROC Curve generation
- Matching score export (CSV)
- Automatic report generation

---

## Technologies Used

- Python 3.11
- OpenCV
- NumPy
- Matplotlib
- Scikit-Learn

---

## Dataset

FVC2002 DB1 Fingerprint Dataset

---

## Project Structure

```
Fingerprint-Matching
│
├── dataset
├── preprocessing
├── feature_extraction
├── matcher
├── evaluation
├── reports
├── output
├── tests
├── utils
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd Fingerprint-Matching
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## Output

The project generates:

- ROC Curve (PNG)
- Matching Scores (CSV)
- Final Report (TXT)

---

## Evaluation Metrics

- FAR (False Acceptance Rate)
- FRR (False Rejection Rate)
- TAR (True Acceptance Rate)
- ROC Curve
- AUC Score

---

## Future Improvements

- CNN-based feature extraction
- Deep Learning matcher
- Fingerprint alignment
- Minutiae extraction
- Streamlit Web Interface

---

## Author

Akash dumala
