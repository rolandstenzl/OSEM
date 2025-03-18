import math


def factorial(n):
    """Compute the factorial of n recursively."""
    return 1 if n == 0 else n * factorial(n - 1)


def taylor_sin(x, n):
    """Compute sin(x) using Taylor series expansion up to n terms.

    sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...

    Parameters:
    x (float): Input angle in radians.
    n (int): Number of terms to approximate.

    Returns:
    float: Approximated sine value.
    """
    result = sum(
        (-1) ** k * (x ** (2 * k + 1)) / factorial(2 * k + 1) for k in range(n)
    )
    return result


def taylor_cos(x, n):
    """Compute cos(x) using Taylor series expansion up to n terms.

    cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...

    Parameters:
    x (float): Input angle in radians.
    n (int): Number of terms to approximate.

    Returns:
    float: Approximated cosine value.
    """
    result = sum((-1) ** k * (x ** (2 * k)) / factorial(2 * k) for k in range(n))
    return result


def taylor_tan(x, n):
    """Compute tan(x) as sin(x)/cos(x) using Taylor approximations.

    Parameters:
    x (float): Input angle in radians.
    n (int): Number of terms to approximate.

    Returns:
    float: Approximated tangent value.
    """
    sin_approx = taylor_sin(x, n)  # Compute sin(x) approximation
    cos_approx = taylor_cos(x, n)  # Compute cos(x) approximation
    return (
        sin_approx / cos_approx if cos_approx != 0 else float("inf")
    )  # Avoid division by zero


def taylor_exp(x, n):
    """Compute exp(x) using Taylor series expansion up to n terms.

    exp(x) = 1 + x + x^2/2! + x^3/3! + x^4/4! + ...

    Parameters:
    x (float): Input value.
    n (int): Number of terms to approximate.

    Returns:
    float: Approximated exponential value.
    """
    result = sum((x**k) / factorial(k) for k in range(n))
    return result


# Example usage
x = math.radians(45)  # Convert degrees to radians for trigonometric functions
n = 10  # Number of terms in the series for better approximation

# Compute Taylor series approximations for sin, cos, tan, and exp
sin_approx = taylor_sin(x, n)
cos_approx = taylor_cos(x, n)
tan_approx = taylor_tan(x, n)
exp_approx = taylor_exp(x, n)

# Print results
print(f"sin({x}) ≈ {sin_approx}")
print(f"cos({x}) ≈ {cos_approx}")
print(f"tan({x}) ≈ {tan_approx}")
print(f"exp({x}) ≈ {exp_approx}")
