# Thyroid Disease Detection

![Thyroid Image](![1667462132](https://github.com/VijendraSRawat/Thyroid_Detection/assets/97980942/facda304-82ea-4a58-afc3-cd5ab9f4e23b))

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

## Running the Web Application

To run the web application, execute the [app.py](https://github.com/VijendraSRawat/Thyroid_Detection/blob/main/app.py) file and access the provided URL. The application will predict whether the user has thyroidal disease based on the input values.
