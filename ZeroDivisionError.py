def divide_numbers(num1, num2):
    return num1 / num2

def safe_division(num1, num2):
    try:
        result = divide_numbers(num1, num2)
        return result
    except ZeroDivisionError:
        return 0
