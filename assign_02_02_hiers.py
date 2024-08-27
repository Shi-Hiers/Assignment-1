# Shi Hiers Assignment 2:2 MMIS 6391

# Business Prompt: There is a retail store that sells various items. Calculate the total price of an item after applying a sales tax.
# continued:The item price is $50, and the sales tax rate is 8%. Calculate and print the total price including tax.

def calculate_total_price(price, tax_rate):
    # Calculate the total price including tax
    total_price = price * (1 + tax_rate / 100)

    # Print the result
    print(f"Total Price including {tax_rate}% tax: ${total_price:.2f}")


def main():
    # Define parameters
    price = 50
    tax_rate = 8

    # Call the function to calculate and print the total price
    calculate_total_price(price, tax_rate)


if __name__ == "__main__":
    main()