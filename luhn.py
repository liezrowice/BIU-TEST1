
#!/usr/bin/env python3
def luhn_algorithm(number):
    # Convert the number to a list of integers
    digits = [int(digit) for digit in str(number)]
    
    # Double every second digit from the right (excluding the check digit to be calculated)
    for i in range(len(digits) - 1, -1, -2):
        doubled = digits[i] * 2
        # If doubling the digit results in a number greater than 9, subtract 9
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled
    
    # Sum all the digits
    total_sum = sum(digits)
    
    # The check digit is the difference to the next multiple of 10
    check_digit = (10 - (total_sum % 10)) % 10
    return check_digit

# Input from the user
number = input("Enter the number (without check digit): ")
check_digit = luhn_algorithm(number)
print(f"The check digit is: {check_digit}")


