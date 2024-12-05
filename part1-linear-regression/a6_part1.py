import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("part1-linear-regression/blood_pressure_data.csv")
x = data["Age"].values
y = data["Blood Pressure"].values

# Use reshape to turn the x values into 2D arrays:
x = x.reshape(-1,1)

# Create the model
model = LinearRegression().fit(x, y)

# Find the coefficient, bias, and r squared values. 
# Each should be a float and rounded to two decimal places. 

coef = round(float(model.coef_[0]), 2)
intercept = round(float(model.intercept_), 2)
r_squared = model.score(x, y)

x_predict = 43
prediction = model.predict([[x.predict]])
# Print out the linear equation and r squared value
print(f"Model's Linear Equation: y = {coef}x + {intercept}")
print(f"R Squared Value: {r_squared}")
print(f"Prediction when x is {x_predict}: {prediction}")

plt.figure(figsize=(7, 5))
plt.scatter(x, y, c="purple")
plt.scatter(x_predict, prediction, c="pink")

plt.xlabel("Age")
plt.ylabel("Blood Pressure")
plt.title("Blood Pressure by Age")

plt.plot(x, coef*x + intercept, c="r", label="Line of Best Fit")

plt.legend()
plt.show()
# Predict the the blood pressure of someone who is 43 years old.
# Print out the prediction


# Create the model in matplotlib and include the line of best fit