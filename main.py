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


#test2

# Example usage:
if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(two_sum(numbers, target))  # Output: [0, 1]


##
#if __name__ == "__main__":
#    numbers = [3, 2, 4]
#    target = 6
#    print(two_sum(numbers, target))  # Output: [1, 2]


 