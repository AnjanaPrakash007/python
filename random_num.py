import random
import csv
import time

random_numbers = [random.randint(1, 500) for _ in range(500)] 
# Writing the random numbers to a CSV file
with open('random_numbers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Random Number'])
    writer.writerows([[num] for num in random_numbers])

print(f"{len(random_numbers)} random numbers have been generated and saved to 'random_numbers.csv'")

# Bubble sort
def bubble_sort(numbers):
    n = len(numbers)
    num_of_comparisons = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            num_of_comparisons += 1
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
    print(f"Number of comparisons in Bubble Sort: {num_of_comparisons}")   
    return numbers

# Read data from the CSV file
with open('random_numbers.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    numbers = [int(row[0]) for row in reader]

bubble_sort(numbers)
start_time = time.time()
end_time = time.time()
print("Bubble Sort for 500 numbers:\n", numbers)
print("Time taken for Bubble sort:\n", end_time - start_time, "seconds")

#quicksort
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_with_comparisons(numbers):
    if len(numbers) <= 1:
        return numbers, 0

    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]

    sorted_left, left_comparisons = quick_sort_with_comparisons(left)
    sorted_right, right_comparisons = quick_sort_with_comparisons(right)

    return sorted_left + middle + sorted_right, len(numbers) - 1 + left_comparisons + right_comparisons


numbers = quick_sort(numbers)
start_time = time.time()
sorted_numbers, num_comparisons = quick_sort_with_comparisons(numbers)
end_time = time.time()
# Print the sorted numbers and number of comparisons
print("\n##########################################################\n")
print("Quicksort for 500 numbers:", sorted_numbers)
print("Number of comparisons in Quicksort:", num_comparisons)
print("Time taken for Quicksort:", end_time - start_time, "seconds")

#Merge sort
def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers, 0 

    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    left, left_comparisons = merge_sort(left)  
    right, right_comparisons = merge_sort(right)  

    merged, merge_comparisons = merge(left, right)  

    total_comparisons = left_comparisons + right_comparisons + merge_comparisons

    return merged, total_comparisons

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    comparisons = 0  

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
        comparisons += 1  

    merged += left[left_index:]
    merged += right[right_index:]

    return merged, comparisons  


sorted_numbers, comparisons = merge_sort(numbers)
start_time = time.time()
sorted_numbers, comparisons = merge_sort(numbers)
end_time = time.time()
print("\n##########################################################\n")
print("Mergesort of 500 numbers:", sorted_numbers)
print("Number of comparisons in Mergesort:", comparisons)
print("Time taken for Mergesort:", end_time - start_time, "seconds")
