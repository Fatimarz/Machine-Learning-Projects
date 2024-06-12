# House Price Prediction using Machine Learning
This project involves predicting house prices based on a dataset containing various features such as area, number of bedrooms, Longitude, Latitude etc. 

### Overview
The project was implemented using Jupyter Notebook to write Python code for data analysis, preprocessing, modeling, and evaluation.

### Project Structure
housing.ipynb: Jupyter Notebook containing the entire code pipeline for the house price prediction project.
housing.csv: CSV file containing the raw dataset for house price prediction.

# Workflow
### 1. Data Exploration and Preprocessing

- Imported the dataset into a Pandas DataFrame.
- Explored the dataset to understand its structure and characteristics.
- Checked for missing values and handled them by imputing with median for numerical features and mode for categorical features.
- Removed outliers using the Interquartile Range (IQR) method.
- Utilized mapping to standardize categories for the "house" feature (e.g., "housea", "houseb", "housec").
- Selected the top 10 categories for "estate agency" and "salesman" features to reduce dimensionality.
  
### 2. Feature Engineering

- Encoded categorical columns using label encoding to prepare the data for modeling.
  
### 3. Modeling

- Split the data into training and testing sets.
- Utilized three different regression algorithms:
- Decision Tree Regressor: Achieved an accuracy of 72.82% on the training set and 67.97% on the testing set.
- Gradient Boosting Regressor: Achieved an accuracy of 91.24% on the training set and 80.11% on the testing set, outperforming other algorithms.
- Random Forest Regressor: Achieved a training score of 83.22% and a testing score of 76.67%.
  
### 4. Conclusion

Based on the evaluation results, the Gradient Boosting Regressor performed the best among the three algorithms, with the highest accuracy on both the training and testing sets.

### 5. Usage

To replicate the project:

- Clone this repository to your local machine.
-  Install the necessary dependencies (e.g., pandas, scikit-learn).
- Open and run the Housing.ipynb notebook in a Jupyter environment.
   
### 6. Future Improvements

- Experiment with hyperparameter tuning to optimize the performance of the models.
- Explore other regression algorithms and ensemble techniques for potential performance enhancement
