#example

def calculate_average(numbers):
    total = 0
    for number in numbers:
        if not isinstance(number, (int,float)):
            raise TypeError("Invalid data type. All values must be numbers.")
        total += number
    average = total / len(numbers)

    return average

# Example script to calculate averages

# def calculate_average(numbers):
#     """
#     Calculate the average of a list of numbers.
    
#     Args:
#         numbers (list): List of numbers to calculate average from
        
#     Returns:
#         float: The average of the numbers
        
#     Raises:
#         TypeError: If any value is not a number
#         ValueError: If the list is empty
#     """
#     if not numbers:
#         raise ValueError("Cannot calculate average of an empty list.")
    
#     total = 0
#     for number in numbers:
#         if not isinstance(number, (int, float)):  # Fixed: "no" -> "not"
#             raise TypeError("Invalid data type. All values must be numbers.")
#         total += number
    
#     average = total / len(numbers)
#     return average


def main():
    """Main function to demonstrate the calculate_average function."""
    try:
        # Test cases
        test_data = [
            [1, 2, 3, 4, 5],
            [10.5, 20.3, 15.7],
            [100],
            [-5, -10, -15, 5, 10, 15]
        ]
        
        for i, numbers in enumerate(test_data, 1):
            avg = calculate_average(numbers)
            print(f"Test {i}: {numbers}")
            print(f"Average: {avg:.2f}")
            print("-" * 30)
            
        # Test error handling
        print("\nTesting error handling:")
        
        # Empty list test
        try:
            calculate_average([])
        except ValueError as e:
            print(f"Empty list error: {e}")
            
        # Invalid data type test
        try:
            calculate_average([1, 2, "3", 4])
        except TypeError as e:
            print(f"Type error: {e}")
            
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()