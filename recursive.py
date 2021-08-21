def recursive_knapsack(weight_cap, weights, values, i):
    if weight_cap == 0 or i == 0:
        return 0
    elif weights[i - 1] > weight_cap:
        return recursive_knapsack(weight_cap, weights, values, i - 1)
    else:
        include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)
        exclude_item = recursive_knapsack(weight, weights, values, i - 1)

        return max(include_item, exlucde_item)