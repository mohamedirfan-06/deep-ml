import numpy as np

def linear_regression_gradient_descent(X, y, alpha, iterations):
    m, n = X.shape

    # Initialize weights to zero
    theta = np.zeros(n)

    for _ in range(iterations):
        # Calculate predictions
        predictions = X @ theta

        # Calculate error
        error = predictions - y

        # Calculate gradient
        gradient = (1 / m) * (X.T @ error)

        # Update weights
        theta = theta - alpha * gradient

    return theta