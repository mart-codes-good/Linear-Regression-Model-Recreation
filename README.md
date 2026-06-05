# Linear-Regression-Model-Recreation
A quick recreation of the linear regression model to improve my understanding of the concept.

## Tech Stack
```
Python
numpy
sklearn (to compare with re-created model)
```
## How it works
At its core, a Linear Regression Model is a custom line of best fit, determined from the slope and intercept of your data. Think of y = mx + b (my favourite function from high school math). In our case, this translates to f(x) = β1x + β0, where β1 is the slope and β0 is the intercept. This is the notation that is properly used when using this model.

To keep things simple, I'll explain this using only two dimensions: an X axis and Y axis (2d plane).

Let's say our X values are 1 through 5, and our Y values are their multiples of 2, so 2, 4, 6, 8, 10. That's is our dataset. Using this we will calculate two things:

    Slope (β1): using m = (y2 - y1) / (x2 - x1)
    Intercept (β0): using b = y - mx

Computing these values using our data, it gives us y = 2x + 0 (or f(x) = 2x), where our slope is 2 and the intercept is 0. At this point, our model is now "trained".

Now we can make predictions. Let's replace x with 6, so that our model returns 12, which accuretely predicts the following y value (since our y plane is the multiples of 2). In reality, Linear Regression works with two or more independent variables, so instead of fitting a line through a 2D plane it fits a hyperplane through multiple dimensions, but the concpet is the same

For a more in depth description visit the kraggle notebook [here](). (Will be updated once the notebook is completed)

## Notes
Please feel free to use this code for your own use or study in accordance with the liscence.
