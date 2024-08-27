# Shi Hiers Assignment 2:3 MMIS 6391

#Business Prompt: Manage a subscription-based service. Charge $15 per month per subscriber. Last month, there were 250 subscribers.
# Continued: Calculate and print the total monthly revenue.

def calculate_revenue(subscribers, monthly_rate):
    # Calculate the total monthly revenue
    total_revenue = subscribers * monthly_rate

    # Print the result
    print(f"Total Monthly Revenue: ${total_revenue}")


def main():
    # Define parameters
    subscribers = 250
    monthly_rate = 15

    # Call the function to calculate and print the total revenue
    calculate_revenue(subscribers, monthly_rate)


if __name__ == "__main__":
    main()
