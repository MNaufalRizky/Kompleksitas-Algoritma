def knapsack_backtracking(weights, values, capacity, currentIndex, currentWeight, currentValue):
    # Base case: jika kita telah mencapai ujung pohon atau kapasitas tas habis
    if currentIndex == len(weights) or currentWeight == 0:
        return currentValue

    # Case 1: Pilih barang saat ini
    if weights[currentIndex] <= currentWeight:
        value_with_item = knapsack_backtracking(weights, values, capacity, currentIndex + 1,
                                                currentWeight - weights[currentIndex],
                                                currentValue + values[currentIndex])

    # Case 2: Tidak memilih barang saat ini
    value_without_item = knapsack_backtracking(weights, values, capacity, currentIndex + 1,
                                               currentWeight, currentValue)

    # Kembalikan nilai maksimal dari kedua kasus
    return max(value_with_item if 'value_with_item' in locals() else 0, value_without_item)

# Barang-barang yang dapat dibawa
weights = [5, 3, 1, 6, 2]
values = [12, 8, 4, 20, 6]

# Kapasitas tas
capacity = 10

# Hitung nilai total dengan knapsack backtracking
total_value = knapsack_backtracking(weights, values, capacity, 0, capacity, 0)

print("Nilai total yang dapat Anda dapatkan:", total_value)
