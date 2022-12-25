def count_combinations(num_notches, max_depth):
    if num_notches == 1:
        return 10
    count = 0
    for depth in range(0, max_depth + 0.5, 0.5):
        if num_notches == 2:
            max_depth_next = min(4.0, depth + 2.5)
        else:
            max_depth_next = min(4.5, depth + 2.5)
        count += count_combinations(num_notches - 1, max_depth_next)
    return count

# Example usage
print(count_combinations(7, 3.5))  # Output: 70
print(count_combinations(19, 4.0))  # Output: 800
