"""
Basic machine learning pipeline for AI-based cyber threat detection.

This file will be used to train and evaluate a simple classification model
for detecting suspicious or malicious activity in cybersecurity-related data.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load cybersecurity dataset from a CSV file.
    """
    return pd.read_csv(file_path)


def prepare_data(df: pd.DataFrame, target_column: str):
    """
    Split the dataset into features and target labels.
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]

    return train_test_split(X, y, test_size=0.2, random_state=42)


def train_model(X_train, y_train):
    """
    Train a simple Random Forest classification model.
    """
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model.
    """
    predictions = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, predictions))
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))
