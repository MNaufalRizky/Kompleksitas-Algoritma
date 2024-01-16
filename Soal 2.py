def knapsack_backtracking(weights, values, capacity, currentIndex, currentWeight, currentValue, selectedItems, maxValue, solution):
    # Base case: jika kita telah mencapai ujung pohon atau kapasitas tas habis
    if currentIndex == len(weights) or currentWeight == 0:
        if currentValue > maxValue:
            # Simpan solusi yang lebih baik
            solution.clear()
            solution.extend(selectedItems)
            return currentValue
        else:
            return maxValue
    
    # Case 1: Pilih barang saat ini
    if weights[currentIndex] <= currentWeight:
        selectedItems.append(currentIndex)
        value_with_item = knapsack_backtracking(weights, values, capacity, currentIndex + 1,
                                                currentWeight - weights[currentIndex],
                                                currentValue + values[currentIndex],
                                                selectedItems, maxValue, solution)
        selectedItems.pop()  # Backtrack

    # Case 2: Tidak memilih barang saat ini
    value_without_item = knapsack_backtracking(weights, values, capacity, currentIndex + 1,
                                               currentWeight, currentValue, selectedItems, maxValue, solution)

    # Kembalikan nilai maksimal dari kedua kasus
    return max(value_with_item if 'value_with_item' in locals() else 0, value_without_item)

def knapsack_solver(weights, values, capacity):
    currentIndex = 0
    currentWeight = capacity
    currentValue = 0
    selectedItems = []
    maxValue = 0
    solution = []

    result = knapsack_backtracking(weights, values, capacity, currentIndex, currentWeight, currentValue, selectedItems, maxValue, solution)

    return result, solution

# Barang-barang yang dapat dibawa
weights = [5, 3, 1, 6, 2]
values = [12, 8, 4, 20, 6]

# Kapasitas tas
capacity = 10

# Solusi
maxValue, selectedItems = knapsack_solver(weights, values, capacity)

print("Solusi Optimal:")
print("Nilai Maksimal:", maxValue)
print("Barang yang Dipilih:")
for item in selectedItems:
    print("- Barang", item + 1)
