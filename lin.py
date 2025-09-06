import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
# You will need to change this path to where your file is located.
# For example: data = pd.read_excel("housing_data.xlsx")
data = pd.read_excel(r"D:\supervised\linear regression\housing_data.xlsx")

## one hot encoding
data['mainroad'] = data['mainroad'].replace({'yes': 1, 'no': 0})
data['guestroom'] = data['guestroom'].replace({'yes': 1, 'no': 0})
data['basement'] = data['basement'].replace({'yes': 1, 'no': 0})
data['hotwaterheating'] = data['hotwaterheating'].replace({'yes': 1, 'no': 0})
data['airconditioning'] = data['airconditioning'].replace({'yes': 1, 'no': 0})

furnishing_status = data['furnishingstatus'].unique()
for status in furnishing_status:
    data[status] = data['furnishingstatus'].apply(lambda x: 1 if x == status else 0)

data.drop(columns=['furnishingstatus'], inplace=True)

# Separate features (X) and target (y)
y = data['price']
X = data.drop(columns=['price'])

# Custom train-test split function
def train_test_split(X, y, test_size=0.2):
    np.random.seed(42)
    n = len(X)
    test_count = int(n * test_size)
    indices = np.arange(n)
    np.random.shuffle(indices)
    
    # getting the random indices
    test_idx = indices[:test_count]
    train_idx = indices[test_count:]
    
    # getting the test_data and train_data
    X_test, X_train = X.iloc[test_idx], X.iloc[train_idx]
    y_test, y_train = y.iloc[test_idx], y.iloc[train_idx]
    
    return X_test, X_train, y_test, y_train

# Split the data
X_test, X_train, y_test, y_train = train_test_split(X, y, 0.2)

# Normal Equation WITHOUT intercept
XtX = X_train.T @ X_train
XtX_inv = np.linalg.inv(XtX)
XtY = X_train.T @ y_train
weights = XtX_inv @ XtY  # slope only, no intercept

# Predictions
y_pred = X_test @ weights

# Results
print("Weights (slope only, intercept=0):", weights)
print("Mean Squared Error:", np.mean((y_test - y_pred)**2))
print("Residual Sum of Squares:", np.sum((y_test - y_pred)**2))

# Plot
plt.figure(figsize=(10, 6))
X_area = X_test['area']
plt.scatter(X_area, y_test, color="black", label="Actual")
plt.scatter(X_area, y_pred, color="red", label="Predicted")
plt.xlabel("Area (sq ft)")
plt.ylabel("Price")
plt.title("Price Prediction using Linear Regression (No Intercept)")
plt.legend()
plt.show()