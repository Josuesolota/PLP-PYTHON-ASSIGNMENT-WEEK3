def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage.

    Returns:
        float: The final price after the discount is applied, or the original price if the
               discount is less than 20%.
    """
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price by subtracting the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# --- Main part of the program ---

# Prompt the user to enter the original price
try:
    original_price = float(input("Enter the original price of the item: "))
    
    # Prompt the user to enter the discount percentage
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Call the function to calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Check if a discount was applied and print the result
    if final_price < original_price:
        print(f"Final price after a {discount_percentage:.2f}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. The price remains: ${original_price:.2f}")

except ValueError:
    print("Invalid input. Please enter valid numbers for price and discount.")