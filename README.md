# AI Cyber Threat Detection

AI-based cybersecurity project for detecting suspicious activity in network or log data using machine learning.

## Overview

This project explores how artificial intelligence can support cybersecurity teams by identifying unusual or potentially malicious activity in log or network traffic data.

The goal is to build a simple machine learning pipeline that can process cybersecurity-related data, detect suspicious patterns, and present the results in a clear way for security analysts.

## Why This Project

Cybersecurity teams often deal with a large number of alerts, logs, and events. AI can help by filtering large amounts of data, detecting anomalies, and highlighting activity that may require human investigation.

This project is focused on:

- AI-driven threat detection
- Anomaly detection
- SOC automation
- Cyber resilience
- Machine learning for cybersecurity

## Planned Features

- Load and clean cybersecurity-related data
- Perform basic data analysis
- Train a machine learning model
- Detect suspicious or abnormal activity
- Generate simple alert outputs
- Create a short report or dashboard showing the results

## Current Progress

The project currently includes:

- Initial data exploration using a public network intrusion dataset
- Binary classification setup:
  - `0` = normal network activity
  - `1` = suspicious or malicious activity
- Machine learning model training using Random Forest
- Model evaluation using accuracy, classification report, and confusion matrix

## Notebooks

- `01_data_exploration.ipynb`  
  Explores the cybersecurity dataset and prepares the binary target label.

- `02_model_training.ipynb`  
  Trains a machine learning model to classify network activity as normal or suspicious.

## Initial Result

Accuracy: 0.9994

The first Random Forest model achieved strong classification performance on the test dataset.

This result shows that machine learning can be used to identify patterns associated with suspicious network activity in a controlled dataset.

Further improvements will focus on explainability, anomaly detection, and SOC-style alert summaries.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

## Project Status

In progress.

## Author

Levente Czako  
3rd-year Artificial Intelligence student at Heriot-Watt University Dubai  
Interested in AI-driven cybersecurity, threat detection, SOC automation, and OT cyber resilience.
