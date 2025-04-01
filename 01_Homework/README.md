# OSEM 
Homework, exercises and tests done in uni lecture OSEM

## Test

## Homework assignment 1 
**CI Homework - Math Utilities**

### **Features**
This project implements **Taylor series approximations** for common mathematical functions, allowing for precise calculations using a specified number of terms.

- **`factorial(n)`**: Computes the factorial of `n` recursively.
- **`taylor_sin(x, n)`**: Approximates `sin(x)` using the Taylor series expansion up to `n` terms.
- **`taylor_cos(x, n)`**: Approximates `cos(x)` using the Taylor series expansion up to `n` terms.
- **`taylor_tan(x, n)`**: Computes `tan(x)` using `sin(x)/cos(x)` based on their Taylor series approximations.
- **`taylor_exp(x, n)`**: Approximates `exp(x)` (Euler's number `e^x`) using the Taylor series expansion up to `n` terms.

Each function provides a mathematical approximation that becomes **more accurate as `n` increases**.

---

### Installation
No external dependencies required. Simply clone the repo and run:

### Running Tests

This project includes tests to validate the accuracy of the Taylor series approximations.

#### Prerequisites
Ensure you have `pytest` installed. If not, install it with:

# [LICENSE](./LICENSE)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
