# Shi Hiers Assignment 2:1 MMIS 6391

# Business Prompt: There is a small online store that sells notebooks. Each notebook costs $7, and 120 notebooks have been sold this month.
# continued:The monthly fixed costs (website hosting, etc.) are $200, and the variable cost per notebook (printing, packaging, etc.) is $2.


def calculate_finances(price_per_notebook, notebooks_sold, fixed_costs, variable_cost_per_notebook):
    # Calculate total revenue
    total_revenue = price_per_notebook * notebooks_sold

    # Calculate total variable cost
    total_variable_cost = variable_cost_per_notebook * notebooks_sold

    # Calculate total cost
    total_cost = fixed_costs + total_variable_cost

    # Calculate profit
    profit = total_revenue - total_cost

    # Print the results
    print("Total Revenue: $", total_revenue)
    print("Total Cost: $", total_cost)
    print("Monthly Profit: $", profit)


def main():
    # Define parameters
    price_per_notebook = 7
    notebooks_sold = 120
    fixed_costs = 200
    variable_cost_per_notebook = 2

    # Call the function to calculate and print finances
    calculate_finances(price_per_notebook, notebooks_sold, fixed_costs, variable_cost_per_notebook)


if __name__ == "__main__":
    main()
