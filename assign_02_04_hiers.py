# Shi Hiers Assignment 2:4 MMIS 6391

# Business Prompt: A small business needs to calculate the profit margin of a product. The product's selling price is $120, and the cost
# Continued: to produce it is $80. Calculate and print the profit margin percentage.

def calculate_profit_margin(selling_price, cost_price):
    # Calculate the profit margin percentage
    profit_margin = ((selling_price - cost_price) / selling_price) * 100

    # Print the result
    print(f"Profit Margin: {profit_margin:.2f}%")


def main():
    # Define parameters
    selling_price = 120
    cost_price = 80

    # Call the function to calculate and print the profit margin
    calculate_profit_margin(selling_price, cost_price)


if __name__ == "__main__":
    main()
