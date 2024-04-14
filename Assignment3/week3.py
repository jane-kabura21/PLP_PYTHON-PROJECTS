def calculate_discount(price, discount_percent):
    """Calculates the final price after applying a discount (if applicable).

    Args:
        price: The original price of the item (float).
        discount_percent: The discount percentage (0 to 100).

    Returns:
        The final price after applying the discount, or the original price
        if the discount is less than 20%.
    """

    if discount_percent >= 20:
        discount = price * discount_percent / 100
        final_price = price - discount
    else:
        final_price = price

    return final_price


original_price = float(input("Enter the original price:  "))
discount_percent = float(input("Enter the discount percentage (0-100): "))


if discount_percent < 0 or discount_percent > 100:
    print("Invalid discount percentage. Please enter a value between 0 and 100.")
else:
    
    final_price = calculate_discount(original_price, discount_percent)
    print(f"Final price after discount: ${final_price:.2f}")