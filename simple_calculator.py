def add(a, b):
    """
    Add two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Subtract two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The difference between the two numbers.
    """
    return a - b

def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The product of the two numbers.
    """
    return a * b

def divide(a, b):
    """
    Divide two numbers.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The quotient of the two numbers.

    Raises:
    ValueError: If the second number (divisor) is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    # Example usage
    num1 = 10
    num2 = 5

    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
    print(f"{num1} / {num2} = {divide(num1, num2)}")
