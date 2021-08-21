def recursive_knapsack(weight_cap, weights, values, i):
    if weight_cap == 0 or i == 0:
        return 0
    elif weights[i - 1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i - 1)
    else:
        include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)
        exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1)

        return max(include_item, exclude_item)


weight_cap = 50
weights = [31, 10, 20, 19, 4, 3, 6]
values = [70, 20, 39, 37, 7, 5, 10]
print(recursive_knapsack(weight_cap, weights, values, len(values)))