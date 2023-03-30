import numpy as np

def cost_function( x, y, theta0, theta1 ):
    """Compute the squared error cost function

    Inputs:
    x        vector of length m containing x values
    y        vector of length m containing y values
    theta_0  (scalar) intercept parameter
    theta_1  (scalar) slope parameter

    Returns:
    cost     (scalar) the cost
    """

    cost = 0.0

    ##################################################
    # TODO: write code here to compute cost correctly
    ##################################################
    h = theta0 + theta1*x
    cost = 0.5*np.sum((h-y)**2)
    return cost


def gradient(x, y, theta0, theta1):
    """Compute the partial derivative of the squared error cost function

    Inputs:
    x          vector of length m containing x values
    y          vector of length m containing y values
    theta_0    (scalar) intercept parameter
    theta_1    (scalar) slope parameter

    Returns:
    d_theta_0  (scalar) Partial derivative of cost function wrt theta_0
    d_theta_1  (scalar) Partial derivative of cost function wrt theta_1
    """

    d_theta0 = 0.0
    d_theta1 = 0.0

    ##################################################
    # TODO: write code here to compute partial derivatives correctly
    ##################################################
    h = theta0 + theta1*x
    d_theta0 = np.sum(h - y)
    d_theta1 = np.dot((h - y),x)
    
    return d_theta0, d_theta1 # return is a tuple