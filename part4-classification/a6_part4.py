import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y)

model = linear_model.LogisticRegression().fit(x_train, y_train)

print("Accuracy:", model.score(x_test, y_test))
print("*************")
print("Testing Results:")
print("")
print(y_test)
for index in range(len(x_test)):
    x = x_test[index]
    x = x.reshape(-1, 3)
    print(x)
    y_pred = int(model.predict(x))

    if y_pred == 0:
        y_pred = "Male"
    elif y_pred == 1:
        y_pred = "Female"
    
    actual = y_test[index]
    if actual == 0:
        actual = "Male"
    elif actual == 1:
        actual = "Female"
    print("Predicted Gender: " + y_pred + " Actual Gender: " + actual)
    print("")
# Step 1: Print the values for x and y

# Step 2: Standardize the data using StandardScaler, 

# Step 3: Transform the data

# Step 4: Split the data into training and testing data

# Step 5: Fit the data

# Step 6: Create a LogsiticRegression object and fit the data

# Step 7: Print the score to see the accuracy of the model

# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data