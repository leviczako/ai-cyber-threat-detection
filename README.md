# AI Cyber Threat Detection

AI-based cybersecurity project for detecting suspicious activity in network or log data using machine learning.

## Overview

This project explores how artificial intelligence can support cybersecurity teams by identifying unusual or potentially malicious activity in network traffic data.

The goal is to build a simple machine learning pipeline that can process cybersecurity-related data, detect suspicious patterns, and present the results in a clear way for security analysts.

## Why This Project

Cybersecurity teams often deal with a large number of alerts, logs, and network events. AI can help by filtering large amounts of data, detecting anomalies, and highlighting activity that may require human investigation.

This project is focused on:

- AI-driven threat detection
- Network intrusion detection
- Suspicious activity classification
- SOC automation
- Cyber resilience
- Machine learning for cybersecurity

## Project Workflow

The project follows a simple AI-based cybersecurity workflow:

1. Load a public network intrusion detection dataset
2. Explore and understand the data
3. Convert attack labels into a binary classification problem
4. Train a machine learning model
5. Evaluate model performance
6. Convert model predictions into SOC-style alert summaries

## Current Progress

The project currently includes:

- Initial data exploration using a public network intrusion dataset
- Binary classification setup:
  - `0` = normal network activity
  - `1` = suspicious or malicious activity
- Machine learning model training using Random Forest
- Model evaluation using accuracy, classification report, and confusion matrix
- SOC-style alert summary generation from model predictions

## Notebooks

### 01_data_exploration.ipynb

Explores the cybersecurity dataset and prepares the binary target label.

### 02_model_training.ipynb

Trains a Random Forest machine learning model to classify network activity as normal or suspicious.

### 03_alert_summary.ipynb

Converts model predictions into simple human-readable SOC-style alert summaries.

Example alert:

```text
Alert: Suspicious network activity detected.
Severity: High
Model confidence: 1.00
Recommended action: Immediate investigation recommended.
```

## Initial Result

The first Random Forest model achieved the following result on the test dataset:

```text
Accuracy: 0.9994
```

This result shows that machine learning can identify patterns associated with suspicious network activity in a controlled public dataset.

This is an early portfolio project and not a production-ready cybersecurity system. Future work will focus on explainability, anomaly detection, attack type classification, and more realistic SOC-style workflows.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook / Google Colab

## Future Improvements

Planned improvements include:

- Model explainability
- Feature importance analysis
- Attack type classification
- Better risk scoring
- LLM-based alert summarization
- Dashboard integration
- Industrial / OT cybersecurity use cases

## Project Status

In progress.

## Author

Levente Czako  
3rd-year Artificial Intelligence student at Heriot-Watt University Dubai  
Interested in AI-driven cybersecurity, threat detection, SOC automation, and OT cyber resilience.
