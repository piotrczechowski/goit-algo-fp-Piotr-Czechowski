# Data
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Calculate the calorie-to-cost ratio for each item
    items_sorted = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    total_cost = 0
    selected_items = []

    for item, data in items_sorted:
        if total_cost + data["cost"] <= budget:
            selected_items.append(item)
            total_calories += data["calories"]
            total_cost += data["cost"]

    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    n = len(items)
    item_names = list(items.keys())
    costs = [items[item]["cost"] for item in item_names]
    calories = [items[item]["calories"] for item in item_names]

    # Initialize DP table
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Find the selected items
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]

    total_calories = dp[n][budget]
    total_cost = sum(items[item]["cost"] for item in selected_items)

    return selected_items, total_calories, total_cost

# Example usage
budget = 100

# Greedy algorithm
greedy_result = greedy_algorithm(items, budget)
print("Greedy Algorithm:")
print("Selected items:", greedy_result[0])
print("Total calories:", greedy_result[1])
print("Total cost:", greedy_result[2])

# Dynamic programming
dp_result = dynamic_programming(items, budget)
print("\nDynamic Programming:")
print("Selected items:", dp_result[0])
print("Total calories:", dp_result[1])
print("Total cost:", dp_result[2])
