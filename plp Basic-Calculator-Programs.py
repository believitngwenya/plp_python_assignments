def main():
    try:
        # Get user inputs
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform calculation based on operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                 raise ZeroDivisionError("Division by zero is not allowed")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation. Please use +, -, *, or /")
        
        # Display the result
        print(f"\n{num1} {operation} {num2} = {result}")
    
    except ValueError as ve:
        print(f"\nError: {ve}")
    except ZeroDivisionError as zde:
        print(f"\nError: {zde}")

if __name__ == "__main__":
    main()