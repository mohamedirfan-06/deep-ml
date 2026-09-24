import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
   
    g_value = np.polyval(g_coeffs, x)
    h_value = np.polyval(h_coeffs, x)

    g_derivative = np.polyder(g_coeffs)
    h_derivative = np.polyder(h_coeffs)

    g_prime = np.polyval(g_derivative, x)
    h_prime = np.polyval(h_derivative, x)

    return (g_prime * h_value - g_value * h_prime) / (h_value ** 2)
    pass