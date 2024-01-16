# Fungsi untuk menyelesaikan masalah Knapsack dengan pendekatan backtracking
def knapsack_backtracking(weights, values, capacity, current_weight, current_value, index, selected_items, best_value, best_items):
    # Basis: Jika kita mencapai akhir barang atau kapasitas tas terlampaui
    if index == len(weights) or current_weight + weights[index] > capacity:
        # Cek apakah nilai saat ini lebih baik dari yang terbaik sejauh ini
        if current_value > best_value:
            best_value = current_value
            best_items = selected_items.copy()
        return best_value, best_items
    
    # Coba memasukkan barang ke dalam tas
    selected_items[index] = 1
    value_with_item, items_with_item = knapsack_backtracking(weights, values, capacity, current_weight + weights[index], current_value + values[index], index + 1, selected_items, best_value, best_items)
    
    # Coba tidak memasukkan barang ke dalam tas
    selected_items[index] = 0
    value_without_item, items_without_item = knapsack_backtracking(weights, values, capacity, current_weight, current_value, index + 1, selected_items, best_value, best_items)
    
    # Pilih solusi terbaik
    if value_with_item > value_without_item:
        return value_with_item, items_with_item
    else:
        return value_without_item, items_without_item

# Barang-barang yang dapat dibawa
weights = [5, 3, 1, 6, 2]
values = [12, 8, 4, 20, 6]

# Kapasitas tas
capacity = 10

# Inisialisasi variabel
current_weight = 0
current_value = 0
index = 0
selected_items = [0] * len(weights)
best_value = 0
best_items = []

# Panggil fungsi knapsack_backtracking
best_value, best_items = knapsack_backtracking(weights, values, capacity, current_weight, current_value, index, selected_items, best_value, best_items)

# Tampilkan hasil
print("Barang yang harus Anda bawa untuk mendapatkan nilai maksimal:")
for i in range(len(best_items)):
    if best_items[i] == 1:
        print(f"{i + 1}. Barang - Berat: {weights[i]} kg, Nilai: {values[i]}")
print(f"Total Nilai: {best_value}")
