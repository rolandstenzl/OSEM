import pytest
import math
from taylorapproximation_trigonometric_functions import (
    factorial,
    taylor_sin,
    taylor_cos,
    taylor_tan,
    taylor_exp,
)


# Test function for factorial
# Ensures correct computation of factorial values
def test_factorial():
    assert factorial(0) == 1  # 0! = 1
    assert factorial(1) == 1  # 1! = 1
    assert factorial(5) == 120  # 5! = 5 * 4 * 3 * 2 * 1 = 120
    assert factorial(6) == 720  # 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720


# Test function for Taylor series approximation of sine
# Compares the approximation to the actual math.sin() function
def test_taylor_sin():
    x = math.radians(30)  # Convert 30 degrees to radians
    assert pytest.approx(taylor_sin(x, 10), rel=1e-3) == math.sin(
        x
    )  # Check approximation within small error margin


# Test function for Taylor series approximation of cosine
# Compares the approximation to the actual math.cos() function
def test_taylor_cos():
    x = math.radians(60)  # Convert 60 degrees to radians
    assert pytest.approx(taylor_cos(x, 10), rel=1e-3) == math.cos(
        x
    )  # Check approximation within small error margin


# Test function for Taylor series approximation of tangent
# Compares the approximation to the actual math.tan() function
def test_taylor_tan():
    x = math.radians(45)  # Convert 45 degrees to radians
    assert pytest.approx(taylor_tan(x, 10), rel=1e-3) == math.tan(
        x
    )  # Check approximation within small error margin


# Test function for Taylor series approximation of exponential function
# Compares the approximation to the actual math.exp() function
def test_taylor_exp():
    x = 1  # Test e^1
    assert pytest.approx(taylor_exp(x, 10), rel=1e-3) == math.exp(
        x
    )  # Check approximation within small error margin


# Run tests if script is executed directly
if __name__ == "__main__":
    pytest.main()
