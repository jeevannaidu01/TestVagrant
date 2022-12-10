import itertools

# Define a dictionary to store the newspaper prices for each day of the week
prices = {
    "Monday": {
        "TOI": 3,
        "Hindu": 2.5,
        "ET": 4,
        "BM": 1.5,
        "HT": 2
    },
    "Tuesday": {
        "TOI": 3,
        "Hindu": 2.5,
        "ET": 4,
        "BM": 1.5,
        "HT": 2
    },
    "Wednesday": {
        "TOI": 3,
        "Hindu": 2.5,
        "ET": 4,
        "BM": 1.5,
        "HT": 2
    },
    "Thursday": {
        "TOI": 3,
        "Hindu": 2.5,
        "ET": 4,
        "BM": 1.5,
        "HT": 2
    },
    "Friday": {
        "TOI": 3,
        "Hindu": 2.5,
        "ET": 4,
        "BM": 1.5,
        "HT": 2
    },
    "Saturday": {
        "TOI": 5,
        "Hindu": 4,
        "ET": 4,
        "BM": 1.5,
        "HT": 4
    },
    "Sunday": {
        "TOI": 6,
        "Hindu": 4,
        "ET": 10,
        "BM": 1.5,
        "HT": 4
    }
}


# Define a function to calculate the weekly subscription expenses for a given set of newspapers
def calculate_weekly_subscription(prices, newspapers):
    # Initialize the total cost to 0
    total_cost = 0

    # Loop over the prices for each day of the week
    for day, day_prices in prices.items():
        # Loop over the given newspapers
        for newspaper in newspapers:
            # If the given newspaper is available on this day, add its price to the total cost
            if newspaper in day_prices:
                total_cost += day_prices[newspaper]

    # Return the total weekly subscription cost for the given set of newspapers
    return total_cost


# Define a function to find all possible combinations of subscriptions that the user can afford
def find_subscriptions(prices, budget):
    # Get a list of all the newspapers that are available
    newspapers = []
    for day, day_prices in prices.items():
        for newspaper in day_prices:
            if newspaper not in newspapers:
                newspapers.append(newspaper)

    # Initialize a list to store all possible combinations of subscriptions
    subscriptions = []

    # Loop over all possible combinations of newspapers
    for i in range(2,
                   len(newspapers) + 1):  # Start the loop at 2 to only include combinations with more than one newspaper
        for combination in itertools.combinations(newspapers, i):
            # Calculate the weekly subscription cost for the current combination
            subscription_cost = calculate_weekly_subscription(prices, combination)

            # If the subscription cost is less than or equal to the given budget, add it to the list of subscriptions
            if subscription_cost <= budget:
                subscriptions.append(combination)

    # Return the list of all possible subscriptions that the user can afford
    return subscriptions


budget = int(input("Enter your weekly budget: "))
subscriptions = find_subscriptions(prices, budget)
print(
    f"All possible combinations of subscriptions that the user can afford with a weekly budget of {budget}: {subscriptions}")