def binary_search(array: list[int], target: int) -> str:
    low: int = 0
    high: int = len(array) - 1
    steps: int = 0
    while low <= high:
        steps += 1

        mid: int = (low + high) // 2

        if array[mid] == target:
            return f"steps: {steps}, found at index: {mid}"
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return f"steps: {steps}, Not Found"


arr = [item for item in range(1000)]
item = 11
print(binary_search(arr, item))
