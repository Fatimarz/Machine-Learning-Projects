## Table of contents
* [Overview](#Overview)
* [Objectives](Objectives)
* [Features](Features)
* [Steps](Steps)
* [Tools and Technologies](ToolsandTechnologies)
* [Results](Results)

## Overview
This project aims to predict whether an investment will fail or not based on various investor and investment-related features.

## Objective
The main objective is analyze the features and determine the likelihood of investment failure and success, helping investors make informed decisions.

## Features
* Investor_ID: Unique identifier for each investor.
* Age: Age of the investor.
* Annual_Income: Annual income of the investor.
* Investment_Amount: The amount invested.
* Risk_Tolerance_Score: A score representing the investor's risk tolerance.
* Months_of_Investing_Experience: Number of months the investor has been investing.
* Number_of_Active_Investments: The number of active investments the investor has.
* Potential_Return_Rate: The potential return rate of the investment.
* Investment_Duration: The duration of the investment in months.
* Investment_to_Income_Ratio: The ratio of investment amount to the investor's annual income.
* Education: The educational background of the investor.
* Employment_Status: The employment status of the investor.
* Marital_Status: The marital status of the investor.
* Owns_Property: Whether the investor owns property.
* Has_Dependents: Whether the investor has dependents.
* Investment_Sector: The sector in which the investment is made.
* Has_Investment_Advisor: Whether the investor has an investment advisor.
* Investment_Failed: The target variable indicating whether the investment failed (0) or succeeded (1).

# Steps
### Data Cleaning:
* Checked for null values and imputed them with the mean.
* Identified and removed outliers in the 'Age' column using IQR due to right skewness in distribution.
  
### Handling Imbalancd data:
* Balanced the target column using SMOTE to address class imbalance.
  
### Data Splitting:
* Split the data into training and testing sets.

### Model Training:
* Used the Random Forest algorithm for prediction.

### Model Evaluation:
* Achieved an accuracy of approximately 99.999% on training data.
* Achieved an accuracy of approximately 89.29% on testing data.

### Tools and Technologies
* Python: The primary programming language used for the project.
* Pandas: For data manipulation and analysis.
* NumPy: For numerical computations.
* Scikit-learn: For building and evaluating machine learning models.
* Matplotlib/Seaborn: For data visualization.
* Jupyter Notebook: For interactive development and analysis.

# Results
### Model Performance: 
The Random Forest model performed exceptionally well on training data with very high accuracy, while also showing strong performance on testing data.

