# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data? The r squared coefficient is 0.86 for my model, and that indicates that the variables have a strong positive correlation.

2. Is your model accurate? Why or why not? My model is not accurate because of the large gaps between the actual value and the predicted value. This could be because the model does not account for other factors beyond mileage and age that affect the cost of a car.

3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles? The model predicts that a 10-year-old car with 89000 miles is worth $9,054.91 (x1 -> mileage, x2 -> age). A car that is 20 years old wih 150000 miles is predicted to be worth $1,359.21. (x1 -> mileage, x2 -> age)

4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening? I think this is happening because both age and mileage drive down the value of a car the higher they get. Because there is not a minimum value set, very high mileage and very high age bring the car down to negative values.