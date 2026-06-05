import numpy as np

# Sample data
# Quick sample variables
# independant variable (x-axis)
X = np.array([1, 2, 3, 4, 5])

# dependant variable (y-axis) what we are trying to predict
Y = np.array([2, 4, 5, 7, 10])

# Calculate means 
x_mean = np.mean(X)
y_mean = np.mean(Y)

# Calculate slope and intercept (b1 and b0)
# slop: beta_1 = sum((x - x_mean) * (y - y_mean)) / sum((x - x_mean)^2)
# intercept: beta_0 = y_mean - (Beta_1 * x_mean)

numerator = np.sum((X - x_mean) * (Y- y_mean))
denominator = np.sum((X - x_mean) ** 2)

beta_1 = numerator / denominator
beta_0 = y_mean - (beta_1 * x_mean)

print(f"Slope: {beta_1:.2f}")
print(f"intercept: {beta_0:.2f}")

print(f"Current Model: y = {beta_1:.2f}x + {beta_0:.2f}")

# Use current model to make predictions
y_pred = beta_0 + beta_1 * X

print(f"Actual y values: {Y}")
print(f"Predicted values: {y_pred}")

# Evaluate the model R^2
# R^2 = 1 - (Residual Sum of Squares / Total Sum of Squares)
rss = np.sum((Y - y_pred) ** 2)
tss = np.sum((Y - y_mean) ** 2)

r2_score = 1 - (rss / tss)
print(f"R^2 Score: {r2_score}")

# Since model is complete lets see what the
# predicted values would be for new random x values!
new_X = 6
new_pred = beta_0 + beta_1 * new_X

print(f"Prediction for new_X (6) is {new_pred:.2f}")