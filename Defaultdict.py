from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'egg', 'spam', 'spam']:
    food_counter[food] += 1
for food, counter in food_counter.items():
        print(food, counter)
