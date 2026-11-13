# Typical coding interview question: Two Sum
# Given an array of integers and a target, return the indices of the two numbers
# that add up to the target.

def two_sum(nums, target):
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return [seen[complement], index]
        seen[value] = index

    return []


# Example usage:
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum(numbers, target))  # Output: [0, 1]
 