def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Args:
        price: The original price of the item.
        discount_percent: The discount percentage.

    Returns:
        The final price after applying the discount, or the original price if no discount is applied.
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    
    final_price = calculate_discount(price, discount_percent)
    print("Final price:", final_price)

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
