# Thyroid Disease Detection

![Thyroid Image](https://private-user-images.githubusercontent.com/97980942/291528108-facda304-82ea-4a58-afc3-cd5ab9f4e23b.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE3MDI5NzU4MzcsIm5iZiI6MTcwMjk3NTUzNywicGF0aCI6Ii85Nzk4MDk0Mi8yOTE1MjgxMDgtZmFjZGEzMDQtODJlYS00YTU4LWFmYzMtY2Q1YWI5ZjRlMjNiLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFJV05KWUFYNENTVkVINTNBJTJGMjAyMzEyMTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjMxMjE5VDA4NDUzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWY0MWJhYmQzMTVhOWQzZDU4ZGQ4NjdlYTA4Y2RlZTZiMmY2MDAyNDE2ODI4NDBiMmM0MTVlYjc5OTFmMGRiN2EmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.ThS7y7GKbODNEYxVvzIpVrA-3cu9UY0aMww5Qj4V6Uk)

*Image Source: maxlab.co.in*

## Introduction

This repository contains code for detecting thyroid disease using machine learning models. The project includes data preprocessing, feature selection, model building, and model selection.

## Code Files

The repository contains the following code files in the [Code](https://github.com/VijendraSRawat/Thyroid_Detection/tree/main/Code) folder:

- [Data_preprocessing.py](https://github.com/VijendraSRawat/Thyroid_Detection/blob/main/Code/data_preprocessing.py)
- [Feature_selection.py](https://github.com/VijendraSRawat/Thyroid_Detection/blob/main/Code/Feature_selection.py)
- [Model_building.py](https://github.com/VijendraSRawat/Thyroid_Detection/blob/main/Code/model_building.py)
- [Model_selection.py](https://github.com/VijendraSRawat/Thyroid_Detection/blob/main/Code/model_selection.py)

## Web Application

The repository also includes a web application for predicting thyroid disease. The web application is built using Flask and includes the following files:

- [App.py](https://github.com/VijendraSRawat/Thyroid_Detection/blob/main/app.py)
- [index.html](https://github.com/VijendraSRawat/Thyroid_Detection/blob/main/Templates/index.html) (in the [Templates](https://github.com/VijendraSRawat/Thyroid_Detection/tree/main/Templates) folder)

## Usage

To use the web application for predicting thyroid disease, follow these steps:

1. Ensure that you have Python and Flask installed.
2. Run the [app.py](https://github.com/VijendraSRawat/Thyroid_Detection/blob/main/app.py) file.
3. Access the web application through the provided URL.

## Predicting Thyroid Disease

The web application allows users to input FTI, TT4, TSH, and T4U values to predict whether they have thyroidal disease.

## Model Deployment

The machine learning models used for prediction are deployed using Flask. The models included are:

- Random Forest Model
- XGBoost Model

