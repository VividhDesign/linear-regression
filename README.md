
Project Overview
This project implements a linear regression model from scratch to predict housing prices using a dataset of residential properties. The goal is to demonstrate a fundamental understanding of machine learning principles by manually performing key steps, including data preprocessing, feature engineering, and model training using the Normal Equation.

The project covers the complete data analysis workflow, from raw data to a working predictive model, without relying on high-level machine learning libraries like scikit-learn for the core algorithm.

Dataset
The dataset used for this project is housing_data.xlsx, which contains information on various residential properties. It includes features such as:

Area: The size of the property in square feet.

Bedrooms: The number of bedrooms.

Bathrooms: The number of bathrooms.

mainroad, guestroom, basement, hotwaterheating, airconditioning: Binary categorical features indicating the presence of these amenities.

furnishingstatus: A categorical feature with three unique values.

price: The target variable to be predicted.

Methodology
The project's workflow is broken down into the following key steps:

Data Preprocessing: Categorical features like mainroad and furnishingstatus are converted into numerical format using one-hot encoding.

Train-Test Split: A custom function is implemented to split the dataset into training and testing sets, ensuring a reproducible shuffle.

Model Implementation: The linear regression model is trained using the Normal Equation (

w=(X 
T
 X) 
−1
 X 
T
 y
), which directly calculates the optimal weights (coefficients) without an iterative process. This method provides a deep understanding of the model's underlying mathematics.

Prediction and Evaluation: The trained model makes predictions on the test set. The performance is evaluated using metrics such as Mean Squared Error (MSE) and Residual Sum of Squares (RSS).

Visualization: A scatter plot is generated to visually compare the actual prices against the model's predicted prices, providing a clear representation of its performance.

How to Run the Project
To run this project on your local machine, follow these steps:

Clone the repository:

Bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
Install dependencies: Make sure you have the required libraries installed. It's recommended to create a requirements.txt file and install them from there.

Bash

pip install pandas numpy matplotlib
Ensure the dataset is present: Place the housing_data.xlsx file in the same directory as the Python script.

Run the script:

Bash

python your_script_name.py
Results
The model's performance metrics and the calculated weights are printed to the console, and a plot is displayed. The results indicate the accuracy of the model and which features have the most influence on the predicted price.

Future Improvements
Adding an intercept term to the Normal Equation to create a more robust model.

Implementing other regression algorithms like Gradient Descent for a comparative analysis.

Adding more features or data points to improve the model's predictive accuracy.
