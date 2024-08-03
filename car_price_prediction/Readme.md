# Table of contents
* [Demo](Demo)
* [Overview](Overview)
* [Motivation](Motivation)
* [Datast](Dataset)
* [Exploratory Data Analysis](ExploratoryDataAnalysis)
* [Model Selection](ModelSelection)
* [Deployment](Deployment)
## Demo
<img src="https://github.com/user-attachments/assets/be88382e-d2a2-4454-a4d5-9191bb763d7e" width="500" />

## Overview
This project demonstrates the end-to-end process of building predictive machine learning model and deploying it locally using flask. 

## Motivation
Accurate car price predictions are crucial for buyers, sellers, and automotive businesses to make informed decisions. Traditional methods of price estimation can be subjective and inconsistent. This project aims to leverage machine learning to provide a data-driven approach for predicting car prices based on various features

## Dataset
https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

## Exploratory Data Analysis

In this project, extensive Exploratory Data Analysis (EDA) is performed to understand the dataset and prepare it for modeling. The following steps were undertaken:

### Checked for Null Values:
Null values are checked in the dataset to ensure data integrity and improve the model's performance.

### Examined Unique Categories in Categorical Features:
Reviewed the unique categories for each categorical feature to understand the diversity and distribution of categorical data.

### Statistical Summary:
A statistical summary of numerical features was generated to understand their distributions, ranges, and basic statistics measures. 

### Dropped Unnecessary Features:
The 'Car_Name' feature was removed from the dataset as it was deemed non-essential for predicting car prices.

### Derived New Feature:
A new feature was created by subtracting the car's manufacturing year from the current year.

### Converted Categorical Features to Numerical:
Categorical features were converted into numerical format using techniques such as one-hot encoding to facilitate their use in machine learning algorithms.

### Analyzed Correlation:
We evaluated the correlation between features and the target variable (Selling_Price) to identify key relationships and understand how each feature influences the car price.

### Top 6 Important Features:
Identified and examined the top 6 features with the most significant impact on car prices. 
<img src="https://github.com/user-attachments/assets/4a08fc7c-23e8-4feb-a82e-d3a6f7a3c724" width="500" />

### ModelSelection
In this project, we evaluated two machine learning models for predicting car prices: Linear Regression and Random Forest. The performance of these models was assessed based on training and testing scores.

* Linear Regression:
Training Score: 0.88
Testing Score: 0.88
Linear Regression provided a good balance between training and testing scores, indicating that the model generalizes well to new data.

* Random Forest:
Training Score: 0.98
Testing Score: 0.97
The Random Forest model achieved higher scores compared to Linear Regression, with a significant improvement in both training and testing scores. This suggests that Random Forest captures complex patterns in the data more effectively.

### Deployment
The trained Random Forest model is integrated into the Flask application locally. The model predicts car prices based on user inputs.Tested the web application to ensure that it accurately predicts car prices and provides a user-friendly experience.

### Setup 
To try out this car price prediction project, follow these steps:

* Clone the Repository:
Clone the repository to your local machine
Navigate to the project directory

* Create a Virtual Environment (optional but recommended):
Activate a virtual environment

* Install Dependencies:
Install the required libraries using
pip install -r requirements.txt

*Train the Model:
Follow the steps mentioned in car_price_prediction.ipynb to train the model from scratch.

*Run the Flask Application:
Start the Flask server by running: python app.py
The application will be accessible at http://localhost:5000 in your web browser.

* Interact with the Web Interface:
Open a web browser and navigate to http://localhost:5000.
Enter car details into the form and click “Predict” to get price predictions.

* View and Test the Predictions:
 Review the predicted car prices provided by the web interface based on the input data.



