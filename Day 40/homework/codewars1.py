def high_and_low(numbers):
    numbers = [int(i) for i in numbers.split(" ")]
    return f"{max(numbers)} {min(numbers)}"