def knapsack_problem():
    # The solution is to use dynamic programming and memoization
    class Item():
        def __init__(self, name, weight, value):
            self.name = name
            self.weight = weight
            self.value = value

        def __repr__(self):
            return self.name

    
    # Items should be list of item objects
    def knapsack(items, max_capacity):
        # This is the dynamic programming table
        # List of list of floats
        # Rows are # of items allowed
        # Columns are different capacities
        table = [[0.0 for _ in range(max_capacity + 1)] for _ in range(len(items) + 1)]
        for i, item in enumerate(items):
            for capacity in range(1, max_capacity + 1):
                previous_items_value = table[i][capacity]
                if capacity >= item.weight:
                    value_freeing_weight_for_item = table[i][capacity - item.weight]
                    table[i + 1][capacity] = max(value_freeing_weight_for_item + item.value, previous_items_value)
                else:
                    table[i + 1][capacity] = previous_items_value
        
        # You can deduce the solution by going up the table and to the left
        # Whenever the value changes, you know that the new item at that row was added
        solution = []
        capacity = max_capacity
        for i in range(len(items), 0, -1):
            if table[i - 1][capacity] != table[i][capacity]:
                solution.append(items[i - 1])
                capacity -= items[i - 1].weight
        return solution
    
    # For test, items are hockey players, like in a fantasy lineup
    items = [
        Item("TV", 50, 500),
        Item("Candlesticks", 2, 300),
        Item("Stereo", 35, 400),
        Item("Laptop", 3, 1000),
        Item("Food", 15, 50),
        Item("Clothing", 20, 800),
        Item("Jewelry", 1, 4000),
        Item("Books", 100, 300),
        Item("Printer", 100, 300),
        Item("Refrigerator", 200, 700),
        Item("Painting", 10, 1000)
    ]
    print(knapsack(items, 75))

knapsack_problem()